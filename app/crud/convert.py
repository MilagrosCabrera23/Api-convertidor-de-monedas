from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.convert import Conversion
from app.schemas.convert import ConversionRequest 

def create_conversion(db: Session, data: ConversionRequest, exchange_rate: float, result:float):
    db_conversion = Conversion(from_currency=data.from_currency,
        to_currency=data.to_currency,
        amount=data.amount,
        exchange_rate=exchange_rate,
        result=result,
        user_id=data.user_id
        )
    db.add(db_conversion)
    db.commit()
    db.refresh(db_conversion)
    return db_conversion

def get_all_conversions(db: Session):
    return db.query(Conversion).all()

def get_conversions_by_user(db: Session, user_id: int):
    return db.query(Conversion).filter(Conversion.user_id == user_id).all()

def update_conversion(db: Session, conversion_id: int, data: ConversionRequest):
    db_conversion = db.query(Conversion).filter(Conversion.id == conversion_id).first()

    if not db_conversion:
        raise HTTPException(status_code=404, detail="No se encontro la conversion")
   
    db_conversion.from_currency = data.from_currency
    db_conversion.to_currency = data.to_currency
    db_conversion.amount = data.amount
    db_conversion.user_id = data.user_id

    db.commit() 
    db.refresh(db_conversion)
    return db_conversion

def delete_conversion(db: Session, conversion_id: int):
    conversion = db.query(Conversion).filter(Conversion.id == conversion_id).first()
    if not conversion:
        raise HTTPException(status_code=404, detail="No se encontro la conversion")
    
    db.delete(conversion)
    db.commit()
    return conversion
    
