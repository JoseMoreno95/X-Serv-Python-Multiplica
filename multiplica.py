#!/usr/bin/python3

numbers = list(range(1,11))
for first_number in numbers:
    print ("Tabla del " + str(first_number))
    for second_number in numbers:
        print (str (first_number) + "x" + str(second_number) + "=" + str(first_number*second_number))
