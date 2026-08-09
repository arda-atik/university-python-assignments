import math

# Read the ship's speed
speed = float(input())

# Constants for Earth and Tropic of Cancer
radius = 6378
phi = 23.5

# Calculate radius of the parallel and total distance
r = radius * math.cos(math.radians(phi))
distance = 2 * math.pi * r

# Calculate time in days and hours
time = distance // speed
days = int(time // 24)
hours = round(time % 24)

# Print the exact format required
print(days, 'd', hours, 'hrs')
