
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

def get_locations():
    '''Returns a list of all locations.'''
    response = requests.get(f"{API_URL}/locations")
    response.raise_for_status()
    return response.json()

def add_location(name: str, asset_class_id: int, address: str = None):
    '''Adds a new location.'''
    payload = {"name": name, "asset_class_id": asset_class_id}
    if address:
        payload["address"] = address
    response = requests.post(f"{API_URL}/locations", json=payload)
    response.raise_for_status()
    return response.json()

def delete_location(id: int):
    '''Deletes a location.'''
    response = requests.delete(f"{API_URL}/locations/{id}")
    response.raise_for_status()
    return response.json()
