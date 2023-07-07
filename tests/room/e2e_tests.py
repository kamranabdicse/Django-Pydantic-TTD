import json
import pytest
import logging
from ninja import testing
from reservation_system.models import Room, Listing, Owner
from reservation_system.api.api_v1.controllers.room import router


logger = logging.getLogger(__name__)

pytestmark = [
    pytest.mark.django_db(databases=["default"]),
    pytest.mark.e2e,
    pytest.mark.room,
]


class TestRoomEndpoints:
    def test_create_room(self, listing, owner):
        client = testing.TestClient(router)
        # listing_id = Listing.objects.create(
        #     name="test", address="test2", description="test"
        # ).id
        # owner_id = Owner.objects.create(name="test", address="test2").id

        payload = {
            "listing_id": listing.id,
            "owner_id": owner.id,
            "number": 1,
            "name": "VIP",
            "price": 100,
        }

        # Send a POST request to the create_room endpoint
        response = client.post("/create", json.dumps(payload))

        # Assert the response status code
        assert response.status_code == 201

        # Parse the response JSON
        result = response.json()

        # Assert the expected fields in the response
        assert "id" in result
        assert result["listing_id"] == listing.id
        assert result["owner_id"] == owner.id
        assert result["number"] == payload["number"]
        assert result["name"] == payload["name"]
        assert result["price"] == payload["price"]

    def test_retrieve_room_does_not_exist(self):
        client = testing.TestClient(router)

        room_id = 102

        response = client.get(f"/{room_id}")

        assert response.status_code == 404

    def test_retrieve_room_exist(self, listing, owner):
        client = testing.TestClient(router)

        room_id = Room.objects.create(
            number=1, name="test2", price=100, listing=listing, owner=owner
        ).id

        response = client.get(f"/{room_id}")

        assert response.status_code == 200
        assert response.json() == {
            "id": room_id,
            "number": 1,
            "name": "test2",
            "price": 100,
            "listing_id": listing.id,
            "owner_id": owner.id,
        }

    def test_put_room_does_not_exist(self):
        client = testing.TestClient(router)

        room_id = 102
        payload = {
            "number": 1,
            "name": "test2",
            "price": 100,
        }

        response = client.put(f"/{room_id}", json.dumps(payload))

        assert response.status_code == 404

    def test_put_room_exist_with_missing_value(self, listing, owner):
        client = testing.TestClient(router)

        room_id = Room.objects.create(
            number=1, name="test2", price=100, listing=listing, owner=owner
        ).id

        payload = {
            "number": 1,
            "name": "test2",
            "price": 100,
        }

        response = client.put(f"/{room_id}", json.dumps(payload))

        assert response.status_code == 422

    def test_put_room_exist(self, listing, owner):
        client = testing.TestClient(router)

        room_id = Room.objects.create(
            number=1, name="test2", price=100, listing=listing, owner=owner
        ).id

        payload = {
            "number": 1,
            "name": "test2",
            "price": 100,
        }

        response = client.put(f"/{room_id}", json.dumps(payload))

        assert response.status_code == 200

    def test_patch_room_does_not_exist(self):
        client = testing.TestClient(router)

        room_id = 102
        payload = {
            "name": "Test room",
            "address": "Test Address",
        }

        response = client.patch(f"/{room_id}", json.dumps(payload))

        assert response.status_code == 404

    def test_patch_room_exist_with_missing_value(self, listing, owner):
        client = testing.TestClient(router)

        room_id = Room.objects.create(
            number=1, name="test2", price=100, listing=listing, owner=owner
        ).id

        payload = {"name": 123}

        response = client.patch(f"/{room_id}", json.dumps(payload))

        assert response.status_code == 200

    def test_patch_room_exist(self, listing, owner):
        client = testing.TestClient(router)

        room_id = Room.objects.create(
            number=1, name="test2", price=100, listing=listing, owner=owner
        ).id

        payload = {
            "name": "Test room",
            "address": "Test Address",
            "description": "Test Description",
        }

        response = client.patch(f"/{room_id}", json.dumps(payload))

        assert response.status_code == 200

    def test_delete_room_does_not_exist(self):
        client = testing.TestClient(router)

        room_id = 102

        response = client.delete(f"/{room_id}")

        assert response.status_code == 404

    def test_delete_room_exist(self, listing, owner):
        client = testing.TestClient(router)

        room_id = Room.objects.create(
            number=1, name="test2", price=100, listing=listing, owner=owner
        ).id

        response = client.delete(f"/{room_id}")

        assert response.status_code == 204
