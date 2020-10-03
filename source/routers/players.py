from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/players/{player_id}', tags=['Players'])
async def get_player_by_id(player_id:int):
    return {}


@router.get('/players/', tags=['Players'])
async def get_players():
    return [
    {
        "id": 4,
        "area": {
            "id": 2088,
            "name": "Germany"
        },
        "name": "BV Borussia 09 Dortmund",
        "shortName": "Dortmund",
        "tla": "BVB",
        "crestUrl": "https://crests.football-data.org/4.svg",
        "address": "Rheinlanddamm 207-209 Dortmund 44137",
        "phone": "+49 (231) 90200",
        "website": "http://www.bvb.de",
        "email": "info@bvb.de",
        "founded": 1909,
        "clubColors": "Black / Yellow",
        "venue": "Signal Iduna Park",
        "lastUpdated": "2020-10-01T01:58:22Z"
    },
    {
        "id": 5,
        "area": {
            "id": 2088,
            "name": "Germany"
        },
        "name": "FC Bayern München",
        "shortName": "Bayern M",
        "tla": "FCB",
        "crestUrl": "https://crests.football-data.org/5.svg",
        "address": "Säbenerstr. 51 München 81547",
        "phone": "+49 (089) 699310",
        "website": "http://www.fcbayern.de",
        "email": "service-team@fcb.de",
        "founded": 1900,
        "clubColors": "Red / White / Blue",
        "venue": "Allianz Arena",
        "lastUpdated": "2020-09-24T01:56:58Z"
    },
    {
        "id": 18,
        "area": {
            "id": 2088,
            "name": "Germany"
        },
        "name": "Borussia Mönchengladbach",
        "shortName": "M'gladbach",
        "tla": "BMG",
        "crestUrl": "https://crests.football-data.org/18.svg",
        "address": "Hennes-Weisweiler-Allee 1 Mönchengladbach 41179",
        "phone": "+49 (02161) 92930",
        "website": "http://www.borussia.de",
        "email": "info@borussia.de",
        "founded": 1900,
        "clubColors": "Black / White / Green",
        "venue": "Stadion im Borussia-Park",
        "lastUpdated": "2020-09-17T01:57:44Z"
    },
    {
        "id": 61,
        "area": {
            "id": 2072,
            "name": "England"
        },
        "name": "Chelsea FC",
        "shortName": "Chelsea",
        "tla": "CHE",
        "crestUrl": "https://crests.football-data.org/61.svg",
        "address": "Fulham Road London SW6 1HS",
        "phone": "+44 (0871) 9841955",
        "website": "http://www.chelseafc.com",
        "email": None,
        "founded": 1905,
        "clubColors": "Royal Blue / White",
        "venue": "Stamford Bridge",
        "lastUpdated": "2020-09-17T01:59:20Z"
    },
    {
        "id": 64,
        "area": {
            "id": 2072,
            "name": "England"
        },
        "name": "Liverpool FC",
        "shortName": "Liverpool",
        "tla": "LIV",
        "crestUrl": "https://crests.football-data.org/64.svg",
        "address": "Anfield Road Liverpool L4 OTH",
        "phone": "+44 (0844) 4993000",
        "website": "http://www.liverpoolfc.tv",
        "email": "customercontact@liverpoolfc.tv",
        "founded": 1892,
        "clubColors": "Red / White",
        "venue": "Anfield",
        "lastUpdated": "2020-09-10T02:55:23Z"
    },
    {
        "id": 65,
        "area": {
            "id": 2072,
            "name": "England"
        },
        "name": "Manchester City FC",
        "shortName": "Man City",
        "tla": "MCI",
        "crestUrl": "https://crests.football-data.org/65.svg",
        "address": "SportCity Manchester M11 3FF",
        "phone": "+44 (0870) 0621894",
        "website": "https://www.mancity.com",
        "email": "mancity@mancity.com",
        "founded": 1880,
        "clubColors": "Sky Blue / White",
        "venue": "Etihad Stadium",
        "lastUpdated": "2020-09-17T01:59:21Z"
    },
    {
        "id": 66,
        "area": {
            "id": 2072,
            "name": "England"
        },
        "name": "Manchester United FC",
        "shortName": "Man United",
        "tla": "MUN",
        "crestUrl": "https://crests.football-data.org/66.svg",
        "address": "Sir Matt Busby Way Manchester M16 0RA",
        "phone": "+44 (0161) 8688000",
        "website": "http://www.manutd.com",
        "email": "enquiries@manutd.co.uk",
        "founded": 1878,
        "clubColors": "Red / White",
        "venue": "Old Trafford",
        "lastUpdated": "2020-09-17T01:59:23Z"
    },
    {
        "id": 78,
        "area": {
            "id": 2224,
            "name": "Spain"
        },
        "name": "Club Atlético de Madrid",
        "shortName": "Atleti",
        "tla": "ATM",
        "crestUrl": "https://crests.football-data.org/78.svg",
        "address": "Paseo Virgen del Puerto, 67 Madrid 28005",
        "phone": "+34 (913) 669048",
        "website": "http://www.clubatleticodemadrid.com",
        "email": "comunicacion@clubatleticodemadrid.com",
        "founded": 1903,
        "clubColors": "Red / White / Blue",
        "venue": "Estadio Wanda Metropolitano",
        "lastUpdated": "2020-09-17T01:59:08Z"
    }]