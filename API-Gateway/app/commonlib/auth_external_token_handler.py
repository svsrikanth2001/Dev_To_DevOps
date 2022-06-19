import time
from typing import Dict
import jwt
from fastapi import status, Request, HTTPException
import json
from app.commonlib.configuration_handler import ConfigurationHandler


config = ConfigurationHandler()


def sign_jwt(user_id: str, customer_data: dict) -> Dict[str, str]:
    try:
        payload = {
        "user_id": user_id,
        "expires": time.time() + 86400,  # 24hrs
        "firstname": customer_data['firstname'],
        "lastname": customer_data['lastname']}

        token = jwt.encode(payload, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)

        return {
        "access_token": token.decode('utf-8'),
        "user_id": user_id
        }
    
    except IndexError:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="Unable to generate a token")


    

   
  

    
