import googlemaps
import csv
from os import environ

locations = []

# Specify output map dimensions
MAP_DIMENSIONS = (1920, 1080)

# Specify output map name
MAP_FILENAME = 'mapify_img.png'

# le regioni d'italia
# Includes cities and smaller region denominations
# Comment this line out if reading from locations.csv
locations += ['Molise', 'Puglia', 'Veneto', 'Emilia Romagna', 'Milano', 'L\'Aquila', 'Campania']  # etc.

# Read from file if locations is empty
if not locations:
    with open('locations.csv', 'r') as locations_csv:
        csv_reader = csv.reader(locations_csv)
        header_row = next(csv_reader)
        for row in csv_reader:
            locations.append(row[1])


# Make the locations a dictionary
locations = dict(zip(range(0, len(locations)), locations))

# Save your Google Maps API key into an environment variable for security purposes
gmaps = googlemaps.Client(key=environ['GOOGLE_MAPS_API_KEY'])

# Geocode the locations
locations_geocode = {index: gmaps.geocode(location, components={'country': 'IT'})[0]['geometry']['location']
                     for index, location in locations.items()}

# Convert the resulting coordinates to be easy to parse
coordinates = {index: (coord['lat'], coord['lng']) for index, coord in locations_geocode.items()}

# Convert coordinates to markers to place on the map
coord_markers = googlemaps.maps.StaticMapMarker(locations=[coord for _, coord in locations_geocode.items()])

with open(MAP_FILENAME, 'wb') as map_file:
    for chunk in gmaps.static_map(size=MAP_DIMENSIONS, region='IT', markers=coord_markers):
        if chunk:
            map_file.write(chunk)
