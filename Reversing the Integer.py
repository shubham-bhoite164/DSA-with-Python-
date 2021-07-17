# Our task is to design an efficient algorithm to reverse the integer
# ex :- i/p =1234 , o/p =4321

# we are after the last digit in every iteration
# we can get it with modulo operator: the last digit is the remainder when dividing by 10
# we have to make sure that we remove that digit from the original number
# so we just have to divide the original number by 10 !!!

def reverse_integer(n):

    reversed_integer = 0
    remainder = 0

    while n>0:
        remainder = n % 10
        reversed_integer = reversed_integer*10 + remainder
        n = n//10    # we don't want decimal point

    return reversed_integer

if __name__ == '__main__':
    print(reverse_integer(1234))

