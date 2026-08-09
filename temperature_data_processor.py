import os

def process_temperatures(in_filename, out_filename, sort="avg"):
    """
    Reads a temperature data file, sorts the entries based on the specified column,
    and writes them to a new file. Handles I/O and formatting errors.
    """
    data = []
    
    # Read the input file
    try:
        file = open(in_filename, "r")
    except:
        return -1
        
    lines = file.readlines()
    file.close()
    
    if len(lines) == 0:
        return -2
        
    header = lines[0].strip()
    
    # Determine sorting index
    if sort == "max":
        sort_index = 4
    elif sort == "min":
        sort_index = 5
    else:
        sort_index = 3
        
    # Parse and validate the data
    for i in range(1, len(lines)):
        line = lines[i].strip()
        parts = line.split(",")
        
        if len(parts) != 6:
            return -2
            
        try:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
        except:
            return -2
            
        if year <= 0 or month <= 0 or day <= 0:
            return -2
            
        try:
            avg = float(parts[3])
            max_t = float(parts[4])
            min_t = float(parts[5])
        except:
            return -2
            
        # Assign the sorting key
        if sort_index == 3:
            key = avg
        elif sort_index == 4:
            key = max_t
        else:
            key = min_t
            
        data.append([key, line])
        
    # Sort the data based on the selected key
    data.sort()
    
    # Write the sorted data to the output file
    try:
        out = open(out_filename, "w")
        out.write(header + "\n")
        for i in range(len(data)):
            out.write(data[i][1] + "\n")
        out.close()
    except:
        # Clean up if an error occurs during writing
        if os.path.exists(out_filename):
            os.remove(out_filename)
        return -1
        
    return 0
