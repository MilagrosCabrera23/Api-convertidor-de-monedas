from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.convert import ConversionRequest, ConversionResponse
from app.api.dependencies.db import get_db
from app.services.convert_service import exchange_rate, convert_currency
from app.crud import convert as conversion_crud

router = APIRouter(prefix="/convert", tags=["convert"])

@router.post("/", response_model=ConversionResponse, status_code=status.HTTP_201_CREATED)
def create_conversion(request:ConversionRequest, db: Session = Depends(get_db)):

    rate = exchange_rate(request.from_currency, request.to_currency)

    result = convert_currency(request.amount, rate)

    conversion = conversion_crud.create_conversion(db, request, rate, result)
    
    return ConversionResponse( from_currency=request.from_currency,
        to_currency=request.to_currency,
        amount=request.amount,
        exchange_rate=rate,
        result=result,
        timestamp=conversion.timestamp)

@router.get("/all", response_model=list[ConversionResponse])
def get_all_conversion(db:Session = Depends(get_db)):
    return  conversion_crud.get_all_conversions(db)

@router.get("/user/{user_id}", response_model=list[ConversionResponse])
def get_conversion_by_user(user_id:int, db:Session = Depends(get_db)):
    return conversion_crud.get_conversions_by_user(db, user_id)

@router.put("/{conversion_id}", response_model=ConversionResponse)
def update_conversion(conversion_id:int, request:ConversionRequest, db:Session = Depends(get_db)):
    updated = conversion_crud.update_conversion(db, conversion_id, request)
    rate = exchange_rate(request.from_currency, request.to_currency)
    result = convert_currency(request.amount, rate)
    updated.exchange_rate = rate
    updated.result = result
    return updated


@router.delete("/{conversion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_conversion(conversion_id:int, db:Session = Depends(get_db)):
    delete = conversion_crud.delete_conversion(db, conversion_id)
    if not delete:
        raise HTTPException(status_code=404, detail="No se encontro la conversion")
    return 