import json

# task 2

with (open("arrondissements.json", "r")) as file:
    paris_arrondissements = json.load(file)

# this shows the border coordinates for each
# feature
for feature in paris_arrondissements['features']:
    geometry = feature['geometry']
    # name of location
    print(feature['properties']['l_aroff'])

    # coords for location
    for coords in geometry['coordinates']:
        
        # coords in a list
        list_coords = coords
        # individual long/lat pairs
        for coord in list_coords:    
            print(coord)

# task 1 - encode geometry dictionary to json
with (open("geometry.json", "w")) as file:
    json.dump(geometry, file)
           
        