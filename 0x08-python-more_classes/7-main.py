#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print("Current print symbol , "  + my_rectangle_1.print_symbol)
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print("Current print symbol , "  + my_rectangle_2.print_symbol)
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print("Current print symbol , "  + my_rectangle_3.print_symbol)
print(my_rectangle_3)

print("--")

print(my_rectangle_3.print_symbol)
