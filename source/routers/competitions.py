from typing import List

from fastapi import APIRouter, HTTPException

from source.services.competitions_service import CompetitionService
from source.schemas.competitions_schemas import CompetitionSchema


router = APIRouter()


@router.get('/competitions/{competition_id}', 
            tags=['Competitions'], 
            response_model=CompetitionSchema)
async def get_competition(competition_id: int):
    competition = CompetitionService.get_competition_by_id(
        competition_id=competition_id
    )
    return competition


@router.get('/competitions/',
            tags=['Competitions'],
            response_model=List[CompetitionSchema])
async def get_competitions():
    competitions = CompetitionService.get_all()
    return competitions