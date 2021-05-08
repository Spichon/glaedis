from app.core.security import decode_secret_key
from app.tests.utils.user import create_random_user_internal
from sqlalchemy.orm import Session

from app import crud
from app.schemas.account import AccountCreate, AccountUpdate
from app.tests.utils.utils import random_lower_string
from app.tests.utils.broker import create_broker


def test_create_account_with_name_with_broker(db: Session) -> None:
    name = random_lower_string()
    api_key = random_lower_string(32)
    secret_key = random_lower_string(32)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(api_key=api_key,
                               name=name,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    assert account.owner_id == user['id']
    assert account.broker.name == broker.name
    assert account.name == name


def test_create_account_without_name_with_broker(db: Session) -> None:
    api_key = random_lower_string(32)
    secret_key = random_lower_string(32)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(api_key=api_key,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    assert account.owner_id == user['id']
    assert account.broker.name == broker.name
    assert account.name == None


def test_get_account_with_broker(db: Session) -> None:
    api_key = random_lower_string(32)
    name = random_lower_string()
    secret_key = random_lower_string(32)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(api_key=api_key,
                               name=name,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    stored_account = crud.account.get(db=db, id=account.id)
    assert stored_account
    assert account.id == stored_account.id


def test_delete_account_with_broker(db: Session) -> None:
    name = random_lower_string()
    api_key = random_lower_string(32)
    secret_key = random_lower_string(32)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(name=name,
                               api_key=api_key,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    account2 = crud.account.remove(db=db, id=account.id)
    account3 = crud.account.get(db=db, id=account.id)
    assert account3 is None
    assert account2.id == account.id
    assert account2.name == name


def test_update_account_with_name_with_broker(db: Session) -> None:
    name = random_lower_string()
    api_key = random_lower_string(32)
    secret_key = random_lower_string(32)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(api_key=api_key,
                               name=name,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    api_key_2 = random_lower_string(32)
    secret_key_2 = random_lower_string(32)
    name_2 = random_lower_string()
    account_in_2 = AccountUpdate(api_key=api_key_2,
                                 name=name_2,
                                 secret_key=secret_key_2)
    account_2 = crud.account.update(db=db, db_obj=account, obj_in=account_in_2)
    assert account_2.owner_id == user['id']
    assert account.broker.name == broker.name
    assert account_2.name == name_2
    assert account_2.api_key == api_key_2
    assert decode_secret_key(account_2.hashed_secret_key) == secret_key_2


def test_not_create_account_with_length_3_api_key(db: Session) -> None:
    name = random_lower_string()
    api_key = random_lower_string(3)
    secret_key = random_lower_string(4)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(api_key=api_key,
                               name=name,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    assert account is None


def test_not_create_account_with_length_3_secret_key(db: Session) -> None:
    name = random_lower_string()
    api_key = random_lower_string(4)
    secret_key = random_lower_string(3)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(api_key=api_key,
                               name=name,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    assert account is None


def test_create_account_with_length_4_secret_key_and_api_key(db: Session) -> None:
    name = random_lower_string()
    api_key = random_lower_string(4)
    secret_key = random_lower_string(4)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(api_key=api_key,
                               name=name,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    assert account.owner_id == user['id']
    assert account.broker.name == broker.name
    assert account.name == name


def test_not_create_account_with_length_5_api_key(db: Session) -> None:
    name = random_lower_string()
    api_key = random_lower_string(5)
    secret_key = random_lower_string(4)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(api_key=api_key,
                               name=name,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    assert account is None


def test_not_create_account_with_length_5_secret_key(db: Session) -> None:
    name = random_lower_string()
    api_key = random_lower_string(4)
    secret_key = random_lower_string(5)
    broker = create_broker(db)
    user = create_random_user_internal()
    account_in = AccountCreate(api_key=api_key,
                               name=name,
                               secret_key=secret_key,
                               broker_id=broker.id)
    account = crud.account.create_with_owner(db=db, obj_in=account_in, owner_id=user['id'])
    assert account is None
