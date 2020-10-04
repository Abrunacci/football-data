import random
from unittest.mock import patch
from source.repositories.competitions_repository import (CompetitionRepository)


class TestCompetitionRepository:
    """This is the CompetitionService test class representation."""

    def setup(self):
        """Class setup"""
        self.repository = CompetitionRepository()

    def teardown(self):
        """Class teardown"""
        pass

    def test_get_by_id_exists(self):
        """Test get_by_id function exist.
        This functions test that CompetitionRepository.get_by_id function
        really exists.
        """
        assert hasattr(self.repository, 'get_by_id')

    def test_get_get_all_exists(self):
        """Test get_get_all function exist.
        This functions test that CompetitionRepository.get_get_all function
        really exists.
        """
        assert hasattr(self.repository, 'get_all')