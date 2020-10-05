from .base import BaseRepository
from source.models import CompetitionTeamModel

class CompetitionTeamRepository(BaseRepository):
    """CompetitionTeamRepository class representation."""
    
    def __init__(self, *args, **kwargs):
        """Class initialization."""
        super().__init__(model=CompetitionTeamModel)

    def get_relation(self, relation:dict):
        """Get relation.
        This functions search for a relation on the database.

        returns
            result : list
                A list of CompetitionTeam objects
        """
        query = self.db.query(self.model)
        for key, value in relation.items():
            query = query.filter(getattr(self.model, key) == value)
        result = query.all()
        return result

    def get_all_teams_from_competition(self, competition_id:int):
        """Get all teams from competition.
        This functions search all the teams related to a competition
        
        Arguments:
            competition_id : int
                A integer that represent the competition_id
        Returns:
            result : list
                A list that contains all the teams_id for the competition
        """
        result = self.db.query(self.model).filter(
            getattr(self.model, 'competition_id') == competition_id).all()
        
        return result