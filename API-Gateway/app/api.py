import traceback

from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import status, Body, Depends, Request, Response, HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import registration
from app.routers import authentication
from app.middleware.request_context_middleware import RequestContextMiddleware
from app.routers import execute



##########################################################################################
# API Configuration
##########################################################################################



prefix = "/api-gateway/web"
#config = ConfigurationHandler()


app = FastAPI(title="FreshersOnly Web API Gateway",
              openapi_url=f"{prefix}/openapi.json",
              docs_url=f"{prefix}"
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.add_middleware(RequestContextMiddleware)


@app.route('/')
async def default_route(request):
    return HTMLResponse(f"Visit <a href=\"{prefix}\">{prefix}</a> to view API documenation.")


##########################################################################################
# API Routers
##########################################################################################

app.include_router(registration.router, prefix=f"{prefix}")
app.include_router(authentication.router, prefix=f"{prefix}")
app.include_router(execute.router, prefix=f"{prefix}")
