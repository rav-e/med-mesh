# sign, encode, decode and return jwts
import time
import jwt
import os

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

# return generated jwt token
def token_response(token: str):
    return {
        "access_token": token
    }


# sign jwt token
def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expires": time.time() + 1800
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    
    return token_response(token)


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}