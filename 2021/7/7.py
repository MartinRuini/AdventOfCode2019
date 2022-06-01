import numpy as np
from matplotlib import pyplot as plt

def main():
    data = np.genfromtxt('input.txt', delimiter=',', dtype=int)

    fuelCost = np.zeros(max(data)+1, dtype=int)
    ### part 1
    for x in range(max(data)+1):
        fuelCost[x] = np.sum( np.abs(data-x) )
    print(f'part 1 min fuel cost = {min(fuelCost)}')
    #plt.plot(fuelCost)

    ### part 2
    for x in range(max(data)+1):
        # fast
        fuelCost[x] = np.sum( (np.abs(data-x)+1)*np.abs(data-x)/2 )
        # slow
        #fuelCost[x] = np.sum( list(map(lambda x: sum(range(x+1)), np.abs(data-x))) )
        #fuelCost[x] = sum( map(lambda x: sum(range(x+1)), np.abs(data-x)) )
    print(f'part 2 min fuel cost = {min(fuelCost)}')
    #plt.plot(fuelCost)
    #plt.show()

if __name__=='__main__':
    main()
