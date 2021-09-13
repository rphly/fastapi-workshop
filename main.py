from typing import Optional
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from routers import routers


def create_app():
    app = FastAPI()  # docs_url=None, redoc_url=None
    setup_routers(app)
    return app


def setup_routers(app):
    for router in routers:
        app.include_router(router, prefix="/api")


app = create_app()


@app.middleware("http")
async def attach_user_object(request: Request, call_next):
    headers = request.headers
    request.state.user = None
    if "Authorization" in headers:
        auth_header = headers.get("Authorization", None)
        request.state.user = get_user_by_auth(auth_header)
    response = await call_next(request)
    return response


def get_user_by_auth(header):
    # mock auth
    ok = header.split(" ")[1] == 123
    return {"id": 1, "first_name": "Tom", "last_name": "Petty"}, ok


@app.get("/")
def read_root():
    return {"Hello": "World"}
