import math

def area_of_polygon(number_of_sides, length_of_sides):
    area = (1.0/4.0)*number_of_sides*length_of_sides*length_of_sides/(math.tan(math.pi/number_of_sides))
    return area

print area_of_polygon(5, 7)
print area_of_polygon(7, 3)
