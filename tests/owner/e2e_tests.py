import json
import pytest
import logging
from ninja import testing
from django.http import Http404

from reservation_system.models import Owner
from reservation_system.api.api_v1.controllers.owner import router

logger = logging.getLogger(__name__)

pytestmark = [
    pytest.mark.django_db(databases=["default"]),
    pytest.mark.e2e,
    pytest.mark.owner,
]


class TestOwnerEndpoints:
    def test_create_Owner(self):
        client = testing.TestClient(router)

        payload = {"name": "Test Owner", "address": "Test Address"}

        response = client.post("/create", json.dumps(payload))

        # Assert the response status code
        assert response.status_code == 201

        # Parse the response JSON
        result = response.json()

        # Assert the expected fields in the response
        assert "id" in result
        assert result["name"] == payload["name"]
        assert result["address"] == payload["address"]

    def test_retrieve_Owner_does_not_exist(self):
        client = testing.TestClient(router)

        owner_id = 102

        response = client.get(f"/{owner_id}")

        assert response.status_code == 404

    def test_retrieve_owner_exist(self):
        client = testing.TestClient(router)

        owner_id = Owner.objects.create(name="test", address="test2").id

        response = client.get(f"/{owner_id}")

        assert response.status_code == 200
        assert response.json() == {
            "id": owner_id,
            "name": "test",
            "address": "test2",
        }

    def test_put_owner_does_not_exist(self):
        client = testing.TestClient(router)

        owner_id = 102
        payload = {
            "name": "Test Owner",
            "address": "Test Address",
        }

        response = client.put(f"/{owner_id}", json.dumps(payload))

        assert response.status_code == 404

    def test_put_owner_exist_with_missing_value(self):
        client = testing.TestClient(router)

        owner_id = Owner.objects.create(name="test", address="test2").id

        payload = {
            "address": "Test Address",
        }

        response = client.put(f"/{owner_id}", json.dumps(payload))

        assert response.status_code == 422

    def test_put_owner_exist(self):
        client = testing.TestClient(router)

        owner_id = Owner.objects.create(name="test", address="test2").id

        payload = {
            "owner": "string",
            "name": "Test Owner",
            "address": "Test Address",
            "description": "Test Description",
        }

        response = client.put(f"/{owner_id}", json.dumps(payload))

        assert response.status_code == 200

    def test_patch_owner_does_not_exist(self):
        client = testing.TestClient(router)

        owner_id = 102
        payload = {
            "owner": "string",
            "name": "Test Owner",
            "address": "Test Address",
        }

        response = client.patch(f"/{owner_id}", json.dumps(payload))

        assert response.status_code == 404

    def test_patch_owner_exist_with_missing_value(self):
        client = testing.TestClient(router)

        owner_id = Owner.objects.create(name="test", address="test2").id

        payload = {"owner": "string", "name": 123}

        response = client.patch(f"/{owner_id}", json.dumps(payload))

        assert response.status_code == 200

    def test_patch_owner_exist(self):
        client = testing.TestClient(router)

        owner_id = Owner.objects.create(name="test", address="test2").id

        payload = {
            "owner": "string",
            "name": "Test Owner",
            "address": "Test Address",
            "description": "Test Description",
        }

        response = client.patch(f"/{owner_id}", json.dumps(payload))

        assert response.status_code == 200

    def test_delete_owner_does_not_exist(self):
        client = testing.TestClient(router)

        owner_id = 102

        response = client.delete(f"/{owner_id}")

        assert response.status_code == 404

    def test_delete_owner_exist(self):
        client = testing.TestClient(router)

        owner_id = Owner.objects.create(name="test", address="test2").id

        response = client.delete(f"/{owner_id}")

        assert response.status_code == 204
