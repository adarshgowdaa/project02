from pydantic import BaseModel, validator
from typing import Optional, Union
import math

class Passenger(BaseModel):
    PassengerId: int
    Survived: int
    Pclass: int
    Name: str
    Sex: str
    Age: Optional[float] = None
    SibSp: int
    Parch: int
    Ticket: Union[str, int]
    Fare: float
    Cabin: Optional[str] = None
    Embarked: Optional[str] = None

    @validator('Age', 'Fare', pre=True, always=True)
    def validate_floats(cls, v):
        if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
            return None  # or a safe default value like 0.0
        return v

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
