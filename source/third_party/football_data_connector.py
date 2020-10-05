from os import environ
import requests

from fastapi import HTTPException

class FootballDataConnector:
    """Football data connector class representation."""

    def __init__(self, *args, **kwargs):
        """Class inititalization"""
        self.base_url = environ.get('EXTERNAL_API_URL')
        self.headers = {
            "X-Auth-Token": environ.get('EXTERNAL_API_TOKEN')
        }
        self.params = None

    def get(self, endpoint:str = None):
        """Get
        This function executes a get request on the FootballData.
        
        Returns:
            data : JSON
                football data response
        """
        data = None
        try:
            url = f'{self.base_url}/{endpoint}'
            response = requests.get(url, headers=self.headers, params=self.params)
            data = response.json()
        except requests.exceptions.ConnectionError:
            raise HTTPException(status_code=504, detail='Server Error')
        except requests.exceptions.Timeout:  
            raise HTTPException(status_code=504, detail='Server Error')
        except requests.exceptions.HTTPError:
            raise HTTPException(status_code=504, detail='Server Error')  
        return data