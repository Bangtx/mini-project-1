from peewee import Model
from config import db


class BaseModel(Model):
    pass

    class Meta:
        database = db
