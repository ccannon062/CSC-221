import math

x1,y1 = eval(input("Please enter the first coordinate pair without parentheses: "))
x2,y2 = eval(input("Please enter the second coordinate pair without parentheses: "))

slope = y2 - y1 / x2 - x1
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("The slope is:",round(slope, 3))
print("The distance between the two points is:",round(distance, 3))
