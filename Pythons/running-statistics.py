import numpy as np  # To use array of numbers instead of list
import matplotlib.pyplot as plt # To plot graphics
import random # To generate random numbers
from statistics import mean # To use mean from statistics package
import math # To use log and pi methods.
from scipy.stats import norm # To show gaussian curve # pip3 install scipy   

# Lets import the data, for now Medidas_2022_02_03_09-57-35.txt
# First line must be desconsidered
# Time stamp ; Contador ;  ; RSSI_DL  ;  ;

RSSIdl = np.loadtxt(open("Medidas_2022_02_03_09-57-35.txt", mode='r').readlines()[:-1], skiprows=1, delimiter=';', usecols=[3])
## Code above just worked after deleting the last row, so we used the .readlines()[:-1] command

print(type(RSSIdl))
print(RSSIdl)     

plt.figure(1)
plt.subplot(2,2,1) 
plt.plot(RSSIdl) # Prepare the plot to show the randon values
plt.xlabel('Time domain') 
plt.ylabel('RSSI') 
plt.title('RSSI DL 2022 - 1322 RSSIs')#'Random values, normal distribution')

plt.subplot(2,2,2)
plt.hist(RSSIdl, bins=20)

print('Mean: ' + str(np.float64(np.mean(RSSIdl)))) # It returns a <numpy.float64> type, then is converted to string
print('Standard deviation: ' + str(np.float64(np.std(RSSIdl)))) # Same as before

############################

RSSIdl = np.loadtxt(open("Medidas_2021_12_06_09-22-49.txt", mode='r').readlines()[:-1], skiprows=1, delimiter=';', usecols=[3])
## Code above just worked after deleting the last row, so we used the .readlines()[:-1] command

print(type(RSSIdl))
print(RSSIdl)     

plt.figure(2)
plt.subplot(2,2,1) 
plt.plot(RSSIdl) # Prepare the plot to show the randon values
plt.xlabel('Time domain') 
plt.ylabel('RSSI') 
plt.title('RSSI DL 2021 - 3921 RSSIs')#'Random values, normal distribution')

plt.subplot(2,2,2)
plt.hist(RSSIdl, bins=20)

print('Mean: ' + str(np.float64(np.mean(RSSIdl)))) # It returns a <numpy.float64> type, then is converted to string
print('Standard deviation: ' + str(np.float64(np.std(RSSIdl)))) # Same as before



# The curve (not a gaussian)

#x = np.linspace(np.mean(RSSIdl) - 4 * np.std(RSSIdl), np.mean(RSSIdl) + 4 * np.std(RSSIdl), 100)  # Valores de RSSIdl para a distribuição gaussiana
#y = norm.pdf(x, np.mean(RSSIdl), np.std(RSSIdl))

#plt.subplot(4,2,4)
#plt.twinx() # To plot over the histogram, but with different scale for Y
#plt.plot(x, y, color='red', linewidth=2)

plt.show()





