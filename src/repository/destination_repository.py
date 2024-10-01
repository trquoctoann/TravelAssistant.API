from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session
from model.destination import Destination
from repository.base_repository import BaseRepository


class DestinationRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Destination)
