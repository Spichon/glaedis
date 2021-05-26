from jose import jwt
from app.core.config import settings
import re

ALGORITHM = "HS256"


def encode_secret_key(secret_key: str, ) -> str:
    encoded_secret_key = jwt.encode({"secret_key": secret_key}, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_secret_key


def decode_secret_key(encoded_secret_key: {}, altchars: str = b'+/') -> str:
    decode_secret_key = jwt.decode(token=encoded_secret_key, key=settings.SECRET_KEY, algorithms=ALGORITHM)
    data = bytes(decode_secret_key['secret_key'], encoding='utf-8')
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'=' * (4 - missing_padding)
    return data.decode("utf-8")
