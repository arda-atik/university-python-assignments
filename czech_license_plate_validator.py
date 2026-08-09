def analyze_license_plate(plate):
    """
    Analyzes a Czech license plate string and classifies it as 
    'standard', 'custom', 'electric', or 'invalid'.
    """
    if plate is None:
        return "invalid"
        
    plate = plate.strip()
    
    # Preprocessing: Handle allowed single space at index 3
    if " " in plate:
        if len(plate) < 4 or plate.count(" ") != 1 or plate[3] != " ":
            return "invalid"
        plate = plate.replace(" ", "")
        
    digits = "0123456789"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    forbidden = "GOQW"
    allowed = digits + letters
    
    has_digit = False
    
    # Universal rules check
    for c in plate:
        if c not in allowed or c in forbidden:
            return "invalid"
        if c in digits:
            has_digit = True
            
    if not has_digit:
        return "invalid"
        
    # Electric vehicle plate check
    if len(plate) == 7 and plate.startswith("EL"):
        if (plate[2] in digits and plate[3] in digits and plate[4] in digits
            and plate[5] in allowed and plate[6] in allowed):
            return "electric"
        return "invalid"
        
    # Region codes setup
    region_codes = set("ABC")
    prague_codes = set("AB")
    
    # Standard passenger car plate check
    if len(plate) == 7:
        if plate[0] in digits and plate[0] != "0":
            region = plate[1]
            if region in region_codes:
                if plate[2] in allowed:
                    c3 = plate[3]
                    
                    # Special rule for Prague
                    if region in prague_codes:
                        pos3_ok = c3 in allowed
                    else:
                        pos3_ok = c3 in digits
                        
                    if pos3_ok:
                        if (plate[4] in digits and 
                            plate[5] in digits and 
                            plate[6] in digits):
                            return "standard"
                            
    # Custom license plate check (falls through if standard fails)
    if len(plate) in (7, 8) and not plate.startswith("EL"):
        return "custom"
        
    return "invalid"
