import azure.functions as func
import logging

@app.route(route="login", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def login(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        email = req_body["email"]
        password = req_body["password"]
        logging.info(f"Request: {email} {password}")
        
        return func.HttpResponse(
            f"You submitted this information to login: {email} {password}",
            status_code=200,
        )
    except Exception as e:
        logging.error(f"Error processing login request: {str(e)}")
        return func.HttpResponse("Error processing login request", status_code=400)

@app.route(route="register", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def register(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        email = req_body["email"]
        password = req_body["password"]
        logging.info(f"Request: {email} {password}")
        
        return func.HttpResponse(
            f"You submitted this information to register: {email} {password}",
            status_code=200,
        )
    except Exception as e:
        logging.error(f"Error processing register request: {str(e)}")
        return func.HttpResponse("Error processing register request", status_code=400)
