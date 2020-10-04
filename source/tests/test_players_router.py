import random
from contextlib import contextmanager
from pytest import fixture
from datetime import datetime

from unittest.mock import patch
from source.routers.players import PlayerService
from source.schemas.players_schemas import PlayerSchema
from fastapi.testclient import TestClient

from source.main import app

client = TestClient(app)

@contextmanager
def patch_services():
    with patch('source.routers.players.PlayerService') as service:
        yield service

@fixture(scope='function')
def player_schema():
    player = PlayerSchema(
        name = 'Antonio Barijho',
        position = 'Delantero',
        day_of_birth = datetime.strptime('1987-12-22 00:00:00', "%Y-%m-%d %H:%M:%S"),
        country_of_birth = "Argentina",
        nationality = "Argentina"
    )
    return player

class TestPlayerRouter:
    """This is the PlayerService test class representation."""

    def setup(self):
        """Class setup"""
        pass

    def teardown(self):
        """Class teardown"""
        pass
    
    def test_get_by_id(self, player_schema):
        """This function test if the router calls the get_player_by_id
        fuction for the PlayerSerivce with the expected parameters."""
        player_id = random.randint(0,1000)
        with patch_services() as mocked_service:
            mocked_service.get_player_by_id.return_value = player_schema

            response = client.get(f'/players/{player_id}')
            
            assert response.status_code == 200
            mocked_service.get_player_by_id.assert_called_once_with(
                player_id=player_id
            )

    def test_get_all(self, player_schema):
        """This function test if the router calls the get_all
        fuction for the PlayerSerivce."""
        with patch_services() as mocked_service:
            mocked_service.get_all.return_value = [player_schema]

            response = client.get('/players/')
            
            assert response.status_code == 200
            mocked_service.get_all.assert_called_once()