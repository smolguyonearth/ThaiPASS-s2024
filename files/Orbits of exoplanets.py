import numpy as np
import matplotlib.pyplot as plt
import math

def distance(M, P): 
    return math.pow(math.pow(P, 2) * M, 1/3)
    
# start stop step
#start at 0.1 and end before 5.1, get the values every 0.1 step

P = np.arange(0.1, 5.1, 0.1)

#start, stop, num
#five values between 0.1 and 2
M = np.linspace(0.1, 2, 5)

#keep distance values in a list
distances = []

# for i in range(len(M)):
#     for j in range(len(P)):
#         distances.append(distance(M[i], P[j]))

plt.figure()
for i in range(len(M)):
    #consist of (start, end)
    #distances[i*len(P):(i+1)*len(P)] will give the distances for the ith planet
    plt.plot(P, distances[i*len(P):(i+1)*len(P)], label='M = ' + str(round(M[i],1)))
plt.xlabel('Period (days)')
plt.ylabel('Semi-major axis (AU)')
plt.title('Orbits of exoplanets')
plt.legend()
plt.show()