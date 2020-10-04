from .base import BaseRepository
from source.models import PlayerModel

class PlayerRepository(BaseRepository):
    """PlayerRepository class representation."""
    
    def __init__(self, *args, **kwargs):
        """Class initialization."""
        super().__init__(model=PlayerModel)
