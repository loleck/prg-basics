import math

# Read the observer height in meters from the keyboard
height = float(input("Enter the height in meters: "))

# Formula for distance to the horizon in kilometers
distance = 3.57 * math.sqrt(height)

print(f"The distance to the horizon is {distance:.2f} km.")

# Example calculations:
# Beach / sea level (assume a height of 1.7 m)
beach_height = 1.7
beach_distance = 3.57 * math.sqrt(beach_height)
print(f"At a height of {beach_height} m, the horizon is {beach_distance:.2f} km away.")

# Hotel window at 20 m
window_height = 20
window_distance = 3.57 * math.sqrt(window_height)
print(f"At a height of {window_height} m, the horizon is {window_distance:.2f} km away.")
