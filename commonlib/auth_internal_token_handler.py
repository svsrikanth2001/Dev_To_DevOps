from fastapi import Header,HTTPException
from commonlib.configuration_handler import ConfigurationHandler

config = ConfigurationHandler()


def verify_internal_token(x_token: str=Header(...)):
    if x_token != config.INTERNAL_API_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
