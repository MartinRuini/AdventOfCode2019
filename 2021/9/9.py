import numpy as np
from pdb import set_trace

def main():
    data = np.genfromtxt('input.txt', delimiter=1, dtype=int)

    ### part 1
    lowerThanRight  = np.zeros_like(data, dtype=bool)
    lowerThanLeft   = np.zeros_like(data, dtype=bool)
    lowerThanAbove  = np.zeros_like(data, dtype=bool)
    lowerThanBelow  = np.zeros_like(data, dtype=bool)

    lowerThanRight[:,-1] = True
    lowerThanLeft[:,0]   = True
    lowerThanAbove[0]    = True
    lowerThanBelow[-1]   = True

    lowerThanRight[:,:-1] = (data[:,:-1]<data[:,1:])
    lowerThanLeft[:,1:]   = (data[:,1:]<data[:,:-1])
    lowerThanAbove[1:]    = (data[1:]<data[:-1])
    lowerThanBelow[:-1]   = (data[:-1]<data[1:])

    lowPoints = lowerThanRight & lowerThanLeft & lowerThanAbove & lowerThanBelow
    sumRiskLevels = np.sum(data[lowPoints]) + np.sum(lowPoints)

    print(f'sum of risk levels = {sumRiskLevels}')

    ### part 2
    basins = lowPoints
    lowPointsCoords = [(x,y) for x,y in zip(*lowPoints.nonzero())]
    newExpansionCoords = lowPointsCoords
    while len(newExpansionCoords>0):
        lastExpansionCoords = newExpansionCoords
        newExpansionCoords = []
        for x,y in lastExpansionCoords:
            for neighbourX,neighbourY in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if neighbourX<len(daX,y]<data[neighbourX,neighbourY]<9 and not basins[neighbourX,neighbourY]:
                    newExpansionCoords += [(neighbourX,neighbourY)]
                    basins[neighbourX,neighbourY] = True
    for i in range(1,len(lowPoints)):
        lastExpansion = newExpansion
        newExpansion = (data[i:][lastExpansion[i:]]<data[:i][lastExpansion[:i]])
        if np.sum(newExpansion)==0: break
        basins[i:] |= newExpansion
    for i in range(1,len(lowPoints)):
        lastExpansion = newExpansion
        newExpansion = (data[:i][lastExpansion[:i]]<data[i:][lastExpansion[i:]])
        if np.sum(newExpansion)==0: break
        basins[i:] |= newExpansion
    
if __name__=='__main__':
    main()
