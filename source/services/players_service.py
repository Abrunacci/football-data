from source.repositories.players_repository import PlayerRepository

class PlayerService:

    def get_player_by_id(self, player_id:int):
        player = PlayerRepository.get_by_filters({
            'player_id': player_id
        })
        return player