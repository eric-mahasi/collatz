"""The Collatz Conjecture is a problem in mathematics that performs two operations, in succession, on a number depending
on its parity. If the number is even, it is divided by two, otherwise if it is odd, the number is multiplied by three
and one is added. These steps are repeated until we are arrive at one."""


# TODO find out why number takes a float type, yet it is initially an int
# TODO add functionality to allow user to keep entering wrong numbers till they match the input criteria


class Collatz(object):

    def __init__(self):
        self.number = 0
        self.counter = 0

    def collatz(self):
        """Repeatedly check if number is even, number/2, if number is odd, number * 3 + 1  until number == 1"""
        self.number = int(input("Enter a number: "))
        while self.number != 1:
            if self.number <= 0:
                print("Please enter a number greater than 1.")
                break
            elif self.number % 2 == 0:
                self.number /= 2
                print(self.number)
            else:
                self.number = (self.number * 3) + 1
                print(self.number)
            self.counter += 1


# Objects for debugging
a = Collatz()
a.collatz()
print(a.counter, "steps taken to reach 1")
