import json
from fastapi import APIRouter
from fastapi import status, Request, HTTPException
from app.models.authentication import AuthReadModel,AuthResponseModel
import re
from datetime import datetime, timedelta, timezone

from app.commonlib.configuration_handler import ConfigurationHandler
from app.library import request_handler
from app.commonlib.hashlib import HashHandler
from app.commonlib import auth_external_token_handler

router = APIRouter()
router_tag = "Authentication"  

config = ConfigurationHandler()

@router.post("/authenticate", response_model=AuthResponseModel, tags=[router_tag])
def register(usernamepwd: AuthReadModel, request: Request):
    applicant_response = request_handler.post(url=f"{config.API_BACKEND_URL}/applicant/search",
                                    data=json.dumps(
                                        {"username": usernamepwd.username}),
                                    raise_exception=HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,
                                                                  detail=f"There was a problem retrieving customer data."),
                                    x_correlation_id=request.state.__getattr__('x-correlation-id')
                                    )
    if not applicant_response:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail= f"User {usernamepwd.username} could not be found")                                

    applicant_data = applicant_response[0]
    # Check if the password sent and stored matches in system 
    pwdhandler = HashHandler()
    input_password =   pwdhandler.hash_password_to_hex_string(usernamepwd.password)                              

    #If input password matches the stored password then generate a token 
    if input_password == applicant_data['password']:
        token = auth_external_token_handler.sign_jwt(applicant_data['id'],applicant_data)
        return token 
    else:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,
                            detail=f"The password is incorrect.")




    
    
    return json.dumps(returnval)