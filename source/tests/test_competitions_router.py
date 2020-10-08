import random
from contextlib import contextmanager
from pytest import fixture
from datetime import datetime

from unittest.mock import patch
from typing import List
from source.routers.competitions import CompetitionService
from source.schemas.competitions_schemas import CompetitionSchema
from .test_teams_router import team_schema
from fastapi.testclient import TestClient

from source.main import app


client = TestClient(app)


@contextmanager
def patch_services():
    with patch('source.routers.competitions.CompetitionService') as service:
        yield service


@fixture(scope='function')
def competition_schema():
    competition = CompetitionSchema(
        name = 'Superliga Argentina',
        code = 'ASL',
        area_name = "Argentina",
    )
    return competition


class TestCompetitionRouter:
    """This is the CompetitionService test class representation."""

    def setup(self):
        """Class setup"""
        pass

    def teardown(self):
        """Class teardown"""
        pass
    
    def test_get_by_id(self, competition_schema):
        """This function test if the router calls the get_competition_by_id
        fuction for the CompetitionSerivce with the expected parameters."""
        competition_id = 'asl'
        schema = competition_schema
        with patch_services() as mocked_service:
            mocked_service.get_competition_by_code.return_value = schema

            response = client.get(f'/competitions/{competition_id}')
            
            assert response.status_code == 200
            mocked_service.get_competition_by_code.assert_called_once_with(
                competition_code=competition_id
            )

    def test_get_all(self, competition_schema):
        """This function test if the router calls the get_all
        fuction for the CompetitionSerivce."""
        with patch_services() as mocked_service:
            mocked_service.get_all.return_value = [competition_schema]

            response = client.get('/competitions/')
            
            assert response.status_code == 200
            mocked_service.get_all.assert_called_once()