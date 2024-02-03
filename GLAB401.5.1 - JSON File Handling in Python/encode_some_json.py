import json

# task 2

with (open("arrondissements.json", "r")) as file:
    paris_arrondissements = json.load(file)

for feature in paris_arrondissements['features']:
    geometry = feature['geometry']

    for coords in geometry['coordinates']:
        list_coords = coords

        for coord in list_coords:
            print(coord)
        