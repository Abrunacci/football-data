from typing import List
from source.models.base import SessionLocal

class BaseRepository:
    """Base repository class representation."""

    def __init__(self, *args, **kwargs):
        """Class initialization."""
        self.db = SessionLocal()
        self.model = kwargs.get('model')

    def get_all(self):
        """ Get all.
        This function returns all the registered items 
        for the given model."""
        result = self.db.query(self.model).filter().all()
        return result

    def get_by_id(self, id:int) -> List:
        """Get by filters.
        This functions returns a list of items found on the database
        using the received id.

        arguments:
            id : int
                An integer that represent the model id.
        returns:
            result : model
                A self.model instance
        """
        result = self.db.query(self.model).get(id)
        return result