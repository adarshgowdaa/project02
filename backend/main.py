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
    return {"message": "Hello, Upload File"}

@app.post("/upload", response_model=UploadResponse)
async def upload_excel(file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a .xlsx file.")
    
    content = await file.read()
    df = pd.read_excel(io.BytesIO(content))
    
    # Fill NaN values with None
    df = df.where(pd.notnull(df), None)
    
    records = df.to_dict(orient='records')
    inserted_count = await create_passenger(records)
    
    return UploadResponse(success=True, message="File uploaded successfully", inserted_count=inserted_count)

@app.get("/api/passengers")
async def get_passengers():
    return await get_all_passengers()

@app.get("/api/passenger/{passenger_id}/", response_model=Passenger)
async def get_passenger(passenger_id: int):
    passenger = await get_passenger_by_id(passenger_id)
    if passenger:
        return passenger
    raise HTTPException(status_code=404, detail="Passenger not found")

@app.put("/api/passenger/{passenger_id}/", response_model=Passenger)
async def put_passenger(passenger_id: int, passenger: UpdatePassenger):
    if await update_passenger(passenger_id, passenger.dict()):
        return await get_passenger_by_id(passenger_id)
    raise HTTPException(status_code=404, detail="Passenger not found")

@app.post("/api/survived")
async def survived(payload: GenderSurvivedPayload):
    count = await get_survived_count(payload.gender)
    return {"gender": payload.gender, "survived_count": count}