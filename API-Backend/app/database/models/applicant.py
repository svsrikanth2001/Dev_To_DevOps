from sqlalchemy import Boolean, Column, BigInteger,Integer, String, VARCHAR, TIMESTAMP,Text, BIGINT, SmallInteger,DATETIME
from app.database.connection import Base


class ApplicantModel(Base):
    __tablename__ = "applicant_login"

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(VARCHAR)
    password = Column(VARCHAR)
    firstname = Column(VARCHAR)
    lastname = Column(VARCHAR)
