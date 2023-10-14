import math

def calculate_circle_properties(radius):
    circumference = 2 * math.pi * radius

    area = math.pi * radius**2

    return circumference, area

radius = float(input("Enter the radius of the circle: "))

circumference, area = calculate_circle_properties(radius)

print(f"The circumference of the circle with radius {radius} is: {circumference:.2f}")
print(f"The area of the circle with radius {radius} is: {area:.2f}")
