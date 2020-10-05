from .base import BaseRepository
from source.models import CompetitionModel

class CompetitionRepository(BaseRepository):
    """CompetitionRepository class representation."""
    
    def __init__(self, *args, **kwargs):
        """Class initialization."""
        super().__init__(model=CompetitionModel)

    def get_by_code(self, competition_code:str=None):
        """Get by code.
        This functions search a competition by code and returns it.
        """
        competition = self.db.query(self.model).filter(
            getattr(self.model,'code') == competition_code).all()
        return competition
