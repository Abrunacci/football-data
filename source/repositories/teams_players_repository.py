from .base import BaseRepository
from source.models import TeamPlayerModel

class TeamPlayerRepository(BaseRepository):
    """TeamPlayerRepository class representation."""
    
    def __init__(self, *args, **kwargs):
        """Class initialization."""
        super().__init__(model=TeamPlayerModel)

    def get_relation(self, relation:dict):
        query = self.db.query(self.model)
        for key, value in relation.items():
            query = query.filter(getattr(self.model, key) == value)
        result = query.all()
        return result

    def count_players_by_teams(self, teams_id:list):
        return self.db.query(self.model).filter(getattr(self.model, 'team_id').in_(teams_id)).count()