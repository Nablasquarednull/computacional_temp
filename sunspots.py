#Ricardo Rodriguez Pineda 169048
#Jose Emilio Pacheco Cuan 172211
#Andrés Alvarez Rodriguez 170060
import numpy as np
from numpy import fft,loadtxt, empty_like,savetxt, square, where
from matplotlib.pyplot import plot,show,scatter

def main():
    #-----Ploting the sunspots file---------------#
    sspot_number = loadtxt('sunspots.txt',usecols=1)
    month = loadtxt('sunspots.txt',usecols=0)
    scatter(month,sspot_number,marker = '.')
    show()
    #ESTIMATE:
    #After seeing the graph it looks like the length of a cycle lasts
    #somewere around 140-170 months
    #-------getting the DFT coeffs of the sunspot data-------#
    FDT_coeff = fft.rfft(sspot_number)
    coeff_squared = empty_like(FDT_coeff) #geting the modulus squared of the coeffs
    for i in range(len(FDT_coeff)):
        coeff_squared[i] = square(abs(FDT_coeff[i]))
    plot(coeff_squared)
    savetxt('ayudaaa.txt',coeff_squared)
    show()
    #------find the value of k, to which the peak corresponds, and find the period of the sine wave that mayorly contributes to the sun cycle-----#
    coeff_squared[0] = 0
    max_coeff = max(coeff_squared)
    max_k = where( coeff_squared == max_coeff)
    print ("The corresponding value of k that contributes most to c_k is: ", max_k[0])
    period =2*np.pi*max_k[0]
    print("The period of the corresponding sine wave is", period )




main()

