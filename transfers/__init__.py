from pydantic import BaseModel


# Класс валидации для создания перевода
class CreateTransactionModel(BaseModel):
    card_from: int
    card_to: int
    amount: float


# Класс валидации для отмены перевода
class CanselTransferModel(BaseModel):
    card_from: int
    card_to: int
    amount: float
    transfer_id: int