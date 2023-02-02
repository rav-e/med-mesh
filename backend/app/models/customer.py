from pydantic import BaseModel, EmailStr


class CustomerLogin(BaseModel):
    email: EmailStr
    password: str


class CustomerSignUp(CustomerLogin):
    name: str
    contact_no: int
    latitude: float
    longitude: float


class Customer(CustomerLogin):
    name: str
    contact_no: int
    latitude: float
    longitude: float
