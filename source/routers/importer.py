from typing import List

from fastapi import APIRouter, HTTPException

from source.services.importer_service import ImporterService


router = APIRouter()


@router.get('/import-data/{competition_code}', 
            tags=['Importer'],
            status_code=201)
async def import_data(competition_code: str):
    ImporterService().import_data(
        competition_code=competition_code
    )
    return {'message':'Successfully imported'}