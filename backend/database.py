import logging
from motor.motor_asyncio import AsyncIOMotorClient
from model import Passenger
from pymongo import ASCENDING

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# MongoDB connection
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client.titanic
collection = db.passengers

# Create passenger records from a list
async def create_passenger(records):
    try:
        logger.info("Creating passenger records")
        result = await collection.insert_many(records, ordered=False)
        logger.info(f"{len(result.inserted_ids)} passenger records inserted")
        return len(result.inserted_ids)
    except Exception as e:
        logger.error(f"Error creating passenger records: {str(e)}")
        return 0

# Get all passengers
async def fetch_all_passengers():
    try:
        logger.info("Fetching all passengers")
        passengers = []
        async for passenger in collection.find():
            passengers.append(Passenger(**passenger))
        logger.info(f"Fetched {len(passengers)} passengers")
        return passengers
    except Exception as e:
        logger.error(f"Error fetching passengers: {str(e)}")
        return []

# Get passenger by PassengerId
async def get_passenger_by_id(passenger_id: int):
    try:
        logger.info(f"Fetching passenger with ID: {passenger_id}")
        passenger = await collection.find_one({"PassengerId": passenger_id})
        if passenger:
            logger.info(f"Passenger found: {passenger_id}")
            return Passenger(**passenger)
        logger.warning(f"Passenger not found: {passenger_id}")
        return None
    except Exception as e:
        logger.error(f"Error fetching passenger with ID {passenger_id}: {str(e)}")
        return None

# Update a passenger
async def update_passenger(passenger_id: int, data):
    if len(data) < 1:
        logger.warning(f"No data provided to update passenger with ID: {passenger_id}")
        return False
    try:
        logger.info(f"Updating passenger with ID: {passenger_id}")
        response = await collection.update_one({"PassengerId": passenger_id}, {"$set": data})
        if response.modified_count == 1:
            logger.info(f"Passenger updated: {passenger_id}")
            return True
        logger.warning(f"Passenger not updated, possibly not found: {passenger_id}")
        return False
    except Exception as e:
        logger.error(f"Error updating passenger with ID {passenger_id}: {str(e)}")
        return False

# Get count of survived passengers by gender and age < 45
async def get_survived_count(gender: str):
    try:
        logger.info(f"Counting survived passengers with gender {gender} and age < 45")
        count = await collection.count_documents({
            "Sex": gender,
            "Survived": 1,
            "Age": {"$lt": 45}
        })
        logger.info(f"Survived count for gender {gender}: {count}")
        return count
    except Exception as e:
        logger.error(f"Error counting survived passengers for gender {gender}: {str(e)}")
        return 0
