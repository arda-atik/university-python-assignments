def analyze_flight_tickets(tickets):
    """
    Analyzes flight tickets and returns destination stats, 
    passenger stats, and total revenue.
    """
    
    # Validate ticket data
    for t in tickets:
        # Check for missing keys
        if ("passenger" not in t or
            "origin" not in t or
            "destination" not in t or
            "price" not in t or
            "duration" not in t or
            "distance" not in t):
            return None
        
        # Check string types
        if type(t["passenger"]) != str: return None
        if type(t["origin"]) != str: return None
        if type(t["destination"]) != str: return None

        price = t["price"]
        duration = t["duration"]
        distance = t["distance"]

        # Check numeric types and positive values
        for v in (price, duration, distance):
            if not isinstance(v, (int, float)):
                return None
            if v <= 0:
                return None
        
        # Check if floats are convertible to integers without error
        for v in (duration, distance):
            if isinstance(v, float) and not v.is_integer():
                return None
        
        # Route validity check
        if t["origin"] == t["destination"]:
            return None

    # Initialize statistics containers
    destination_stats = {}
    passenger_stats = {}
    total_revenue = 0

    # Calculate statistics
    for t in tickets:
        passenger = t["passenger"]
        origin = t["origin"]
        dest = t["destination"]
        price = t["price"]
        duration = t["duration"]
        distance = t["distance"]

        # Update destination statistics
        if dest not in destination_stats:
            destination_stats[dest] = 0
        destination_stats[dest] += 1

        # Initialize passenger statistics if not exists
        if passenger not in passenger_stats:
            passenger_stats[passenger] = {
                "total_duration": 0,
                "total_distance": 0,
                "total_price": 0,
                "visited_airports": set()
            }
        
        # Update passenger statistics
        pstats = passenger_stats[passenger]
        pstats["total_duration"] += duration
        pstats["total_distance"] += distance
        pstats["total_price"] += price
        pstats["visited_airports"].add(origin)
        pstats["visited_airports"].add(dest)

        # Accumulate total revenue
        total_revenue += price

    return {
        "destination_stats": destination_stats,
        "passenger_stats": passenger_stats,
        "total_revenue": total_revenue
    }
