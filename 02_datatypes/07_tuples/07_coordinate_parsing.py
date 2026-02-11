"""
Demonstrates parsing a string into a coordinate tuple.
"""

from typing import Tuple

def parse_coordinates(coord_string: str) -> Tuple[float, float]:
    parts = coord_string.split(",")
    return float(parts[0].strip()), float(parts[1].strip())

if __name__ == "__main__":
    coords = "40.7128,-74.0060"
    lat, lon = parse_coordinates(coords)
    print(f"Latitude: {lat}, Longitude: {lon}")
