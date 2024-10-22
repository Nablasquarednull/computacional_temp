from numpy import empty,arange,exp,real,pi,loadtxt
from numpy.fft import rfft,irfft
from matplotlib.pyplot import plot,show
# 1D DCT Type-II
def dct(y):
    N = len(y)
    y2 = empty(2*N,float)
    for n in range(N):
        y2[n] = y[n]
        y2[2*N-1-n] = y[n]

    c = rfft(y2)
    phi = exp(-1j*pi*arange(N)/(2*N))
    return real(phi*c[:N])

# 1D inverse DCT Type-II
def idct(a):
    N = len(a)
    c = empty(N+1,complex)

    phi = exp(1j*pi*arange(N)/(2*N))
    c[:N] = phi*a
    c[N] = 0.0
    return irfft(c)[:N]
#----------------------------------------
#Load the file
dow = loadtxt('dow2.txt')
#smooth the signal
c = rfft(dow)
ind = round(0.02*len(dow))
cnew = empty(len(c),complex)
cnew[:ind] = c[:ind]
cnew[ind:]=0
#ifft
dow_new = irfft(cnew)

#plot the signal
plot(dow)
plot(dow_new,color='red')
show()

