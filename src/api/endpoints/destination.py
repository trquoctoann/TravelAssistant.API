from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends

from config.container import Container
from config.middleware import inject
from schema.base_schema import Blank
from schema.destination_schema import Destination, FindDestination, UpsertDestination, FindDestinationResult
from service.destination_service import DestinationService

router = APIRouter(
    prefix="/destinations",
    tags=["destinations"],
)


@router.get("", response_model=FindDestinationResult)
@inject
def get_destination_list(
    find_query: FindDestination = Depends(),
    service: DestinationService = Depends(Provide[Container.destination_service]),
):
    return service.get_list(find_query)


@router.get("/{destination_id}", response_model=Destination)
@inject
def get_destination(
    destination_id: int,
    service: DestinationService = Depends(Provide[Container.destination_service]),
):
    return service.get_by_id(destination_id)


@router.post("", response_model=Destination)
@inject
def create_destination(
    destination: UpsertDestination,
    service: DestinationService = Depends(Provide[Container.destination_service]),
):
    return service.add(destination)


@router.patch("/{destination_id}", response_model=Destination)
@inject
def update_destination(
    destination_id: int,
    destination: UpsertDestination,
    service: DestinationService = Depends(Provide[Container.destination_service]),
):
    return service.patch(destination_id, destination)


@router.delete("/{destination_id}", response_model=Blank)
@inject
def delete_destination(
    destination_id: int,
    service: DestinationService = Depends(Provide[Container.destination_service]),
):
    service.remove_by_id(destination_id)
    return Blank()
