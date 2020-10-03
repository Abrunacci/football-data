class BaseRepository:

    @classmethod
    def get_by_filters(cls, filters:dict):
        """Get by filters.
        This functions returns a list of players found on the database
        using the received filters.

        arguments:
            filters : dict
                A dictionary that contains <filter_key>/<filter_value>.
        returns:
            players : list
                A list that contains all the players found for the 
                specified filters.
        """
        players = list()
        for player in cls.players:
            for filter_key, filter_value in filters.items():
                if player.get(filter_key) == filter_value:
                    players.append(player)
        return players