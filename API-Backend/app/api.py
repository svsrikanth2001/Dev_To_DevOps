from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import status, Body, Depends, Request, Response
import traceback

from fastapi import FastAPI
from app.library.configuration_handler import ConfigurationHandler

from app.routers import applicant
from app.routers import applicant_skills
from app.routers import  skillslist


##########################################################################################
# API Configuration
##########################################################################################

config = ConfigurationHandler()


prefix = "/api/backend"

app = FastAPI(title="Freshersonly API v1.0",
              openapi_url=f"{prefix}/openapi.json",
              docs_url=f"{prefix}")


@app.route('/')
async def default_route(request):
    return HTMLResponse(f"Visit <a href=\"{prefix}\">{prefix}</a> to view API documenation.")


##########################################################################################
# Exception Handers
##########################################################################################

@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    error = str(exc)

    trace = "".join(
        traceback.format_exception(
            etype=type(exc), value=exc, tb=exc.__traceback__
        ))

    print(trace)

    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content={"message": "An error was encountered while processing the request.",
                                 "error": error,
                                 "traceback": trace})


##########################################################################################
# API Routers
##########################################################################################





app.include_router(applicant.router,prefix=f"{prefix}")
app.include_router(applicant_skills.router,prefix=f"{prefix}")
app.include_router(skillslist.router,prefix=f"{prefix}")
    



