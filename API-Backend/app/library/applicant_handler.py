from app.library.configuration_handler import ConfigurationHandler
from fastapi import status,Depends, Request, Response
from app.auth.auth_bearer import JWTBearer


# class to hold sub-dependencies needed for customer API routes.
class ApplicantDependencies():
    def __init__(self, config: ConfigurationHandler = Depends(ConfigurationHandler), jwt_token: JWTBearer = Depends(JWTBearer())):
        # set attributes from dependencies injected into constructor as defaults
        self.config = config
        self.jwt_token = jwt_token

        # decrypt our token
        self.decrypted_token = JWTBearer.decode_jwt(self.jwt_token)

        # set our token keys as atributes



