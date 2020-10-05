from source.repositories.teams_players_repository import TeamPlayerRepository

class TeamPlayerService:
    """TeamPlayer Service class representation."""

    @staticmethod
    def create_from_imported_data(team_id:int=None, player_id:int=None):
        """Create from imported data.
        This function call the teams__players repository to create a 
        team-player relation.
        Arguments:
            team_id : int
                An integer that represents the team id
            player_id : int
                An integer that represents the player id
        """
        new_team_player = {
            'player_id': player_id,
            'team_id': team_id
        }
        if not TeamPlayerRepository().get_relation(new_team_player):
            TeamPlayerRepository().create(new_team_player)

    @staticmethod
    def get_total_players_for_league(teams_id:list):
        """Get total players for league.
        This functions calls the team_players repository in order to
        obtains all the players related to the list of teams_id
        Arguments
            teams_id : list
                A list that contains teams id
        returns
            result : int
                The total amount of players to that list of teams
        """
        result = TeamPlayerRepository().count_players_by_teams(
            teams_id=teams_id
        )
        return result