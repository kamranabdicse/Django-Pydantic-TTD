import json
import pytest
import logging
from ninja import testing
from django.http import Http404
from reservation_system.exceptions.exceptions import ListingObjectDoesNotExist
from reservation_system.models import Listing
from reservation_system.api.api_v1.controllers.listing import router

logger = logging.getLogger(__name__)

pytestmark = [
    pytest.mark.django_db(databases=["default"]),
    pytest.mark.e2e,
    pytest.mark.listing,
]


class TestListingEndpoints:
    def test_create_listing(self):
        client = testing.TestClient(router)

        payload = {
            "owner": "string",
            "name": "Test Listing",
            "address": "Test Address",
            "description": "Test Description",
        }

        # Send a POST request to the create_listing endpoint
        response = client.post("/create", json.dumps(payload))

        # Assert the response status code
        assert response.status_code == 201

        # Parse the response JSON
        result = response.json()

        # Assert the expected fields in the response
        assert "id" in result
        assert result["name"] == payload["name"]
        assert result["address"] == payload["address"]
        assert result["description"] == payload["description"]

    def test_retrieve_listing_does_not_exist(self):
        client = testing.TestClient(router)

        listing_id = 102

        response = client.get(f"/{listing_id}")

        assert response.status_code == 404

    def test_retrieve_listing_exist(self):
        client = testing.TestClient(router)

        listing_id = Listing.objects.create(
            owner="test", name="test", address="test2", description="test"
        ).id

        response = client.get(f"/{listing_id}")

        assert response.status_code == 200
        assert response.json() == {
            "id": listing_id,
            "owner": "test",
            "name": "test",
            "address": "test2",
            "description": "test",
        }

    def test_put_listing_does_not_exist(self):
        client = testing.TestClient(router)

        listing_id = 102
        payload = {
            "owner": "string",
            "name": "Test Listing",
            "address": "Test Address",
            "description": "Test Description",
        }

        response = client.put(f"/{listing_id}", json.dumps(payload))

        assert response.status_code == 404

    def test_put_listing_exist_with_missing_value(self):
        client = testing.TestClient(router)

        listing_id = Listing.objects.create(
            owner="test", name="test", address="test2", description="test"
        ).id

        payload = {
            "owner": "string",
            "name": "Test Listing",
            "address": "Test Address",
        }

        response = client.put(f"/{listing_id}", json.dumps(payload))

        assert response.status_code == 422

    def test_put_listing_exist(self):
        client = testing.TestClient(router)

        listing_id = Listing.objects.create(
            owner="test", name="test", address="test2", description="test"
        ).id

        payload = {
            "owner": "string",
            "name": "Test Listing",
            "address": "Test Address",
            "description": "Test Description",
        }

        response = client.put(f"/{listing_id}", json.dumps(payload))

        assert response.status_code == 200

    def test_patch_listing_does_not_exist(self):
        client = testing.TestClient(router)

        listing_id = 102
        payload = {
            "owner": "string",
            "name": "Test Listing",
            "address": "Test Address",
        }

        response = client.patch(f"/{listing_id}", json.dumps(payload))

        assert response.status_code == 404

    def test_patch_listing_exist_with_missing_value(self):
        client = testing.TestClient(router)

        listing_id = Listing.objects.create(
            owner="test", name="test", address="test2", description="test"
        ).id

        payload = {"owner": "string", "name": 123}

        response = client.patch(f"/{listing_id}", json.dumps(payload))

        assert response.status_code == 200

    def test_patch_listing_exist(self):
        client = testing.TestClient(router)

        listing_id = Listing.objects.create(
            owner="test", name="test", address="test2", description="test"
        ).id

        payload = {
            "owner": "string",
            "name": "Test Listing",
            "address": "Test Address",
            "description": "Test Description",
        }

        response = client.patch(f"/{listing_id}", json.dumps(payload))

        assert response.status_code == 200

    def test_delete_listing_does_not_exist(self):
        client = testing.TestClient(router)

        listing_id = 102

        response = client.delete(f"/{listing_id}")

        assert response.status_code == 404

    def test_delete_listing_exist(self):
        client = testing.TestClient(router)

        listing_id = Listing.objects.create(
            owner="test", name="test", address="test2", description="test"
        ).id

        response = client.delete(f"/{listing_id}")

        assert response.status_code == 204
