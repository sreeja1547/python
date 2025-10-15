import numpy as np

# Create two sample arrays
speed_car1 = np.array([45, 60, 72, 90, 55, 80])
speed_car2 = np.array([50, 60, 70, 85, 58, 78.000000001])

print("Speed Car 1:", speed_car1)
print("Speed Car 2:", speed_car2)

# Element-wise comparisons
print("\nGreater than:", speed_car1 > speed_car2)
print("Greater than or equal to:", speed_car1 >= speed_car2)
print("Less than:", speed_car1 < speed_car2)
