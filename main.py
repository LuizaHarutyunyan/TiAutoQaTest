from NotTriangleException import NotTriangleException
from Point import Point
import math


def input_dot_data():
    a_x = int(input("Enter coordinate x of dot A: "))
    a_y = int(input("Enter coordinate y of dot A: "))
    b_x = int(input("Enter coordinate x of dot B: "))
    b_y = int(input("Enter coordinate y of dot B: "))
    c_x = int(input("Enter coordinate x of dot C: "))
    c_y = int(input("Enter coordinate y of dot C: "))
    a = Point(a_x, a_y)
    b = Point(b_x, b_y)
    c = Point(c_x, c_y)
    validate_triangle(a, b, c)

    print_triangle_data(a, b, c)

def validate_triangle(a, b, c):
    if (a.x*(b.y-c.y)+ b.x*(c.y-a.y)+c.x+(a.y-b.y)):
        raise Exception(NotTriangleException(), "Given points are in one line,")

def print_triangle_data(a, b, c):
    a_b = get_line_length_with_two_points(a, b)
    a_c = get_line_length_with_two_points(a, c)
    c_b = get_line_length_with_two_points(c, b)
    print(f"Length of AB is: '{a_b}'")
    print(f"Length of AC is: '{a_c}'")
    print(f"Length of CB is: '{c_b}'")
    print_triangle_type(a_b, c_b, a_c)
    perimeter =  a_b + a_c + c_b
    print(f"Perimeter: '{perimeter}'")
    print("Parity number in range from 0 to triangle perimeter:")
    perimeter_of_triangle(perimeter)

def get_line_length_with_two_points(first_point, second_point):
    return math.sqrt((first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2)


def print_triangle_type(a_b, c_b, a_c):
    equilateral_triangle(a_b, c_b, a_c)
    isoscales_triangle(a_b, c_b, a_c)
    right_triangle(a_b, c_b, a_c)

def equilateral_triangle(first_line_length, second_line_length, third_line_length):
    if first_line_length == second_line_length == third_line_length:
        print("Triangle is Equilateral")
    else:
        print("Triangle is Not Equilateral")

def isoscales_triangle(first_line_length, second_line_length, third_line_length):
    if first_line_length == second_line_length != third_line_length or first_line_length == third_line_length != second_line_length or second_line_length == third_line_length != first_line_length:
        print("Triangle is Isoscales")
    else:
        print("Triangle is Not Isoscales")

def right_triangle(first_line_length, second_line_length, third_line_length):
    right_triangle1 = math.sqrt((first_line_length) ** 2 + (second_line_length) ** 2)
    right_triangle2 = math.sqrt((first_line_length) ** 2 + (third_line_length) ** 2)
    right_triangle3 = math.sqrt((second_line_length) ** 2 + (third_line_length) ** 2)
    if first_line_length == right_triangle3 or third_line_length == right_triangle1 or second_line_length == right_triangle2:
        print("Triangle is Right")
    else:
        print("Triangle is Not Right")

def perimeter_of_triangle(perimeter):
    for i in range(0, int(perimeter)):
        if i % 2 == 0:
            print(i)


input_dot_data()
