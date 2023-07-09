from django.utils.translation import gettext_lazy as _

from ninja_extra.exceptions import APIException
from ninja_extra import status


class ListingObjectDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Listing object does not exist"


class OwnerObjectDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Owner object does not exist"


class RoomObjectDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Room object does not exist"


class ReservationObjectExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Reservation object exist in your choosing time"
