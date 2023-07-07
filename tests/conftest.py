import pytest
from reservation_system.models import Room, Listing, Owner


@pytest.fixture
def listing():
    return Listing.objects.create(
        name="Listing 1", address="Address 1", description="Description 1"
    )


@pytest.fixture
def owner():
    return Owner.objects.create(
        name='Owner 1', address='Owner Address 1'
    )