from sqlalchemy import select
from sqlalchemy.orm import Session

from models.base import get_engine
from models.models import Status


def list_statutes() -> list[dict]:
    with Session(get_engine()) as session:
        statutes = session.scalars(select(Status).order_by(Status.name))
        return [
            {"id": status.id, "code": status.code, "name": status.name}
            for status in statutes
        ]