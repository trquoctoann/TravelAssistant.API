from dependency_injector import containers, providers

from config.config import configs
from config.database import Database
from repository.destination_repository import DestinationRepository
from service.destination_service import DestinationService

DESTINATIONS_FILE_PATH = "data/destinations.xlsx"


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "api.endpoints.destination",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

    destination_repository = providers.Factory(DestinationRepository, session_factory=db.provided.session)

    destination_service = providers.Factory(DestinationService, destination_repository=destination_repository)
