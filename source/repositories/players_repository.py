players =  [{
            "id": 115,
            "name": "José Maria Giménez",
            "position": "Defender",
            "dateOfBirth": "1995-01-20T00:00:00Z",
            "countryOfBirth": "Uruguay",
            "nationality": "Uruguay",
            "shirtNumber": None,
            "role": "PLAYER"
        },
        {
            "id": 116,
            "name": "Šime Vrsaljko",
            "position": "Defender",
            "dateOfBirth": "1992-01-10T00:00:00Z",
            "countryOfBirth": "Croatia",
            "nationality": "Croatia",
            "shirtNumber": None,
            "role": "PLAYER"
        },
        {
            "id": 1671,
            "name": "Renan Lodi",
            "position": "Defender",
            "dateOfBirth": "1998-04-08T00:00:00Z",
            "countryOfBirth": "Brazil",
            "nationality": "Brazil",
            "shirtNumber": None,
            "role": "PLAYER"
        },
        {
            "id": 3312,
            "name": "Kieran Trippier",
            "position": "Defender",
            "dateOfBirth": "1990-09-19T00:00:00Z",
            "countryOfBirth": "England",
            "nationality": "England",
            "shirtNumber": None,
            "role": "PLAYER"
        }]


class PlayerRepository:
    """PlayerRepository class representation."""

    @staticmethod
    def get_by_filters(filters:dict):
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
        for player in players:
            for filter_key, filter_value in filters.items():
                if player.get(filter_key) == filter_value:
                    players.append(player)
        return players