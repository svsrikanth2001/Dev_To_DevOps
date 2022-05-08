from fastapi import APIRouter
from typing import List
from fastapi import status,Depends, Response
from sqlalchemy.orm import Session

from app.models.applicantskills import ApplicantSkillsCreateModel
from app.models.applicantskills import ApplicantSkillsReadModel
from app.models.applicantskills import ApplicantSkillsUpdateModel
from app.models.applicantskills import ApplicantSkillsDeleteModel
from app.models.applicantskills import ApplicantSkillsSearchModel

from app.database.models.applicantskills import ApplicantSkillsModel
from app.database.connection import get_db
from app.database.crud.applicant import ApplicantCrud

router_tag = "ApplicantSkills"  # groups api routes within Swagger
router_prefix = "/"+router_tag.lower().replace(" ", "")
router = APIRouter(prefix=router_prefix)


@router.post("/search", response_model=List[ApplicantSkillsReadModel], tags=[router_tag])
def search(ApplicantSkills: ApplicantSkillsSearchModel , db: Session = Depends(get_db)):
    crud = ApplicantSkillsCrud(db_session=db, db_model=ApplicantSkillsModel)
    records = crud.get_by_args(model_object_fields=ApplicantSkills)
    return records


@router.post("/create", response_model=ApplicantSkillsReadModel, tags=[router_tag])
def create(ApplicantSkills: ApplicantSkillsCreateModel, db: Session = Depends(get_db)):
    crud = ApplicantSkillsCrud(db_session=db, db_model=ApplicantSkillsModel)
    record = crud.create(input_model_object=ApplicantSkills)
    return record


@router.post("/{id:int}", response_model=ApplicantSkillsReadModel, tags=[router_tag])
def update(ApplicantSkills: ApplicantSkillsUpdateModel, id: int, db: Session = Depends(get_db)):
    crud = ApplicantSkillsCrud(db_session=db, db_model=ApplicantSkillsModel)
    record = crud.update(update_model_object=ApplicantSkills, id=id)
    return record


@router.get("/{id:int}", response_model=ApplicantSkillsReadModel, tags=[router_tag])
def get_by_id(id: int, db: Session = Depends(get_db)):
    crud = ApplicantSkillsCrud(db_session=db, db_model=ApplicantSkillsModel)
    record = crud.get(object_id=id)
    if record:
        return record
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{id:int}", tags=[router_tag])
def delete(id: int, db: Session = Depends(get_db)):
    crud = ApplicantSkillsCrud(db_session=db, db_model=ApplicantSkillsModel)
    result = crud.delete(object_id=id)
    if result:
        return Response(status_code=status.HTTP_200_OK)
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
