import math

EARTH_RADIUS_KM = 6378
LATITUDE_DEG = 23.5

speed = float(input())

r = EARTH_RADIUS_KM * math.cos(math.radians(LATITUDE_DEG))
distance = 2 * math.pi * r

time = distance / speed
days = int(time // 24)
hours = round(time % 24)

print(f"{days} d {hours} hrs")
