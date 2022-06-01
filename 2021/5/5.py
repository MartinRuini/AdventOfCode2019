import numpy as np
from pdb import set_trace

def main():
    start, stop = [], []
    with open('input.txt') as f:
        for line in f.readlines():
            startStr, stopStr = line.strip().split(' -> ')
            start += [[int(n) for n in startStr.split(',')]]
            stop  += [[int(n) for n in stopStr.split(',')]]
    start = np.array(start)
    stop  = np.array(stop)
    xMax = np.max( np.concatenate((start[:,0],stop[:,0])) )
    yMax = np.max( np.concatenate((start[:,1],stop[:,1])) )
    grid = np.zeros((xMax+1,yMax+1), dtype=int)
    for istart, istop in zip(start,stop):
        xstart, xstop = np.sort((istart[0], istop[0]))
        ystart, ystop = np.sort((istart[1], istop[1]))
        ### part 1
        if (xstart==xstop) or (ystart==ystop):
            grid[xstart:xstop+1,ystart:ystop+1] += 1
        ### part 2
        else:
            xDirection = np.sign(istop[0]-istart[0])
            yDirection = np.sign(istop[1]-istart[1])
            pathLength = xstop-xstart+1
            for j in range(pathLength):
                xPath = istart[0]+j*xDirection
                yPath = istart[1]+j*yDirection
                grid[xPath,yPath] += 1
    nOverlaps = np.sum(grid>1)
    print(f'number of points with overlaps: {nOverlaps}')

if __name__=='__main__':
    main()
