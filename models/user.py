from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Product(BaseModel):
    product_id: int
    product_name: str
    product_owner: str
    created_at: datetime
    status: bool

class UpdateProduct(BaseModel):
    product_name: Optional[str] = None
    status: Optional[bool] = None
