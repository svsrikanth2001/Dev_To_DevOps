from app.database.connection import Base

from sqlalchemy.orm import Session
from app.database.crud._base_crud import BaseCrud


class ApplicantSkillsCrud(BaseCrud):

    def __init__(self, db_session: Session, db_model: Base):
        super().__init__(db_session, db_model)
        self._db = db_session
