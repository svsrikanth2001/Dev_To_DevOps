
from sqlalchemy.orm import Session
from app.database.connection import Base
from pydantic import BaseModel


class Postgres:

    def __init__(self, db_session: Session):
        self.__db_session = db_session

    def execute_sql_cmd(self, sqlcommand ):
        return self.__db_session.execute(sqlcommand)


