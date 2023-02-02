from fastapi import HTTPException, status
from ..models.customer import CustomerSignUp
from aiomysql.connection import Connection
from passlib.context import CryptContext

hash_helper = CryptContext(schemes=["bcrypt"])


async def add_customer(customer: CustomerSignUp, conn: Connection):
    async with conn.cursor() as cursor:
        await cursor.execute("""SELECT * FROM customer WHERE email = %s""", (str(customer.email)))
        dub_cust = await cursor.fetchone()
        print(dub_cust)
        if dub_cust:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail=f"user with email: {customer.email} already exist")

        else:
            await cursor.execute(
                """INSERT INTO customer (name, email, password, contact_no, address) VALUES (%s, %s, %s, %s, Point(%s, %s))""",
                (customer.name, str(customer.email), customer.password, str(customer.contact_no), str(customer.latitude), str(customer.longitude)))

            await conn.commit()

            await cursor.execute("""SELECT customer_id, name, email, contact_no, ST_X(address) AS latitude, ST_Y(address) AS longitude FROM customer WHERE email = %s""", customer.email)
            customer = await cursor.fetchone()

        await cursor.close()

    return customer
