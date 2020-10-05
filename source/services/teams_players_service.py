from source.repositories.teams_players_repository import TeamPlayerRepository

class TeamPlayerService:
    """TeamPlayer Service class representation."""

    @staticmethod
    def create_from_imported_data(team_id:int=None, player_id:int=None):
        new_team_player = {
            'player_id': player_id,
            'team_id': team_id
        }
        if not TeamPlayerRepository().get_relation(new_team_player):
            TeamPlayerRepository().create(new_team_player)

    @staticmethod
    def get_total_players_for_league(teams_id:list):
        return TeamPlayerRepository().count_players_by_teams(
            teams_id=teams_id
        )