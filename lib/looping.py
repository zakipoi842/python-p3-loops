#!/usr/bin/env python3

def happy_new_year():
    counter = 10

    while counter > 0:
        print(counter)
        counter -= 1

    print("Happy New Year!")

happy_new_year()
    

def square_integers(intlist):
    squaredlist = []

    for num in intlist:
        squaredlist.append(num ** 2)

    return squaredlist

print(square_integers([1, 2, 3, 4, 5]))
print(square_integers([-1, -2, -3, -4, -5]))


def fizzbuzz(num=None):
    # If no argument is provided, print 1 to 100
    if num is None:
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    else:
        # Handle single number as before
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return num

# This will print 1-100 as the test expects
fizzbuzz()