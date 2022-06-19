
import uuid
from contextvars import ContextVar
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request


class RequestContextMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):

        request_id = str(uuid.uuid4())
        request.state.__setattr__('x-request-id', request_id)

        if request.headers.get('x-correlation-id'):
            correlation_id = request.headers.get('x-correlation-id')
        else:
            correlation_id = str(uuid.uuid4())

        request.state.__setattr__('x-correlation-id', correlation_id)

        response = await call_next(request)
        response.headers['x-correlation-id'] = correlation_id
        response.headers['x-request-id'] = request_id

        return response
