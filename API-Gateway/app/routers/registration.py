import json
from fastapi import APIRouter
from fastapi import status, Request, HTTPException
from app.models.registration import CreateRegistrationModel, RegistrationResponseModel
import re
from datetime import datetime, timedelta, timezone

from app.commonlib.configuration_handler import ConfigurationHandler
from app.library import request_handler
from app.commonlib.hashlib import HashHandler

router = APIRouter()
router_tag = "Registration"  

config = ConfigurationHandler()

@router.post("/register", response_model=RegistrationResponseModel, tags=[router_tag])
def register(registration: CreateRegistrationModel, request: Request):
    h1 =  HashHandler()

    hash_password = h1.hash_password_to_hex_string(registration.password)
    applicant = request_handler.post(url=f"{config.API_BACKEND_URL}/applicant/create",
                                    data=json.dumps(
                                            {
                                                "username": registration.username,
                                                "password": hash_password,
                                                "firstname": registration.firstname,
                                                "lastname": registration.lastname
                                            }
                                    ),
                                    raise_exception=HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,
                                                                  detail=f"There was a problem retrieving customer data.")
                                    
                                    )
    return applicant