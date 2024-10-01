from repository.destination_repository import DestinationRepository
from service.base_service import BaseService


class DestinationService(BaseService):
    def __init__(self, destination_repository: DestinationRepository):
        self.destination_repository = destination_repository
        super().__init__(destination_repository)
