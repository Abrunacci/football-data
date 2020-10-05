from fastapi import FastAPI
from source.routers import competitions, players, teams, importer

app = FastAPI()


app.include_router(competitions.router)
app.include_router(players.router)
app.include_router(teams.router)
app.include_router(importer.router)

@app.get('/')
def root():
    return {'hello': 'world', "it":"works"}