import datetime
import uuid
from sqlmodel import Field, SQLModel, Relationship


class Receipt(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    date: datetime.datetime = Field(nullable=False)
    market_id: uuid.UUID = Field(foreign_key='marketplace.id', nullable=False)
    total: float = Field(nullable=False)
    items: list['Item'] = Relationship(
        back_populates='receipt', nullable=False
    )


class Item(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(nullable=False)
    receipt_id: uuid.UUID | None = Field(
        default=None, foreign_key='receipt.id'
    )
    unit_price: float = Field(nullable=False)
    receipt: Receipt = Relationship(back_populates='items', nullable=False)


class Marketplace(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(nullable=False)
