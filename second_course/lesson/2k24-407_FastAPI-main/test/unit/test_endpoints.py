import pytest

from fastapi import status

class TestEndpoints:
    @pytest.mark.parametrize(
        "path, expected",
        [
            ('/rooms', status.HTTP_200_OK),
            ('/rooms/', status.HTTP_200_OK),
        ]
    )
    def test_get_rooms(self, http_client, path, expected):
        response = http_client.get(path)
        print(response.json())
        assert response.status_code == expected 