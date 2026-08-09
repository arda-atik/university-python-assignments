import math

# Sabit Değerler (Constants)
EARTH_RADIUS_KM = 6378
LATITUDE_DEG = 23.5

# Kullanıcıdan hızı al
speed = float(input())

# Paralel yarıçapını ve toplam mesafeyi hesapla
r = EARTH_RADIUS_KM * math.cos(math.radians(LATITUDE_DEG))
distance = 2 * math.pi * r

# Süreyi hesapla (Gün ve Saat olarak ayır)
time = distance / speed
days = int(time // 24)
hours = round(time % 24)

print(f"{days} d {hours} hrs")
