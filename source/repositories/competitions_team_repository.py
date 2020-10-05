from .base import BaseRepository
from source.models import CompetitionTeamModel

class CompetitionTeamRepository(BaseRepository):
    """CompetitionTeamRepository class representation."""
    
    def __init__(self, *args, **kwargs):
        """Class initialization."""
        super().__init__(model=CompetitionTeamModel)

    def get_relation(self, relation:dict):
        query = self.db.query(self.model)
        for key, value in relation.items():
            query = query.filter(getattr(self.model, key) == value)
        result = query.all()
        return result

    def get_all_teams_from_competition(self, competition_id:list):
        return self.db.query(self.model).filter(getattr(self.model, 'competition_id') == competition_id).all()