import json
from jsonschema import validate

# task 2

try:
    with (open("arrondissements.json", "r")) as file:
        paris_arrondissements = json.load(file)
except Exception:
    print("Something went wrong reading the json file")
    exit()

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
try:
    with (open("geometry.json", "w")) as file:
        json.dump(geometry, file)
except Exception:
    print("Something went wrong writing the json file")
    exit()
# task 3 (I can't find schema for geojson that works)
with open('my_file_schema.json','r') as schema_fp:
    my_schema = json.load(schema_fp)

with open('my_file.json','r') as my_file_fp:
    my_file_data = json.load(my_file_fp)

with open('my_wrong_file.json','r') as my_invalid_fp:
    invalid_data = json.load(my_invalid_fp)


# this works with the files given
print(validate(instance=my_file_data,schema=my_schema))
print(validate(instance=invalid_data,schema=my_schema))








           
        