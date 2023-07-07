from ninja import NinjaAPI
from .controllers.listing import router as listing_router
from .controllers.owner import router as owner_router
from .controllers.room import router as room_router

api = NinjaAPI(version="1.0.0")
api.add_router("/v1/listing", listing_router, tags=["listing"])
api.add_router("/v1/owner", owner_router, tags=["owner"])
api.add_router("/v1/room", room_router, tags=["room"])
