from typing import Optional, List

from pydantic import BaseModel

from schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from utils.schema import all_optional


class BaseDestination(BaseModel):
    title: Optional[str] = None
    link: Optional[str] = None
    rate: Optional[float] = None
    overall_review: Optional[str] = None
    address: Optional[str] = None

    class Config:
        from_attributes = True


@all_optional
class Destination(ModelBaseInfo, BaseDestination):
    pass


@all_optional
class FindDestination(FindBase, BaseDestination):
    pass


@all_optional
class UpsertDestination(BaseDestination):
    pass


@all_optional
class FindDestinationResult(BaseModel):
    founds: Optional[List[Destination]]
    search_options: Optional[SearchOptions]
