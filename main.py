def fprime(f):
    # adjust accuracy of calculation
    h = 1E-6
    # return different quotient function
    return lambda x : (f(x+h)-f(x))/h

def abs(x):
    # if positive, return result
    if x >= 0:
        return x
    # if negative, return reflected input
    else:
        return -1*x

def exp(x):
    # adjust accuracy of calculation
    n = 1E6
    # calculate e by definition
    e = (1+(1/n))**n
    # return exponentiation
    return e**x

def newton(x, delta, criteria):
    # used for implementing newtons method
    # loop until result converges
    while True:
        # calculate increment value
        # using given delta function
        dx = delta(x)
        # check if increment is negligible
        if dx < criteria:
            return x
        # otherwise increment answer and continue
        else:
            x -= dx

def inverse(f):
    # adjust accuracy of calculation
    criteria = 1E-6
    # produce derivative function
    dfdx = fprime(f)
    # define the inverse function
    def fi(a):
        # calculate delta function for newton method
        delta = lambda x : (f(x)-a)/dfdx(x)
        # create initial answer by halving input
        x = a/2
        # use newton method to converge
        return newton(x, delta, criteria)
    # return this function
    return fi

def factorial(x):
    # set up initial product for updating
    product = 1
    # loop x times, starting at 1
    for multiplier in range(1,x+1):
        # update the product with each element of range
        product *= multiplier
    # return final result
    return product

def taylor(termfunction, k, x):
    # used for implementing a taylor series
    # set up initial sum for updating
    result = 0
    # loop k times, starting at 0
    for n in range(0,k+1):
        # update the sum with each term of the series
        result += termfunction(n,x)
    # return final result
    return result

def sqrt(a):
    # def square function
    f = lambda x : x**2
    # produce inverse of this function
    # by definition: the square root
    fi = inverse(f)
    # return inverse function
    return fi(a)
        
def ln(a):
    # produce inverse of the exp
    # by definition: the natural log
    fi = inverse(exp)
    # return inverse function
    return fi(a)

def log(base, x):
    # any log base is reduced to ln
    # using 'change of base formula'
    return ln(x)/ln(base)

def sin(x):
    # adjust accuracy of calculation
    k = 10
    # define term function for sin(x)
    tf = lambda n,x : (-1)**n / factorial(2*n+1) * x**(2*n+1)
    # return taylor summation
    return taylor(tf, k, x)

def cos(x):
    # cosx = d/dx(sinx)
    # produce derivative of sin(x)
    dfdx = fprime(sin)
    # return function
    return dfdx(x)

def tan(x):
    # by definition of tan(x)
    return sin(x)/cos(x)

def csc(x):
    # by definition of csc(x)
    return 1/sin(x)

def sec(x):
    # by definition of sec(x)
    return 1/cos(x)

def cot(x):
    # by definition of cot(x)
    return 1/tan(x)