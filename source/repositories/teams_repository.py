from .base import BaseRepository
from source.models import TeamModel

class TeamRepository(BaseRepository):
    """TeamRepository class representation."""
    
    def __init__(self, *args, **kwargs):
        """Class initialization."""
        super().__init__(model=TeamModel)