import requests

API_URL = "http://real-track-svc.os-stogops-wrk.svc.cluster.local/api"

def get_asset_classes():
    '''Returns a list of all asset classes.'''
    response = requests.get(f"{API_URL}/asset-classes")
    response.raise_for_status()
    return response.json()

def add_asset_class(name: str):
    '''Adds a new asset class.'''
    response = requests.post(f"{API_URL}/asset-classes", json={"name": name})
    response.raise_for_status()
    return response.json()

def delete_asset_class(id: int):
    '''Deletes an asset class and all its locations.'''
    response = requests.delete(f"{API_URL}/asset-classes/{id}")
    response.raise_for_status()
    return response.json()

def get_counties(asset_class_id=None):
    '''Returns a list of counties, optionally filtered by asset class ID.'''
    params = {}
    if asset_class_id:
        params["asset_class_id"] = asset_class_id
    response = requests.get(f"{API_URL}/counties", params=params)
    response.raise_for_status()
    return response.json()

def add_county(county_name: str, state: str, asset_class_id: int):
    '''Creates a new county of interest for a specific asset class.'''
    payload = {
        "county_name": county_name,
        "state": state,
        "asset_class_id": asset_class_id
    }
    response = requests.post(f"{API_URL}/counties", json=payload)
    response.raise_for_status()
    return response.json()

def delete_county(id: int):
    '''Deletes a county of interest.'''
    response = requests.delete(f"{API_URL}/counties/{id}")
    response.raise_for_status()
    return response.json()

def get_locations():
    '''Returns a list of all locations, including their name, address, coordinates, square footage, lot size, and tax value.'''
    response = requests.get(f"{API_URL}/locations")
    response.raise_for_status()
    return response.json()

def add_location(name, asset_class_id, county_id=None, address=None, latitude=None, longitude=None, square_footage=0, lot_size=0, tax_value=0):
    '''Adds a new location with optional county, address, coordinates, square footage, lot size, and tax value.'''
    payload = {
        "name": name,
        "asset_class_id": asset_class_id,
        "county_id": county_id,
        "square_footage": square_footage,
        "lot_size": lot_size,
        "tax_value": tax_value
    }
    
    if address:
        payload["address"] = address
    if latitude is not None:
        payload["latitude"] = latitude
    if longitude is not None:
        payload["longitude"] = longitude

    response = requests.post(f"{API_URL}/locations", json=payload)
    response.raise_for_status()
    return response.json()

def delete_location(id: int):
    '''Deletes a location.'''
    response = requests.delete(f"{API_URL}/locations/{id}")
    response.raise_for_status()
    return response.json()
