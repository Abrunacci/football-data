from source.repositories.players_repository import PlayerRepository

class PlayerService:
    """Player Service class representation."""

    @staticmethod
    def get_player_by_id(player_id:int):
        """Get player by id.
        This function calls the get_by_id function from 
        PlayerRepository and returns a player instance when the id 
        it's correct. Otherwise, returns 404.
        
        Arguments
            player_id : int
                An integer that represents the player id
        Returns
            player : PlayerModel
                An instance of PlayerModel
        """
        player = PlayerRepository().get_by_id(player_id)
        return player
    
    @staticmethod
    def get_all():
        """Get all.
        This function calls the get_all function from 
        PlayerRepository and returns a list of player instances.
        
        Returns
            players : List[PlayerModel]
                A list of PlayerModel instances
        """
        players = PlayerRepository().get_all()
        return players