"""
John 21:11
 ... It was full of large fish, 153, but even with so many the net was not torn.
"""

"""
153 is the 17th triangular number 153 = 1 + 2 + 3 + ... + 17

153 is a 3-digit Pluperfect Digital Invariant
153 = 1^3 + 5^3 + 3^3    (each digit to the power of three then sum up)

For every positive number that is a multiple of 3. If we do the following to it:
1. separate out all the digits
2. do cubic summation on all digits to obtain a new number
3. repeat 1 and 2 for the new number
It will always converge to 153.
"""

number = 1236933    # Change this to any positive multiple of three 

def converge_to_153(number):
    if type(number) != int or number <= 0 or number % 3 != 0:
        print("{} is not a positive multiple of three.".format(number))
        return

    iteration = 0
    while number != 153:
        iteration += 1
        print("Iteration {:2d} : number is {}".format(iteration, number))
        nxt = 0
        while number != 0:
            nxt += (number % 10)**3
            number //= 10
        number = nxt
    print("Iteration {:2d} : number is {}".format(iteration+1, number))
    return

converge_to_153(number)
