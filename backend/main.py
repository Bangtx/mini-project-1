from fastapi import FastAPI
from config import db
import schemas.account as schemas_account

app = FastAPI()


@app.on_event('startup')
def startup():
    if db.is_closed():
        db.connect()


@app.on_event('shutdown')
def startup():
    if not db.is_closed():
        db.close()


@app.post('/')
def create_account(account: schemas_account.Account):
    from models.account import Account
    account = account.dict()
    return Account.create(**account)



@app.get('/')
def test():
    from models.account import Account
    return Account.get_list()

