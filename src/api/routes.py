from fastapi import APIRouter

from api.endpoints.destination import router as destination_router

routers = APIRouter()
router_list = [destination_router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
