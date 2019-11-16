def fprime(func):
    # adjust accuracy of calculation
    xh = 1e-6
    # return different quotient function
    return lambda x: (func(x + hx) - func(x)) / hx


def fprimeprime(func):
    # get first derivative
    dfdx = fprime(func)
    # return derivative of first derivative
    return fprime(dfdx)


def x_range(xa, xb, dx):
    # calculate size of range
    size = int((xb - xa) / dx) + 1
    # return list of elements incremented by dx
    return [xa + dx * i for i in range(0, size)]


def summer(values):
    # assume sum starts at 0
    summation = 0
    # loop through list and add elements to sum
    for number in values:
        summation += number
    # return sum
    return summation


def average(values):
    # divide sum of list by number of elements in list
    return summer(values) / len(values)


def integral(func, xa, xb):
    # set interval width
    dx = 1e-6
    # calculate sum of function from a to b-dx
    summation = summer([func(x) for x in x_range(xa, xb - dx, dx)])
    # return trapezoidal rule formula
    return dx * (summation + average([func(xa), func(xb)]))


def anti_derivative(func, const=0):
    # return integral with varying b
    # and arbitrary constant
    return lambda x: integral(func, 0, x) + const


def abs(number):
    # if positive, return result
    if number >= 0:
        return number
    # if negative, return reflected input
    else:
        return -1 * number


def floor(xa, xb):
    # assume number goes in 0 times
    counter = 0
    # count up each time multiples of b are under a
    while True:
        if xb * (counter + 1) > xa:
            break
        counter += 1
    # return counter
    return counter


def mod(xa, xb):
    # mod is the difference
    # between a and b*floor(a/b)
    return xa - xb * floor(xa, xb)


def exp(number):
    # adjust accuracy of calculation
    delta = 1e6
    # calculate e by definition
    euler = (1 + (1 / delta)) ** delta
    # return exponentiation
    return euler ** number


def newton(number, delta, criteria):
    # used for implementing newtons method
    # loop until result converges
    while True:
        # calculate increment value
        # using given delta function
        dx = delta(number)
        # check if increment is negligible
        if dx < criteria:
            return number
        # otherwise increment answer and continue
        else:
            number -= dx


def inverse(func):
    # adjust accuracy of calculation
    criteria = 1e-6
    # produce derivative function
    dfdx = fprime(func)
    # define the inverse function
    def fi(xa):
        # calculate delta function for newton method
        delta = lambda x: (func(x) - xa) / dfdx(x)
        # create initial answer by halving input
        number = xa / 2
        # use newton method to converge
        return newton(number, delta, criteria)

    # return this function
    return fi


def factorial(number):
    # set up initial product for updating
    product = 1
    # loop x times, starting at 1
    for multiplier in range(1, number + 1):
        # update the product with each element of range
        product *= multiplier
    # return final result
    return product


def taylor(termfunction, max, number):
    # used for implementing a taylor series
    # set up initial sum for updating
    result = 0
    # loop k times, starting at 0
    for integer in range(0, max + 1):
        # update the sum with each term of the series
        result += termfunction(integer, number)
    # return final result
    return result


def sqrt(xa):
    # def square function
    func = lambda x: x ** 2
    # produce inverse of this function
    # by definition: the square root
    fi = inverse(func)
    # return inverse function
    return fi(xa)


def ln(xa):
    # produce inverse of the exp
    # by definition: the natural log
    fi = inverse(exp)
    # return inverse function
    return fi(xa)


def log(base, xa):
    # any log base is reduced to ln
    # using 'change of base formula'
    return ln(xa) / ln(base)


def sin(xa):
    # calculate equivalent angle
    xa = mod(xa, 2 * 3.14159)
    # adjust accuracy of calculation
    max = 100
    # define term function for sin(x)
    tf = lambda n, x: (-1) ** n / factorial(2 * n + 1) * x ** (2 * n + 1)
    # return taylor summation
    return taylor(tf, max, xa)


def cos(xa):
    # cosx = d/dx(sinx)
    # produce derivative of sin(x)
    dfdx = fprime(sin)
    # return function
    return dfdx(xa)


def tan(xa):
    # by definition of tan(x)
    return sin(xa) / cos(xa)


def csc(xa):
    # by definition of csc(x)
    return 1 / sin(xa)


def sec(xa):
    # by definition of sec(x)
    return 1 / cos(xa)


def cot(xa):
    # by definition of cot(x)
    return 1 / tan(xa)
