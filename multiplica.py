#!/usr/bin/python3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for first_number in numbers:
    print ("Tabla del " + str(first_number))
    for second_number in numbers:
        print (str (first_number) + "x" + str(second_number) + "=" + str(first_number*second_number))
