from models.base import BaseModel
from peewee import CharField


class Account(BaseModel):
    name = CharField()
    password = CharField()

    class Meta:
        db_table = 'account'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)