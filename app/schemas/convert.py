from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ConversionRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    user_id: Optional[int] = None  

class ConversionResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    exchange_rate: float  
    result: float
    timestamp: datetime  

    class Config:
        orm_mode = True
