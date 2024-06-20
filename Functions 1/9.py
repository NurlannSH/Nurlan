import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

radius = 5
print(f"Volume of sphere with radius {radius}: {sphere_volume(radius)}")
