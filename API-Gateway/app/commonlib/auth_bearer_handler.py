from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import jwt
import time
from app.commonlib.configuration_handler import ConfigurationHandler

config = ConfigurationHandler()


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        is_token_valid: bool = False

        try:
            payload = self.decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid

    @staticmethod
    def decode_jwt(token: str) -> dict:
        try:
            decoded_token = jwt.decode(token, config.JWT_SECRET,
                                       algorithms=[config.JWT_ALGORITHM])
            return decoded_token if decoded_token["expires"] >= time.time() else None
        except Exception as  Ex:
            print(Ex)
            return {}
