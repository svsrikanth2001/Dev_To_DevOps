import json
import requests
from fastapi import APIRouter
from fastapi import Depends, HTTPException, Response, status, Request
from api_gateway_web.models import execute
from app.commonlib.configuration_handler import ConfigurationHandler
from app.commonlib.auth_bearer_handler import JWTBearer
from fastapi.encoders import jsonable_encoder
 

router = APIRouter()
router_tag = "Execute"  # groups api routes within Swagger

config = ConfigurationHandler()


@router.post("/execute", response_model=execute.ExecutePostResponseModel, dependencies=[Depends(JWTBearer())],
             tags=[router_tag])
def api_gateway(gateway_post: execute.ExecutePostModel, response: Response, request: Request,
                jwt_token: JWTBearer = Depends(JWTBearer())):
    try:
        gateway_post.service = gateway_post.service.upper()
        service_origin = config.__getattribute__(f"LB_SERVICE_REGISTRY_{gateway_post.service}")
    except AttributeError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"The service {gateway_post.service} does not exist.")

    url = f"{service_origin}"
    correlation_id = request.state.__getattr__(key='x-correlation-id')
    request_id = request.state.__getattr__(key='x-request-id')

    logger = Logger(x_request_id=request_id, x_correlation_id=correlation_id)

    # base headers
    headers = {'Content-Type': 'application/json',
               'accept': 'application/json',
               'x-correlation-id': correlation_id}

    # add our authorization context to headers based on destination.
    if gateway_post.service in ["API_CORE"]:
        headers['x-token'] = config.INTERNAL_API_TOKEN
    else:
        headers['Authorization'] = f"Bearer {jwt_token}"

    if gateway_post.path:
        url += gateway_post.path

    if gateway_post.query:
        url += f"?{gateway_post.query}"

    if gateway_post.method == 'GET':
        request_response = requests.get(url=url,
                                        headers=headers,
                                        verify=False
                                        )
    elif gateway_post.method == 'POST':
        request_response = requests.post(url=url,
                                         headers=headers,
                                         data=json.dumps(gateway_post.data),
                                         verify=False
                                         )
    elif gateway_post.method == 'DELETE':
        request_response = requests.delete(url=url,
                                           headers=headers,
                                           data=json.dumps(gateway_post.data),
                                           verify=False
                                           )

    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"The provided method type is not supported.")

    # initialize a response object and call construct() pydantic method to skip validation for now since we plan to
    # assign values for data and status code one step at a time and then fastapi will validate the response
    # on return. More info https://pydantic-docs.helpmanual.io/usage/models/#creating-models-without-validation
    response_model = execute.ExecutePostResponseModel.construct()

    if request_response.status_code >= 400:
        logger.debug(message=f"API-Gateway-Web Execute", trace=f"Request='{str(request_response.request.__dict__)}' Response='{str(request_response.__dict__)}")

    if request_response.headers.get('content-type') == 'application/json':
        try:
            if request_response.text:
                response_model.data = json.dumps(request_response.json())
        except:
            raise RuntimeError(f"There was an issue trying to decode the response in API-Gateway Execute. Request-Response='{str(request_response.text)}' Request-URL='{request_response.url}'")

    response_model.status_code = request_response.status_code
    response.status_code = request_response.status_code

    return response_model.__dict__  # response object will be validated now on return
