from app.repositories import auth_repository
from email_validator import validate_email, EmailNotValidError

def register_user(email: str, password: str):
    new_email = is_email_valid(email.lower())
    response = auth_repository.register_user(new_email, password)

    return response

def login_user(email: str, password: str):
    new_email = is_email_valid(email.lower())
    response = auth_repository.login_user(new_email, password)

    return response


def is_email_valid(email: str):
    try:
        result = validate_email(email)
        return result.normalized
    except EmailNotValidError as e:
        raise ValueError(e)
    