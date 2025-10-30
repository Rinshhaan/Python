# ALGORITHM
# STEP 1: Start.
# STEP 2: 'Define' functions for calculating surface area and volume. 
# STEP 3: 'Input' radius and height of the cylinder.
# STEP 4: 'Call' the functions with inputs and display results surface area=2*PI*R*(R+H) and volume=PI*R*R*H.
# STEP 5: Stop

import math # to use pi

def surface_area(radius,height):
    return 2*math.pi*radius*(radius+height) #2πr(r+h)

def volume(radius,height):
    return math.pi*radius**2*height #πr^2h

radius = float(input("Enter the radius of cylinder: "))
height = float(input("Enter the height of cylinder: "))

sa = surface_area(radius,height)
volume = volume(radius,height)

print(f"surface area = {sa:.2f}")
print(f"volume = {volume:.2f}")
