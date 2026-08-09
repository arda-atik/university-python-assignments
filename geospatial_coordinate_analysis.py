import math

def validate_coordinates(coordinates):
    """Validates if coordinates are a valid (latitude, longitude) pair."""
    # 1) Must be list or tuple
    if not isinstance(coordinates, (list, tuple)):
        raise TypeError

    # 2) Must have length 2
    if len(coordinates) != 2:
        raise ValueError

    lat = coordinates[0]
    lon = coordinates[1]

    # 3) Both must be int or float
    if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
        raise TypeError

    # 4) Latitude range [-90, 90]
    if lat < -90 or lat > 90:
        raise ValueError

    # 5) Longitude range [-180, 180]
    if lon < -180 or lon > 180:
        raise ValueError


def geo_distance(coordinates1, coordinates2):
    """Calculates the distance between two points on the Earth's surface in km."""
    # Input validation
    validate_coordinates(coordinates1)
    validate_coordinates(coordinates2)

    # Approximate radius of earth in km
    radius = 6373

    # Unpack the coordinates
    lat1, lon1 = coordinates1
    lat2, lon2 = coordinates2

    # Calculate angles in radians
    dlon = math.radians(lon2 - lon1)
    dlat = math.radians(lat2 - lat1)

    # Apply the haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 2 * radius * c

    return distance


def geo_path_distance(*coordinates):
    """Calculates the total distance traveled following points on a given path."""
    # Input adjustments and validation
    if len(coordinates) == 0:
        raise ValueError

    if len(coordinates) == 1:
        if not isinstance(coordinates[0], (list, tuple)):
            raise TypeError
        coordinates = coordinates[0]

    # Corner case: single coordinate provided
    if len(coordinates) == 1:
        validate_coordinates(coordinates[0])
        return 0

    # Calculation of the distance
    distance = 0

    i = 0
    while i < len(coordinates) - 1:
        distance = distance + geo_distance(coordinates[i], coordinates[i + 1])
        i = i + 1

    return distance


def filter_invalid_coordinates(coordinates):
    """Checks if coordinates are valid and categorizes them by exception types."""
    valid = set()
    type_errors = set()
    value_errors = set()

    for coord in coordinates:
        # Convert list -> tuple so it can be stored in a set
        if isinstance(coord, list):
            store = tuple(coord)
        else:
            store = coord

        try:
            validate_coordinates(coord)
            valid.add(store)
        except TypeError:
            type_errors.add(store)
        except ValueError:
            value_errors.add(store)

    return valid, type_errors, value_errors
