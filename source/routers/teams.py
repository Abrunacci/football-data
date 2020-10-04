from typing import List

from fastapi import APIRouter, HTTPException

from source.services.teams_service import TeamService
from source.schemas.teams_schemas import TeamSchema


router = APIRouter()


@router.get('/teams/{team_id}', tags=['Teams'], response_model=TeamSchema)
async def get_team(team_id: int):
    team = TeamService.get_team_by_id(team_id=team_id)
    return team


@router.get('/teams/', tags=['Teams'], response_model=List[TeamSchema])
async def get_teams():
    teams = TeamService.get_all()
    return teams