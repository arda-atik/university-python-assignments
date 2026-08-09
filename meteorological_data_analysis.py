def average_temp(data):
    """Return average temperature or None if data is empty."""
    if data == []:
        return None
        
    total = 0
    count = 0
    for day, temp in data:
        total = total + temp
        count = count + 1
        
    return total / count

def hot_days(data, threshold=25.0):
    """Return list of (day, temp) with temp >= threshold."""
    result = []
    for day, temp in data:
        if temp >= threshold:
            result.append((day, temp))
            
    return result

def temp_range(data):
    """Return max - min temperature or None if data is empty."""
    if data == []:
        return None
        
    first_day, first_temp = data[0]
    max_temp = first_temp
    min_temp = first_temp
    
    for day, temp in data:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp
            
    return max_temp - min_temp

def temperature_summary(data, hot_threshold=25.0):
    """Return (average_temp, hot_days, temp_range)."""
    if data == []:
        return (None, [], None)
        
    avg = average_temp(data)
    hot = hot_days(data, hot_threshold)
    rng = temp_range(data)
    
    return (avg, hot, rng)
