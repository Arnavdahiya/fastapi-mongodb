from fastapi import APIRouter, HTTPException
from models.user import Product, UpdateProduct
from config.db import product_collection
from schemas.user import serialize_dict, serialize_list
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.get("/")
def find_all_products():
    return serialize_list(product_collection.find())

@router.get("/{id}")
def find_one_product(id: str):
    product = product_collection.find_one({"_id": ObjectId(id)})
    if product:
        return serialize_dict(product)
    raise HTTPException(status_code=404, detail=f"Product {id} not found")

@router.post("/")
def create_product(product: Product):
    product.created_at = datetime.now()
    product_collection.insert_one(product.dict())
    return serialize_list(product_collection.find())

@router.put("/{id}")
def update_product(id: str, product: UpdateProduct):
    product_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": product.dict(exclude_unset=True)}
    )
    return serialize_dict(product_collection.find_one({"_id": ObjectId(id)}))

@router.delete("/{id}")
def delete_product(id: str):
    product = product_collection.find_one_and_delete({"_id": ObjectId(id)})
    if product:
        return serialize_dict(product)
    raise HTTPException(status_code=404, detail=f"Product {id} not found")
