from sqlalchemy import Boolean, Column, BigInteger,Integer, \
    String, VARCHAR, TIMESTAMP,Text, BIGINT, SmallInteger,DATETIME,ForeignKey,Numeric
from app.database.connection import Base


class ApplicantSkillsModel(Base):
    __tablename__ = "applicant_skills"
    id = Column(BigInteger, primary_key=True, index=True)
    applicant_login_id = Column(BigInteger,  ForeignKey("applicant_login.id"),nullable=False)
    skillid = Column(BigInteger)
    

