def fprime(f):
    h = 1E-6
    return lambda x : (f(x+h)-f(x))/h

def abs(x):
    if x >= 0:
        return x
    else:
        return -1*x

def newton(x, delta, criteria):
    # used for implementing newtons method
    while True:
        dx = delta(x)
        if dx < criteria:
            return x
        else:
            x -= dx

def exp(x):
    n = 1E6
    e = (1+(1/n))**n
    return e**x

def sqrt(a):
    criteria = 1E-6
    x = a/2
    delta = lambda x : (x**2-a)/(2*x)
    return newton(x, delta, criteria)
        
def ln(a):
    criteria = 1E-6
    x = a/2
    delta = lambda x : 1-(a/exp(x))
    return newton(x, delta, criteria)

def log(base, x):
    return ln(x)/ln(base)

def factorial(x):
    product = 1
    for multiplier in range(1,x+1):
        product *= multiplier
    return product

def taylor(termfunction, k, x):
    # used for implementing a taylor series
    result = 0
    for n in range(0,k+1):
        result += termfunction(n,x)
    return result

def sin(x):
    k = 10
    tf = lambda n,x : (-1)**n / factorial(2*n+1) * x**(2*n+1)
    return taylor(tf, k, x)

def cos(x):
    # cosx = d/dx(sinx)
    dfdx = fprime(sin)
    return dfdx(x)

def tan(x):
    return sin(x)/cos(x)

def csc(x):
    return 1/sin(x)

def sec(x):
    return 1/cos(x)

def cot(x);
    return 1/tan(x)