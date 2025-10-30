import numpy as np
hand = np.array([17,15,19,17,21])
height = [150,154,169,172,175]

n = len(hand)

sum_x = sum(hand)
print(f"sm x:{sum_x}")

sum_y = sum(height)
print(f"sm y:{sum_y}")

sum_x2 = sum([x**2 for x in hand])
print(f"sm x^2:{sum_x2}")

sum_y2 = sum(y**2 for y in height)
print(f"sm y^2:{sum_y2}")

sum_xy = sum(x*y for x,y in zip(hand,height))
print(f"sm xy:{sum_xy}")

numerator = n * sum_xy - (sum_x * sum_y)
denominator = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))**0.5


if denominator == 0:
    R = 0
else:
    R = numerator / denominator
    print("Correlation Coefficient R:",round(R,3)) # 3 decimal places