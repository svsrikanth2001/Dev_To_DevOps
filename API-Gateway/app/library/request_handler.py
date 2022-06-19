import requests
from typing import Dict, AnyStr, Union
from fastapi import HTTPException
import json
import backoff
from app.commonlib.configuration_handler import ConfigurationHandler

config = ConfigurationHandler()

@backoff.on_exception(backoff.expo, (RuntimeError, HTTPException), max_time=3)
def post(url: AnyStr, data: str, raise_exception: Union[RuntimeError, HTTPException],
         headers: Dict = None, x_correlation_id: str = None) -> json:
    if not headers:
        headers = {
                    'Content-Type': 'application/json',
                   'accept': 'application/json',
                   'x-token': config.INTERNAL_API_TOKEN
                   }

    if x_correlation_id:
        headers['x-correlation-id'] = x_correlation_id

    response = requests.post(url=url,
                             headers=headers,
                             data=data,
                             verify=False)

    if response.status_code >= 400:
        if type(raise_exception) is HTTPException:
            try:
                response_json = response.json()

                msg = ""
                if response_json.get('message'):
                    msg += response_json.get('message')
                if response_json.get('detail'):
                    msg += str(response_json.get('detail'))

                raise_exception.detail = raise_exception.detail + " " + msg

            except json.JSONDecodeError:
                pass

        raise raise_exception

    response_json = response.json()

    return response_json



@backoff.on_exception(backoff.expo, (RuntimeError, HTTPException), max_time=3)
def get(url: AnyStr, raise_exception: Union[RuntimeError, HTTPException],
         headers: Dict = None, x_correlation_id: str = None) -> json:
    if not headers:
        headers = {'Content-Type': 'application/json',
                   'accept': 'application/json',
                   'x-token': config.INTERNAL_API_TOKEN}

    if x_correlation_id:
        headers['x-correlation-id'] = x_correlation_id

    response = requests.get(url=url,
                             headers=headers,
                             verify=False)

    if response.status_code >= 400:
        if type(raise_exception) is HTTPException:
            try:
                response_json = response.json()

                msg = ""
                if response_json.get('message'):
                    msg += response_json.get('message')
                if response_json.get('detail'):
                    msg += str(response_json.get('detail'))

                raise_exception.detail = raise_exception.detail + " " + msg

            except json.JSONDecodeError:
                pass

        raise raise_exception

    response_json = response.json()

    return response_json

@backoff.on_exception(backoff.expo, (RuntimeError, HTTPException), max_time=3)
def delete(url: AnyStr, raise_exception: Union[RuntimeError, HTTPException],
           headers: Dict = None, x_correlation_id: str = None) -> json:
    if not headers:
        headers = {'Content-Type': 'application/json',
                   'accept': 'application/json',
                   'x-token': config.INTERNAL_API_TOKEN}

    if x_correlation_id:
        headers['x-correlation-id'] = x_correlation_id

    response = requests.delete(url=url,
                               headers=headers,
                               verify=False)

    if response.status_code >= 400:
        if type(raise_exception) is HTTPException:
            try:
                response_json = response.json()
                raise_exception.detail = raise_exception.detail + " " + response_json.get('message')

            except json.JSONDecodeError:
                pass

        raise raise_exception

    return response.status_code
