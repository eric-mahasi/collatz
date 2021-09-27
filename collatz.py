"""The Collatz Conjecture is a problem in mathematics that performs two operations, in succession, on a number depending
on its parity. If the number is even, it is divided by two, otherwise if it is odd, the number is multiplied by three
and one is added. These steps are repeated until we are arrive at one."""


# TODO find out why number takes a float type, yet it is initially an int
# TODO add functionality to allow user to keep entering wrong numbers till they match the input criteria


def collatz():
    """Repeatedly check if number is even, number/2, if number is odd, number * 3 + 1  until number == 1"""
    number = int(input("Enter a number: "))
    counter = 0
    while number != 1:
        if number <= 0:
            print("Please enter a number greater than 1.")
            break
        elif number % 2 == 0:
            number /= 2
            print(number)
        else:
            number = (number * 3) + 1
            print(number)
        counter += 1
    print(counter, "steps taken to reach 1")


if __name__ == '__main__':
    collatz()
