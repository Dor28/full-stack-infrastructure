import os

import dotenv
dotenv.load_dotenv()

error_responses = {
    400: {
        "description": "Bad request",
        "content": {
            "application/json": {
                "example": {"detail": "Error --> {code} {function_name} params [params]; {hint detail}"}
            }
        }
    }
}

# JWT

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

service_base_url = os.getenv('SERVICE1_URL')