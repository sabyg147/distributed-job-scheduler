from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database import get_db
from app.job.schemas import JobCreate, JobResponse
from app.models.job import Job
from app.models.queue import Queue
from app.models.retry_policy import RetryPolicy

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.post(
    "/",
    response_model=JobResponse,
)
def create_job(
    request: JobCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    queue = (
        db.query(Queue)
        .filter(Queue.id == request.queue_id)
        .first()
    )

    if queue is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Queue not found",
        )

    if request.retry_policy_id:

        retry_policy = (
            db.query(RetryPolicy)
            .filter(
                RetryPolicy.id == request.retry_policy_id
            )
            .first()
        )

        if retry_policy is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Retry policy not found",
            )

    job = Job(
        name=request.name,
        description=request.description,
        payload=request.payload,
        priority=request.priority,
        max_retries=request.max_retries,
        is_recurring=request.is_recurring,
        cron_expression=request.cron_expression,
        scheduled_at=request.scheduled_at,
        queue_id=request.queue_id,
        retry_policy_id=request.retry_policy_id,
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


@router.get(
    "/",
    response_model=list[JobResponse],
)
def get_jobs(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return (
        db.query(Job)
        .order_by(Job.created_at.desc())
        .all()
    )


@router.get(
    "/{job_id}",
    response_model=JobResponse,
)
def get_job(
    job_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )

    return job