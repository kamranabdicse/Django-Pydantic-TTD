from ninja import NinjaAPI
from .controllers.listing import router as listing_router
from .controllers.owner import router as owner_router
from .controllers.room import router as room_router
from .controllers.reservation import router as reservation_router

api = NinjaAPI(version="1.0.0", title="Reservation System")
api.add_router("/v1/listing", listing_router, tags=["listing"])
api.add_router("/v1/owner", owner_router, tags=["owner"])
api.add_router("/v1/room", room_router, tags=["room"])
api.add_router("/v1/reservation", reservation_router, tags=["reservation"])
