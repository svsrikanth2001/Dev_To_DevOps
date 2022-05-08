from fastapi import APIRouter
from typing import List
from fastapi import status,Depends, Response
from sqlalchemy.orm import Session

from app.models.applicant import ApplicantCreateModel
from app.models.applicant import ApplicantReadModel
from app.models.applicant import ApplicantUpdateModel
from app.models.applicant import ApplicantDeleteModel
from app.models.applicant import ApplicantSearchModel

from app.database.models.applicant import ApplicantModel
from app.database.connection import get_db
from app.database.crud.applicant import ApplicantCrud

router_tag = "Applicant"  # groups api routes within Swagger
router_prefix = "/"+router_tag.lower().replace(" ", "")
router = APIRouter(prefix=router_prefix)


@router.post("/search", response_model=List[ApplicantReadModel], tags=[router_tag])
def search(Applicant: ApplicantSearchModel , db: Session = Depends(get_db)):
    crud = ApplicantCrud(db_session=db, db_model=ApplicantModel)
    records = crud.get_by_args(model_object_fields=Applicant)
    return records


@router.post("/create", response_model=ApplicantReadModel, tags=[router_tag])
def create(Applicant: ApplicantCreateModel, db: Session = Depends(get_db)):
    crud = ApplicantCrud(db_session=db, db_model=ApplicantModel)
    record = crud.create(input_model_object=Applicant)
    return record


@router.post("/{id:int}", response_model=ApplicantReadModel, tags=[router_tag])
def update(Applicant: ApplicantUpdateModel, id: int, db: Session = Depends(get_db)):
    crud = ApplicantCrud(db_session=db, db_model=ApplicantModel)
    record = crud.update(update_model_object=Applicant, id=id)
    return record


@router.get("/{id:int}", response_model=ApplicantReadModel, tags=[router_tag])
def get_by_id(id: int, db: Session = Depends(get_db)):
    crud = ApplicantCrud(db_session=db, db_model=ApplicantModel)
    record = crud.get(object_id=id)
    if record:
        return record
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{id:int}", tags=[router_tag])
def delete(id: int, db: Session = Depends(get_db)):
    crud = ApplicantCrud(db_session=db, db_model=ApplicantModel)
    result = crud.delete(object_id=id)
    if result:
        return Response(status_code=status.HTTP_200_OK)
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
