import time
from typing import Dict
import jwt
from fastapi import status, Request, HTTPException
import json
from docuspace_pylib.configuration_handler import ConfigurationHandler
from docuspace_pylib import request_handler

config = ConfigurationHandler()


def sign_jwt(user_id: str, customer_data: dict, request: Request) -> Dict[str, str]:
    customer_security_info = request_handler.post(
        url=f"{config.LB_SERVICE_REGISTRY_API_CORE}/customersecurityinfo/search",
        data=json.dumps({"customer_id": customer_data['id']}),
        raise_exception=HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,
                                      detail=f"There was a problem retrieving customer data."),
        x_correlation_id=request.state.__getattr__('x-correlation-id')
    )

    try:
        customer_security_info_data = customer_security_info[0]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="Something went wrong with trying to find the customer's security information.")

    customer_subscription_results = request_handler.post(
        url=f"{config.LB_SERVICE_REGISTRY_API_CORE}/customersubscription/search?sort_by=created_on.desc",
        data=json.dumps({"customer_id": customer_data['id']
                        }),
        raise_exception=HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED,
                                      detail=f"There was a problem retrieving the customer subscription data. Please try again."),
        x_correlation_id=request.state.__getattr__('x-correlation-id')
    )

    try:
        customer_subscription_data = customer_subscription_results[0]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="Something went wrong with trying to find the customer's subscription information.")


    connection_string = "postgresql://{username}:{password}@{host}/{db_name}".format(
        username=customer_security_info_data['db_username'],
        password=customer_security_info_data['db_password'],
        host=customer_security_info_data['db_host'],
        db_name=customer_security_info_data['database_name'])

    payload = {
        "user_id": user_id,
        "expires": time.time() + 86400,  # 24hrs
        "customer_id": customer_data['id'],
        "customer_subdomain": customer_data['subdomain'],
        "customer_database_connection": connection_string
    }
    token = jwt.encode(payload, config.CUSTOMER_AUTH_JWT_SECRET, algorithm=config.CUSTOMER_AUTH_JWT_ALGORITHM)

    return {
        "access_token": token.decode('utf-8'),
        "user_id": user_id,
        "customer_id": customer_data['id'],
        "customer_subscription_plan_id": customer_subscription_data['subscription_plan_id'],
        "customer_subscription_end_on": customer_subscription_data['end_on'],
        "customer_subscription_trial": customer_subscription_data['trial']

    }
