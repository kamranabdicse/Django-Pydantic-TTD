
from django.utils.translation import gettext_lazy as _

from ninja_extra.exceptions import APIException
from ninja_extra import status


class ListingObjectDoesNotExist(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Listing object does not exist"