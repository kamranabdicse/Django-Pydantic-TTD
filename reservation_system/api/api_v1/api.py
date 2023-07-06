from ninja import NinjaAPI
from .controllers.listing import router as listing_router


api = NinjaAPI(version="1.0.0")
api.add_router("/v1/listing", listing_router)
