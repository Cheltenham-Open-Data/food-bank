# import
from requests import get
import json
import pathlib
import os

city = os.getenv('city_code') or 'cheltenham'

def get_data_from_endpoint():
    endpoint = (f'https://www.givefood.org.uk/api/2/foodbank/{city}/')
    response = get(endpoint, timeout=10)
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
    return response.json()

# output
if __name__ == "__main__":
    root = pathlib.Path(__file__).parent.parent.resolve()
    with open( root / "foodbank.json", 'r+') as filehandle:
        data = json.load(filehandle)
        new_data = get_data_from_endpoint()
        filehandle.seek(0)
        json.dump(new_data, filehandle, indent=4)