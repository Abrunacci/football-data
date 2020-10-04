from .base import BaseRepository
from source.models import CompetitionModel

class CompetitionRepository(BaseRepository):
    """CompetitionRepository class representation."""
    
    def __init__(self, *args, **kwargs):
        """Class initialization."""
        super().__init__(model=CompetitionModel)