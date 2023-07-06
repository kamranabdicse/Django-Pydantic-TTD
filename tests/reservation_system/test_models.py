import pytest

from reservation_system.models import Listing


pytestmark = [
    pytest.mark.django_db(databases=["default"]),
    pytest.mark.model,
]


class TestListingModel:
    """test `User` methods and managers"""

    def test_listing_model(self):
        listing = Listing.objects.create(
            owner="test", name="test", address="test2", description="test"
        )
        assert listing != None
