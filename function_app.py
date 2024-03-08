import azure.functions as func
import datetime
import json
import logging
from urllib.parse import parse_qs


app = func.FunctionApp()

@app.route(route="login", auth_level=func.AuthLevel.ANONYMOUS)
def login(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body_bytes = req.get_body()
    req_body = req_body_bytes.decode("utf-8")
    logging.info(f"Request: {req_body}")

    email = parse_qs(req_body)["email"]
    password = parse_qs(req_body)["password"]

    return func.HttpResponse(
        f"You submitted this information to login: {email} {password}",
        status_code=200,
    )
    
@app.route(route="register", auth_level=func.AuthLevel.ANONYMOUS)
def register(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body_bytes = req.get_body()
    req_body = req_body_bytes.decode("utf-8")
    logging.info(f"Request: {req_body}")

    email = parse_qs(req_body)["email"]
    password = parse_qs(req_body)["password"]

    return func.HttpResponse(
        f"You submitted this information to register: {email} {password}",
        status_code=200,
    )