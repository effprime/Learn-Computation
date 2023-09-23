def fprime(func):
    # adjust accuracy of calculation
    h = 1e-6
    # return different quotient function
    return lambda x: (func(x + h) - func(x)) / h


def fprimeprime(func):
    # get first derivative
    dfdx = fprime(func)
    # return derivative of first derivative
    return fprime(dfdx)


def x_range(a, b, dx):
    # calculate size of range
    size = int((b - a) / dx) + 1
    # return list of elements incremented by dx
    return [a + dx * i for i in range(0, size)]


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


def integral(func, a, b):
    # set interval width
    dx = 1e-6
    # calculate sum of function from a to b-dx
    summation = summer([func(x) for x in x_range(a, b - dx, dx)])
    # return trapezoidal rule formula
    return dx * (summation + average([func(a), func(b)]))


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


def floor(a, b):
    # assume number goes in 0 times
    counter = 0
    # count up each time multiples of b are under a
    while True:
        if b * (counter + 1) > a:
            break
        counter += 1
    # return counter
    return counter


def mod(a, b):
    # mod is the difference
    # between a and b*floor(a/b)
    return a - b * floor(a, b)


def exp(x):
    # adjust accuracy of calculation
    delta = 1e6
    # calculate e by definition
    euler = (1 + (1 / delta)) ** delta
    # return exponentiation
    return euler ** x


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
    def fi(x):
        # calculate delta function for newton method
        delta = lambda x: (func(x) - x) / dfdx(x)
        # create initial answer by halving input
        number = x / 2
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


def sqrt(x):
    # def square function
    func = lambda x: x ** 2
    # produce inverse of this function
    # by definition: the square root
    fi = inverse(func)
    # return inverse function
    return fi(x)


def ln(x):
    # produce inverse of the exp
    # by definition: the natural log
    fi = inverse(exp)
    # return inverse function
    return fi(x)


def log(base, x):
    # any log base is reduced to ln
    # using 'change of base formula'
    return ln(x) / ln(base)


def sin(x):
    # calculate equivalent angle
    x = mod(x, 2 * 3.14159)
    # adjust accuracy of calculation
    max = 100
    # define term function for sin(x)
    tf = lambda n, x: (-1) ** n / factorial(2 * n + 1) * x ** (2 * n + 1)
    # return taylor summation
    return taylor(tf, max, x)


def cos(x):
    # cosx = d/dx(sinx)
    # produce derivative of sin(x)
    dfdx = fprime(sin)
    # return function
    return dfdx(x)


def tan(x):
    # by definition of tan(x)
    return sin(x) / cos(x)


def csc(x):
    # by definition of csc(x)
    return 1 / sin(x)


def sec(x):
    # by definition of sec(x)
    return 1 / cos(x)


def cot(x):
    # by definition of cot(x)
    return 1 / tan(x)

if __name__ == "__main__":
    print(cot(1.5))