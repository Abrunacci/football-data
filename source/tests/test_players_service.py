import random
from unittest.mock import patch
from source.services.players_service import (PlayerService, 
                                             PlayerRepository)


class TestPlayerService:
    """This is the PlayerService test class representation."""

    def setup(self):
        """Class setup"""
        self.service = PlayerService()

    def teardown(self):
        """Class teardown"""
        pass

    @patch.object(PlayerRepository, 'get_by_filters')
    def test_get_player_by_id(self, patched_repository_function):
        """Test get_player_by_id.
        This functions test that PlayerService.get_player_by_id calls
        the PlayerRepository.get_by_filters with the correct data
        """
        player_id = random.randint(0,100)
        player_filter = {"player_id": player_id}

        patched_repository_function.return_value = []
        
        self.service.get_player_by_id(player_id)

        patched_repository_function.assert_called_once_with(player_filter)