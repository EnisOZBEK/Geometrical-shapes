# This program is made by Enis ÖZBEK to calculate area, volume, perimeter etc. of the geometrical shapes!

import math

# ------------------------------------------------------------------------------------------------------------------------------------

def clear():
    print(chr(27) + "[2J")

# ------------------------------------------------------------------------------------------------------------------------------------

def square():
    side = int(input("\nType the side of the square: "))

    perimeter = side * 4
    area = side * side

    print(f"\nSide: {side}, Area: {area}, Perimeter: {perimeter}")

def rectangle():
    shortside = int(input("\nType the short side of the rectangle: "))
    longside = int(input("\nType the long side of the rectangle: "))

    perimeter = 2 * (shortside + longside)
    area = shortside * longside

    print(f"\nShort Side: {shortside}, Long Side: {longside}, Area: {area}, Perimeter: {perimeter}")

def circle():
    radius = int(input("Type the radius of the circle: "))

    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius

    print(f"\nRadius: {radius}, Perimeter: {perimeter}, Area: {area}")

def triangle():
    height = int(input("Type the height of the triangle: "))
    base = int(input("Type the base of the triangle: "))
    first_side = int(input("Type the first side of the triangle: "))
    second_side = int(input("Type the second side of the triangle: "))

    perimeter = base + first_side + second_side
    area = (base * height) / 2

    print(f"\nHeight: {height}, Base: {base}, First Side: {first_side}, Second Side: {second_side}, Perimeter: {perimeter}, Area: {area}")

def cube():
    side = int(input("Type the side of the cube: "))

    perimeter = 12 * side
    area = 6 * (side ** 2)
    volume = side * side * side

    print(f"\nSide: {side}, Perimeter: {perimeter}, Area: {area}, Volume: {volume}")

def sphere():
    radius = int(input("Type the radius of the sphere: "))

    area = 4 * math.pi * radius ** 2
    volume = 4 / 3 * math.pi * radius * radius * radius

    print(f"\nRadius: {radius}, Area: {area}, Volume: {volume}")

def cylinder():
    radius = int(input("Type the radius of cylinder: "))
    height = int(input("Type the height of cylinder: "))

    area = 2 * math.pi * radius * radius + 2 * math.pi * radius * height
    volume = math.pi * radius * height

    print(f"\nRadius: {radius}, Height: {height}, Area: {area}, Volume: {volume}")

def cone():
    radius = int(input("Type the radius of the cone: "))
    height = int(input("Type the height of the cone: "))

    area = (math.pi * radius * radius) + (math.pi * radius)
    volume = (1.0/3) * math.pi * radius * radius * height

    print(f"\nRadius: {radius}, Height: {height}, Area: {area}, Volume: {volume}")

def square_prism():
    side = int(input("Type the side of the square prism: "))
    height = int(input("Type the height of the square prism: "))

    area = (2 * (side * side)) + (4 * side * height)
    volume = side * side * height

    print(f"\nSide: {side}, Height: {height}, Area: {area}, Volume: {volume}")

def rectangular_prism():
    shortside = int(input("Type the short side of the rectangle prism: "))
    longside = int(input("Type the long side of the rectangle prism: "))
    height = int(input("Type the height of the rectangle prism: "))

    area = 2 * (shortside * longside + shortside * height + longside * height)
    volume = shortside * longside * height

    print(f"\nShort Side: {shortside}, Long Side: {longside}, Height: {height}, Area: {area}, Volume: {volume}")

def triangular_prism():
    first_side = int(input("Type the first side of the triangular prism: "))
    second_side = int(input("Type the second side of the triangular prism: "))
    third_side = int(input("Type the third side of the triangular prism: "))
    height_of_base = int(input("Type the height of the base of prism: "))
    height_of_prism = int(input("Type the height of the triangular prism: "))

    area = 2 * (first_side * height_of_base) + height_of_prism * (first_side + second_side + third_side)
    volume = first_side * height_of_base * height_of_prism

    print(f"\nFirst Side: {first_side}, Second Side: {second_side}, Third Side: {third_side}, Height Of Base: {height_of_base}, Height Of Prism: {height_of_prism}, Area: {area}, Volume: {volume}")

def square_pyramid():
    side = int(input("Type the side of the base: "))
    height = int(input("Type the height of the pyramid: "))

    area = math.pow(side * side + side (math.sqrt(side * side + 4 * height * height)))
    volume = ((side * side) * height) / 3

    print(f"Side: {side}, Height: {height}, Area: {area}, Volume: {volume}")

def rectangular_pyramid():
    shortside = int(input("Type the short side of the base: "))
    longside = int(input("Type the long side of the base: "))
    height = int(input("Type the height of the pyramid: "))

    area = math.pow(shortside * longside + shortside (math.sqrt(longside * shortside + 4 * height * height)))
    volume = ((shortside * longside) * height) / 3

    print(f"Short Side: {shortside}, Long Side: {longside}, Height: {height}, Area: {area}, Volume: {volume}")

def triangular_pyramid():
    first_side = int(input("Type the first side of the triangular pyramid: "))
    second_side = int(input("Type the second side of the triangular pyramid: "))
    third_side = int(input("Type the third side of the triangular pyramid: "))
    height_of_base = int(input("Type the height of the base of pyramid: "))
    height_of_pyramid = int(input("Type the height of the triangular pyramid: "))

    area = (first_side * height_of_base) + height_of_pyramid * (first_side + second_side + third_side) / 3
    volume = (first_side * height_of_base * height_of_pyramid) / 3

    print(f"\nFirst Side: {first_side}, Second Side: {second_side}, Third Side: {third_side}, Height Of Base: {height_of_base}, Height Of Pyramid: {height_of_pyramid}, Area: {area}, Volume: {volume}")

# ------------------------------------------------------------------------------------------------------------------------------------

again = "y"

while again == "y":
    clear()

    choice = int(input("\nChose the dimension: \n\nPress ---> 1 for 2D shapes! \nPress ---> 2 for 3D shapes!\n\nChoice: -> "))

    if choice == 1:
        clear()

        choice_2D = int(input("<---> 2D Shapes Menu <---> \n\nPress ---> 1 for SQUARE! \nPress ---> 2 for RECTANGLE! \nPress ---> 3 for CIRCLE! \nPress ---> 4 for TRIANGLE! \n\nChoice: -> "))

        if choice_2D == 1:
            clear()
            square()

            again = input("\nDo you want to calculate again ? (y, n): ")
            
            if again == "n":
                clear()

                print("\nThanks for trusting our service!")

                exit

        elif choice_2D == 2:
            clear()
            rectangle()

            again = input("\nDo you want to calculate again ? (y, n): ")
            
            if again == "n":
                clear()

                print("\nThanks for trusting our service!")

                exit

        elif choice_2D == 3:
            clear()
            circle()

            again = input("\nDo you want to calculate again ? (y, n): ")
            
            if again == "n":
                clear()

                print("\nThanks for trusting our service!")

                exit

        elif choice_2D == 4:
            clear()
            triangle()

            again = input("\nDo you want to calculate again ? (y, n): ")
            
            if again == "n":
                clear()

                print("\nThanks for trusting our service!")

                exit

# ------------------------------------------------------------------------------------------------------------------------------------

    if choice == 2:
        clear()

        choice_3D = int(input("<---> 3D Shapes Menu <---> \n\nPress ---> 1 for CUBE! \nPress ---> 2 for Sphere! \nPress ---> 3 for CYLINDER! \nPress ---> 4 for CONE! \nPress ---> 5 for PRISM MENU! \nPress ---> 6 for PYRAMID MENU! \n\nChoice: -> "))

        if choice_3D == 1:
            clear()
            cube()

            again = input("\nDo you want to calculate again ? (y, n): ")
            
            if again == "n":
                clear()

                print("\nThanks for trusting our service!")

                exit

        elif choice_3D == 2:
            clear()
            sphere()

            again = input("\nDo you want to calculate again ? (y, n): ")
            
            if again == "n":
                clear()

                print("\nThanks for trusting our service!")

                exit

        elif choice_3D == 3:
            clear()
            cylinder()

            again = input("\nDo you want to calculate again ? (y, n): ")
            
            if again == "n":
                clear()

                print("\nThanks for trusting our service!")

                exit

        elif choice_3D == 4:
            clear()
            cone()

            again = input("\nDo you want to calculate again ? (y, n): ")
            
            if again == "n":
                clear()
                print("\nThanks for trusting our service!")
                exit

# ------------------------------------------------------------------------------------------------------------------------------------

        elif choice_3D == 5:
            clear()

            choice_prism = int(input("\nPress ---> 1 for SQUARE PRISM! \nPress ---> 2 for RECTANGULAR PRISM! \nPress ---> 3 for TRIANGULAR PRISM! \n\nChoice: -> "))

            if choice_prism == 1:
                clear()
                square_prism()

                again = input("\nDo you want to calculate again ? (y, n): ")
            
                if again == "n":
                    clear()

                    print("\nThanks for trusting our service!")

                    exit

            elif choice_prism == 2:
                clear()
                rectangular_prism()

                again = input("\nDo you want to calculate again ? (y, n): ")
            
                if again == "n":
                    clear()

                    print("\nThanks for trusting our service!")

                    exit

            elif choice_prism == 3:
                clear()
                triangular_prism()

                again = input("\nDo you want to calculate again ? (y, n): ")
            
                if again == "n":
                    clear()

                    print("\nThanks for trusting our service!")

                    exit

# ------------------------------------------------------------------------------------------------------------------------------------

        elif choice_3D == 6:
            clear()

            choice_pyramid = int(input("\nPress ---> 1 for SQUARE PYRAMID! \nPress ---> 2 for RECTANGULAR PYRAMID! \nPress ---> 3 for TRIANGULAR PYRAMID! \n\nChoice: -> "))

            if choice_pyramid == 1:
                clear()
                square_pyramid()

                again = input("\nDo you want to calculate again ? (y, n): ")
            
                if again == "n":
                    clear()

                    print("\nThanks for trusting our service!")

                    exit

            elif choice_pyramid == 2:
                clear()
                rectangular_pyramid()

                again = input("\nDo you want to calculate again ? (y, n): ")
            
                if again == "n":
                    clear()

                    print("\nThanks for trusting our service!")

                    exit

            elif choice_pyramid == 3:
                clear()
                triangular_pyramid()

                again = input("\nDo you want to calculate again ? (y, n): ")
            
                if again == "n":
                    clear()

                    print("\nThanks for trusting our service!")

                    exit