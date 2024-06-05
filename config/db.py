from pymongo import MongoClient
conn = MongoClient("mongodb://localhost:27017") 
database = conn.test
product_collection = database.get_collection("products")