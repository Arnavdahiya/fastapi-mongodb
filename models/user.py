from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional

class Product(BaseModel):
    product_name: str
    product_owner: str
    created_at: datetime
    status: bool
    @validator("product_name", "product_owner")
    def name_must_be_longer_than_two_chars(cls, v):
        if len(v) < 3:
            raise ValueError("must be longer than 2 characters")
        return v

class UpdateProduct(BaseModel):
    product_name: Optional[str] = None
    status: Optional[bool] = None
