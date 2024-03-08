import azure.functions as func
import datetime
import json
import logging
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
app = func.FunctionApp()

# Connect to database
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    return conn


@app.route(route="login", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def login(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        email = req_body["email"]
        password = req_body["password"]
        logging.info(f"Request: {email} {password}")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s AND password = %s", (email, password))
        count = cursor.fetchone()[0]

        conn.commit()
        cursor.close()
        conn.close()
        if count > 0:
            return func.HttpResponse(
                f"You submitted this information to login: {email} {password}",
                status_code=200,
            )
        else:
            return func.HttpResponse(
                "Invalid email or password",
                status_code=401,
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

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (user_email, password) VALUES (%s, %s)",
            (
                email,
                password
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        return func.HttpResponse(
            f"You submitted this information to register: {email} {password}",
            status_code=200,
        )
    except Exception as e:
        logging.error(f"Error processing register request: {str(e)}")
        return func.HttpResponse("Error processing register request", status_code=400)
