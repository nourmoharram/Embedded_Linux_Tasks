'''
Task description: Write a Python program which accepts the radius of a circle from the user 
and compute the area.

'''

def Area_of_Circle(Radius):
    Area = 3.14 * Radius**2
    print(Area)

radius = float(input("Enter the radius of the circle: "))
Area_of_Circle(radius)
