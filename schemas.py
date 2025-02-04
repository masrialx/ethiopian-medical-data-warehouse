from pydantic import BaseModel
from datetime import datetime

class DataSchema(BaseModel):
    id: int
    text: str
    cleaned_date: datetime
