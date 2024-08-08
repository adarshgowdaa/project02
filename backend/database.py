from motor.motor_asyncio import AsyncIOMotorClient
from model import Passenger
from pymongo import ASCENDING

# Mongo DB connection
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client.titanic
collection = db.passengers

# Create passenger records from a list
async def create_passenger(records):
    try:
        result = await collection.insert_many(records, ordered=False)
        return len(result.inserted_ids)
    except Exception as e:
        return 0

# Get all passengers
async def get_all_passengers():
    passengers = []
    async for passenger in collection.find():
        passengers.append(Passenger(**passenger))
    return passengers

# Get passenger by PassengerId
async def get_passenger_by_id(passenger_id: int):
    passenger = await collection.find_one({"PassengerId": passenger_id})
    if passenger:
        return Passenger(**passenger)
    return None

# Update a passenger
async def update_passenger(passenger_id: int, data):
    if len(data) < 1:
        return False
    response = await collection.update_one({"PassengerId": passenger_id}, {"$set": data})
    if response.modified_count == 1:
        return True
    return False

# Get count of survived passengers by gender and age < 45
async def get_survived_count(gender: str):
    count = await collection.count_documents({
        "Sex": gender,
        "Survived": 1,
        "Age": {"$lt": 45}
    })
    return count