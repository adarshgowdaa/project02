from pydantic import BaseModel, Field
from typing import Optional

class Passenger(BaseModel):
    PassengerId: int
    Survived: int
    Pclass: int
    Name: str
    Sex: str
    Age: Optional[float] = None
    SibSp: int
    Parch: int
    Ticket: str
    Fare: float
    Cabin: Optional[str] = None  # Allow Cabin to be None
    Embarked: Optional[str] = None

class UpdatePassenger(BaseModel):
    Survived: Optional[int] = None
    Pclass: Optional[int] = None
    Name: Optional[str] = None
    Sex: Optional[str] = None
    Age: Optional[float] = None
    SibSp: Optional[int] = None
    Parch: Optional[int] = None
    Ticket: Optional[str] = None
    Fare: Optional[float] = None
    Cabin: Optional[str] = None  # Allow Cabin to be None
    Embarked: Optional[str] = None

class GenderSurvivedPayload(BaseModel):
    gender: str

class UploadResponse(BaseModel):
    success: bool
    message: str
    inserted_count: int
