from pydantic import BaseModel
from typing import Optional


def all_optional(model_cls):
    for field, field_type in model_cls.__annotations__.items():
        if not field.startswith("__"):
            model_cls.__annotations__[field] = Optional[field_type]
    return model_cls
