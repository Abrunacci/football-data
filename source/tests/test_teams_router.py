import random
from contextlib import contextmanager
from pytest import fixture
from datetime import datetime

from unittest.mock import patch
from source.routers.teams import TeamService
from source.schemas.teams_schemas import TeamSchema
from fastapi.testclient import TestClient

from source.main import app


client = TestClient(app)


@contextmanager
def patch_services():
    with patch('source.routers.teams.TeamService') as service:
        yield service


@fixture(scope='function')
def team_schema():
    team = TeamSchema(
        name = 'BOKEE',
        tla = 'BOC',
        area_name = "Argentina",
        email = "esto_es@boca.com.ar"
    )
    return team


class TestTeamRouter:
    """This is the TeamService test class representation."""

    def setup(self):
        """Class setup"""
        pass

    def teardown(self):
        """Class teardown"""
        pass
    
    def test_get_by_id(self, team_schema):
        """This function test if the router calls the get_team_by_id
        fuction for the TeamSerivce with the expected parameters."""
        team_id = random.randint(0,1000)
        with patch_services() as mocked_service:
            mocked_service.get_team_by_id.return_value = team_schema

            response = client.get(f'/teams/{team_id}')
            
            assert response.status_code == 200
            mocked_service.get_team_by_id.assert_called_once_with(
                team_id=team_id
            )

    def test_get_all(self, team_schema):
        """This function test if the router calls the get_all
        fuction for the TeamSerivce."""
        with patch_services() as mocked_service:
            mocked_service.get_all.return_value = [team_schema]

            response = client.get('/teams/')
            
            assert response.status_code == 200
            mocked_service.get_all.assert_called_once()