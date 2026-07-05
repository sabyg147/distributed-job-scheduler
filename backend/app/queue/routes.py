from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database import get_db
from app.models.project import Project
from app.models.queue import Queue
from app.queue.schemas import QueueCreate, QueueResponse

router = APIRouter(
    prefix="/queues",
    tags=["Queues"],
)


@router.post(
    "/",
    response_model=QueueResponse,
)
def create_queue(
    request: QueueCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    project = (
        db.query(Project)
        .filter(Project.id == request.project_id)
        .first()
    )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    existing = (
        db.query(Queue)
        .filter(
            Queue.name == request.name,
            Queue.project_id == request.project_id,
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Queue already exists",
        )

    queue = Queue(
        name=request.name,
        description=request.description,
        priority=request.priority,
        concurrency_limit=request.concurrency_limit,
        max_retries=request.max_retries,
        project_id=request.project_id,
    )

    db.add(queue)
    db.commit()
    db.refresh(queue)

    return queue


@router.get(
    "/",
    response_model=list[QueueResponse],
)
def get_queues(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return db.query(Queue).all()