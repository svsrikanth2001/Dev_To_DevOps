from fastapi import APIRouter
from typing import List
from fastapi import status,Depends, Response
from sqlalchemy.orm import Session

from app.models.skillslist import SkillsListCreateModel
from app.models.skillslist import SkillsListReadModel
from app.models.skillslist import SkillsListUpdateModel
from app.models.skillslist import SkillsListDeleteModel
from app.models.skillslist import SkillsListSearchModel

from app.database.models.skillslist import SkillsListModel
from app.database.connection import get_db
from app.database.crud.skillslist import SkillsCrud 

router_tag = "SkilsList"  # groups api routes within Swagger
router_prefix = "/"+router_tag.lower().replace(" ", "")
router = APIRouter(prefix=router_prefix)


@router.post("/search", response_model=List[SkillsListReadModel], tags=[router_tag])
def search(Applicant: SkillsListSearchModel , db: Session = Depends(get_db)):
    crud = SkillsCrud(db_session=db, db_model=SkillsListModel)
    records = crud.get_by_args(model_object_fields=Applicant)
    return records


@router.post("/create", response_model=SkillsListReadModel, tags=[router_tag])
def create(Applicant: SkillsListCreateModel, db: Session = Depends(get_db)):
    crud = SkillsCrud(db_session=db, db_model=SkillsListModel)
    record = crud.create(input_model_object=Applicant)
    return record


@router.post("/{id:int}", response_model=SkillsListReadModel, tags=[router_tag])
def update(Applicant: SkillsListUpdateModel, id: int, db: Session = Depends(get_db)):
    crud = SkillsCrud(db_session=db, db_model=SkillsListModel)
    record = crud.update(update_model_object=Applicant, id=id)
    return record


@router.get("/{id:int}", response_model=SkillsListReadModel, tags=[router_tag])
def get_by_id(id: int, db: Session = Depends(get_db)):
    crud = SkillsCrud(db_session=db, db_model=SkillsListModel)
    record = crud.get(object_id=id)
    if record:
        return record
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{id:int}", tags=[router_tag])
def delete(id: int, db: Session = Depends(get_db)):
    crud = SkillsCrud(db_session=db, db_model=SkillsListModel)
    result = crud.delete(object_id=id)
    if result:
        return Response(status_code=status.HTTP_200_OK)
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
