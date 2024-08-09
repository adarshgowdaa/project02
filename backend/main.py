import logging
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from model import Passenger, UpdatePassenger, GenderSurvivedPayload, UploadResponse

from database import (
    get_all_passengers,
    get_passenger_by_id,
    create_passenger,
    update_passenger,
    get_survived_count,
)
import pandas as pd
import io

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello, Upload File"}

@app.post("/upload", response_model=UploadResponse)
async def upload_excel(file: UploadFile = File(...)):
    try:
        logger.info(f"File upload initiated: {file.filename}")
        
        if not file.filename.endswith('.xlsx'):
            logger.warning("Invalid file format attempted")
            raise HTTPException(status_code=400, detail="Invalid file format. Please upload a .xlsx file.")
        
        content = await file.read()
        df = pd.read_excel(io.BytesIO(content))
        
        # Fill NaN values with None
        df = df.where(pd.notnull(df), None)
        
        records = df.to_dict(orient='records')
        inserted_count = await create_passenger(records)
        
        logger.info(f"File uploaded successfully, {inserted_count} records inserted")
        return UploadResponse(success=True, message="File uploaded successfully", inserted_count=inserted_count)
    
    except Exception as e:
        logger.error(f"Error during file upload: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the file.")

@app.get("/api/passenger/{passenger_id}/", response_model=Passenger)
async def get_passenger(passenger_id: int):
    try:
        logger.info(f"Fetching passenger with ID: {passenger_id}")
        passenger = await get_passenger_by_id(passenger_id)
        if passenger:
            logger.info(f"Passenger found: {passenger_id}")
            return passenger
        logger.warning(f"Passenger not found: {passenger_id}")
        raise HTTPException(status_code=404, detail="Passenger not found")
    
    except Exception as e:
        logger.error(f"Error fetching passenger with ID {passenger_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching the passenger.")

@app.put("/api/passenger/{passenger_id}/", response_model=Passenger)
async def put_passenger(passenger_id: int, passenger: UpdatePassenger):
    try:
        logger.info(f"Updating passenger with ID: {passenger_id}")
        if await update_passenger(passenger_id, passenger.dict()):
            logger.info(f"Passenger updated: {passenger_id}")
            return await get_passenger_by_id(passenger_id)
        logger.warning(f"Passenger not found for update: {passenger_id}")
        raise HTTPException(status_code=404, detail="Passenger not found")
    
    except Exception as e:
        logger.error(f"Error updating passenger with ID {passenger_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while updating the passenger.")

@app.post("/api/survived")
async def survived(payload: GenderSurvivedPayload):
    try:
        logger.info(f"Survival count requested for gender: {payload.gender}")
        count = await get_survived_count(payload.gender)
        logger.info(f"Survived count for {payload.gender}: {count}")
        return {"gender": payload.gender, "survived_count": count}
    
    except Exception as e:
        logger.error(f"Error fetching survived count for gender {payload.gender}: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching the survived count.")