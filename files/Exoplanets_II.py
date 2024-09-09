#Make a graph with the mass of the star $M_\star$ (in solar masses) versus  $a_{\rm inner}$ and $a_{\rm outer}$ (in AU) that shows the boundaries (inner and outer) of the habitable zone around stars with masses from 0.1 to 2 times the mass of the Sun. 

import numpy as np
import matplotlib.pyplot as plt
import math

Lsun = 3.86e26
Boltzmann = 5.67e-8
AU = 1.496e11

T1 = 273
T2 = 373


def Luminosity(M):
    return Lsun * math.pow(M, 3)

def findD(L, T):
    return (math.pow(((1-0.36) * L)/ (16*math.pi*Boltzmann), 0.5)* math.pow(T, -2)) / AU


M = np.arange(0.1, 2.1, 0.1)
D1 = []
D2 = []

for i in range(len(M)):
    D1.append(findD(Luminosity(M[i]), T1))
    D2.append(findD(Luminosity(M[i]), T2))


# plot mass with a of T1 and T2

#plt.plot(x, y, label = "label")

plt.plot(D1, M, label = "Temperater = 273 K")
plt.plot(D2, M, label = "Temperature = 373 K")

plt.ylabel('Mass of the star (Msun)')
plt.xlabel('Distance (AU)')

plt.title('Habitable zone boundaries')
plt.legend()
plt.show()