import random
from unittest.mock import patch
from source.services.competitions_service import (CompetitionService, 
                                                  CompetitionRepository)


class TestCompetitionService:
    """This is the CompetitionService test class representation."""

    def setup(self):
        """Class setup"""
        self.service = CompetitionService()

    def teardown(self):
        """Class teardown"""
        pass

    @patch.object(CompetitionRepository, 'get_by_id')
    def test_get_competition_by_id(self, patched_repository_function):
        """Test get_competition_by_id.
        This functions test that CompetitionService.get_competition_by_id calls
        the CompetitionRepository.get_by_filters with the correct data
        """
        competition_id = random.randint(0,100)
        patched_repository_function.return_value = None
        
        self.service.get_competition_by_id(competition_id)

        patched_repository_function.assert_called_once_with(competition_id)

    @patch.object(CompetitionRepository, 'get_all')
    def test_get_all(self, patched_repository_function):
        """Test get_all.
        This functions test that CompetitionService.get_all calls
        the CompetitionRepository.get_all function only one time
        """
        patched_repository_function.return_value = []
        
        self.service.get_all()

        patched_repository_function.assert_called_once()