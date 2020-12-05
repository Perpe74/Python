import math

class ComplexNumber:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Method that returns complete form of complex number
    def val(self):
        return '{} + ({})j'.format(self.real, self.imag)

    # Method adding two complex numbers
    def sum(self, other):
        return ComplexNumber(self.real + other.real,
                       self.imag + other.imag)

    # Method subtracting two complex numbers
    def sub(self, other):
        return ComplexNumber(self.real - other.real,
                       self.imag - other.imag)

    # Method multiply two complex numbers
    def mul(self, other):
        return ComplexNumber(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)

    # Method returns absolute value of complex number
    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)


def complex_parse(string):
    arr = string.split("+")
    real_str = arr[0]
    imag_str = arr[1].strip("i")
    return int(real_str), int(imag_str)


operation = int(input("Give an operation to perform\n"
                  "1 - add complex numbers\n"
                  "2 - subract complex numbers\n"
                  "3 - multipliacte complex numbers\n"
                  "4 - abs of complex number\n"))

a = input("Give first value in format x+yi\n")
real_a, imag_a = complex_parse(a)
complex_a = ComplexNumber(real_a, imag_a)

if operation != 4:
    b = input("Give second value in format x+yi\n")
    real_b, imag_b = complex_parse(b)
    complex_b = ComplexNumber(real_b, imag_b)

if operation == 1:
    result = complex_a.sum(complex_b)
elif operation == 2:
    result = complex_a.sub(complex_b)
elif operation == 3:
    result = complex_a.mul(complex_b)
elif operation == 4:
    result = complex_a.abs()

if  operation != 4:
    print("{}+{}i".format(result.real, result.imag))
else:
    print(result)
