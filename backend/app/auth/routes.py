from fastapi import APIRouter, Depends, Body, HTTPException
from aiomysql.connection import Connection
from ..models.customer import CustomerLogin, CustomerSignUp, Customer
from ..database import Database
from ..database.customer import add_customer
from .auth_handler import signJWT
from passlib.context import CryptContext

auth_router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])


# def validate_login(data: CustomerLogin):
#     with open("customers.json") as customer_file:
#         customer_list = json.load(customer_file)

#     for customer in customer_list:
#         if customer["email"] == data.email and hash_helper.verify(data.password, customer["password"]):
#             return True

#     return False


@auth_router.post("/signup")
async def customer_signup(customer: CustomerSignUp = Body(), conn: Connection = Depends(Database.get_db)):
    customer.password = hash_helper.encrypt(customer.password)
    customer_details = await add_customer(customer, conn)
    print(customer_details)
    return {
        "access_token": signJWT(customer.email),
        "data": customer_details
    }


# @auth_router.post("/login")
# async def customer_login(customer: CustomerLogin = Body()):
#     if validate_login(customer):
#         return signJWT(customer.email)
#     else:
#         raise HTTPException(
#             status_code=401, detail="Invalid login credentials")
