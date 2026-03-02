from pydantic import BaseModel


class Data(BaseModel):
    name: str
    balance: float


class AmountSchema(BaseModel):
    amount: float


class TransferSchema(BaseModel):
    sender_id: int
    receiver_id: int
    amount: float
    amount: float
