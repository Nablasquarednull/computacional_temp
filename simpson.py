def func(x):
    return 1
def simpson(a,b,N,func):
    h = (b-a)/N
    sum1 = func(a) +func(b)
    for i in range(1,N/2,1):
        sum1 += 4*func(a +(2i-1)*h)
    for i in range(1,N/2 -1,1):
        sum1 += 2*func(a + 2*i*h)
    result = (h/3)*sum1
    return result
simson(0,1,100,func)
