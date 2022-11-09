from schemas.base import SchemasBase


class Account(SchemasBase):
    name: str
    password: str