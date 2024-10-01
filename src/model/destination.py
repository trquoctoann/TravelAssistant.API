from sqlmodel import Field

from model.base_model import BaseModel


class Destination(BaseModel, table=True):
    title: str = Field(default=None, nullable=True)
    link: str = Field(default=None, nullable=True)
    rate: float = Field(default=None, nullable=True)
    overall_review: str = Field(default=None, nullable=True)
    address: str = Field(default=None, nullable=True)
