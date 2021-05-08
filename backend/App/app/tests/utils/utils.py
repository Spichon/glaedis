import random
import string
from random import randint

def random_lower_string(k: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=k))

def random_integer() -> int:
    return randint(0, 99999999)

def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"
