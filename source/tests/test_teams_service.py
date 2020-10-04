import random
from unittest.mock import patch
from source.services.teams_service import (TeamService, 
                                             TeamRepository)


class TestTeamService:
    """This is the TeamService test class representation."""

    def setup(self):
        """Class setup"""
        self.service = TeamService()

    def teardown(self):
        """Class teardown"""
        pass

    @patch.object(TeamRepository, 'get_by_id')
    def test_get_team_by_id(self, patched_repository_function):
        """Test get_team_by_id.
        This functions test that TeamService.get_team_by_id calls
        the TeamRepository.get_by_filters with the correct data
        """
        team_id = random.randint(0,100)
        patched_repository_function.return_value = None
        
        self.service.get_team_by_id(team_id)

        patched_repository_function.assert_called_once_with(team_id)

    @patch.object(TeamRepository, 'get_all')
    def test_get_all(self, patched_repository_function):
        """Test get_all.
        This functions test that TeamService.get_all calls
        the TeamRepository.get_all function only one time
        """
        patched_repository_function.return_value = []
        
        self.service.get_all()

        patched_repository_function.assert_called_once()