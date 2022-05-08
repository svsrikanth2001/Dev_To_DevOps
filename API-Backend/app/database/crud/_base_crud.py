
from sqlalchemy.orm import Session
from app.database.connection import Base
from pydantic import BaseModel


class BaseCrud:

    def __init__(self, db_session: Session, db_model: Base):
        self.__db_session = db_session
        self.__db_model = db_model

    def create(self, input_model_object: BaseModel):
        db_item = self.__db_model(**input_model_object.dict())
        self.__db_session.add(db_item)
        self.__db_session.commit()
        return db_item

    def get_by_args(self, model_object_fields: BaseModel):
        query_arguments = model_object_fields.dict()
        for key, value in query_arguments.copy().items():
            if value is None:
                del query_arguments[key]
        results = self.__db_session.query(self.__db_model).filter_by(**query_arguments).all()

        return results

    def update(self, update_model_object: BaseModel, id: int):
        db_item = self.__db_session.query(self.__db_model).filter(self.__db_model.id == id).first()
        for key, value in update_model_object.dict().items():
            setattr(db_item, key, value)

        self.__db_session.add(db_item)
        self.__db_session.commit()
        return db_item

    def delete(self, object_id: int):
        db_item = self.__db_session.query(self.__db_model).filter(self.__db_model.id == object_id).first()
        if db_item:
            self.__db_session.delete(db_item)
            self.__db_session.commit()
            return True
        else:
            return None

    def get(self, object_id: int):
        return self.__db_session.query(self.__db_model).filter(self.__db_model.id == object_id).first()
