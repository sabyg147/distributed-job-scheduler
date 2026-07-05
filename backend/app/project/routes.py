from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database import get_db
from app.models.organization import Organization
from app.models.project import Project
from app.project.schemas import (
    ProjectCreate,
    ProjectResponse,
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post(
    "/",
    response_model=ProjectResponse,
)
def create_project(
    request: ProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    organization = (
        db.query(Organization)
        .filter(Organization.id == request.organization_id)
        .first()
    )

    if organization is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )

    existing = (
        db.query(Project)
        .filter(
            Project.name == request.name,
            Project.organization_id == request.organization_id,
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Project already exists",
        )

    project = Project(
        name=request.name,
        description=request.description,
        organization_id=request.organization_id,
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


@router.get(
    "/",
    response_model=list[ProjectResponse],
)
def get_projects(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return db.query(Project).all()