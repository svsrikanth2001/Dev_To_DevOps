from sqlalchemy import Boolean, Column, BigInteger,Integer, String, VARCHAR, TIMESTAMP,Text,BIGINT, SmallInteger,DATETIME,ForeignKey
from app.database.connection import Base


class SkillsListModel(Base):
    __tablename__ = "skillslist"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(VARCHAR)



