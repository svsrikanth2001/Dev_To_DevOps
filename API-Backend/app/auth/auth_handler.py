import time
from typing import Dict
import jwt

from app.commonlib.configuration_handler import ConfigurationHandler

config = ConfigurationHandler()


def sign_jwt_aspirant(applicant_id: str) -> Dict[str, str]:
    payload = {
        "applicant_id": applicant_id,
        "expires": time.time() + 3600
    }
    token = jwt.encode(payload, config.AUTH_JWT_SECRET, algorithm=config.AUTH_JWT_ALGORITHM)
    return {
        "access_token": token.decode('utf-8')
    }