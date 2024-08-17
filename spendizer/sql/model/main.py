import datetime
import uuid
from sqlmodel import Field, SQLModel


class Receipt(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    date: datetime.datetime = Field(
        default_factory=datetime.utcnow, nullable=False
    )
    market_id: uuid.UUID = Field(default=None, foreign_key="marketplace.id")
    total: float


class Item(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    receipt_id: uuid.UUID | None = Field(
        default=None, foreign_key="receipt.id"
    )
    unit_price: float


class Marketplace(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
