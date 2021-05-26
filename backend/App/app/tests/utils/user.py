from typing import Dict
import boto3
from botocore.exceptions import ClientError

from app.core.config import settings
from app.tests.utils.utils import random_email, random_lower_string
from app.schemas import User


def user_authentication_headers(email: str, password: str) -> Dict[str, str]:
    cidp = boto3.client('cognito-idp')
    response = cidp.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': email,
            'PASSWORD': password},
        ClientId=settings.COGNITO_USER_POOL_CLIENT_ID)
    headers = {"Authorization": f"Bearer {response['AuthenticationResult']['AccessToken']}"}
    return headers


def create_random_user(username: str = random_lower_string() + "@antispam.com",
                       password: str = random_lower_string()):
    cidp = boto3.client('cognito-idp')
    try:
        cidp.sign_up(
            ClientId=settings.COGNITO_USER_POOL_CLIENT_ID,
            Username=username,
            Password=password,
            UserAttributes=[{'Name': 'email',
                             'Value': username}])
        confirm_sign_up_response = cidp.admin_confirm_sign_up(
            UserPoolId=settings.COGNITO_USER_POOL_ID,
            Username=username)
    except ClientError as err:
        print(err)


def create_random_user_internal() -> User:
    return {"id": random_lower_string()}


def authentication_token_from_email(email: str) -> Dict[str, str]:
    """
    Return a valid token for the user with given email.

    If the user doesn't exist it is created first.
    """
    password = random_lower_string()
    create_random_user(username=email, password=password)

    return user_authentication_headers(email=email, password=password)
