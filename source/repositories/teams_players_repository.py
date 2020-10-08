from .base import BaseRepository
from source.models import TeamPlayerModel

class TeamPlayerRepository(BaseRepository):
    """TeamPlayerRepository class representation."""
    
    def __init__(self, *args, **kwargs):
        """Class initialization."""
        super().__init__(model=TeamPlayerModel)

    def get_relation(self, relation:dict):
        """Get relation.
        This function search on the database for a particular team-player
        relation.

        Arguments:
            relation : dict
                Dict object with team_id/player_id relation.
        Returns:
            result : list
                A list with all the relations founded.
        """
        query = self.db.query(self.model)
        for key, value in relation.items():
            query = query.filter(getattr(self.model, key) == value)
        result = query.all()
        return result

    def count_players_by_teams(self, teams_id:list):
        """Count players by teams.
        This functions search for all the players related to a list of
        teams_id.

        Arguments:
            teams_id : list
                A list of teams id
        Returns:
            result : int
                The total of players
        """
        return self.db.query(self.model).filter(
            getattr(self.model, 'team_id').in_(teams_id)).count()
