import random
from unittest.mock import patch
from source.repositories.players_repository import (PlayerRepository)


class TestPlayerRepository:
    """This is the PlayerService test class representation."""

    def setup(self):
        """Class setup"""
        self.repository = PlayerRepository()

    def teardown(self):
        """Class teardown"""
        pass

    def test_get_by_id_exists(self):
        """Test get_by_id function exist.
        This functions test that PlayerRepository.get_by_id function
        really exists.
        """
        assert hasattr(self.repository, 'get_by_id')

    def test_get_get_all_exists(self):
        """Test get_get_all function exist.
        This functions test that PlayerRepository.get_get_all function
        really exists.
        """
        assert hasattr(self.repository, 'get_all')