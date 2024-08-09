from locust import HttpUser, TaskSet, task, between
from pydantic import BaseModel

class GenderSurvivedPayload(BaseModel):
    gender: str

class PassengerLoadTest(TaskSet):
    
    @task
    def get_survived_count(self):
        payload = GenderSurvivedPayload(gender="female")
        self.client.post("/api/survived", json=payload.dict())
        
class WebsiteUser(HttpUser):
    tasks = [PassengerLoadTest]
    wait_time = between(1, 5)