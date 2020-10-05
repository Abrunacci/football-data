from fastapi import HTTPException
from source.repositories.competitions_repository import CompetitionRepository

class CompetitionService:
    """Competition Service class representation."""

    @staticmethod
    def get_competition_by_code(competition_code:str):
        """Get competition by id.
        This function calls the get_by_id function from 
        CompetitionRepository and returns a competition instance when the id 
        it's correct. Otherwise, returns 404.
        
        Arguments
            competition_code : str
                An string that represents the competition code
        Returns
            competition : CompetitionModel
                An instance of CompetitionModel
        """
        competition = CompetitionRepository().get_by_code(competition_code)
        if not competition:
            raise HTTPException(status_code=404, detail="Competition not found")
        return competition[0]
    
    @staticmethod
    def get_all():
        """Get all.
        This function calls the get_all function from 
        CompetitionRepository and returns a list of competition instances.
        
        Returns
            competitions : List[CompetitionModel]
                A list of CompetitionModel instances
        """
        competitions = CompetitionRepository().get_all()
        return competitions

    @staticmethod
    def create_from_imported_data(data:dict=None):
        """create from imported data.
        This function calls the repository to insert the 
        competition on the database.
        """
        new_competition = {
            "id" : data.get('id'),
            "name": data.get('name'),
            "code": data.get('code'),
            "area_name": data.get('area', {}).get('name')
        }
        if not CompetitionRepository().get_by_id(data.get('id')):
            CompetitionRepository().create(new_competition)