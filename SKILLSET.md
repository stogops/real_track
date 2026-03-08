# Real Track Skillset

Interact with the Real Track application to manage real estate asset classes and locations.

## Functions

- `get_asset_classes()`: List all asset classes.
- `add_asset_class(name)`: Create a new asset class.
- `delete_asset_class(id)`: Remove an asset class.
- `get_counties(asset_class_id=None)`: List counties of interest.
- `add_county(county_name, state, asset_class_id)`: Create a new county of interest.
- `delete_county(id)`: Remove a county of interest.
- `get_locations()`: List all locations.
- `add_location(name, asset_class_id, county_id=None, address=None, latitude=None, longitude=None, square_footage=0, lot_size=0, tax_value=0)`: Create a new location.
- `delete_location(id)`: Remove a location.
