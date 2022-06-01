import numpy as np
from pdb import set_trace

def main():
    fish = np.genfromtxt('input.txt', delimiter=',', dtype=int)

    nDays = 256

    ### part 1, brute force
    for day in range(1,nDays+1):
        if day>80: break
        newFish = np.sum(fish==0)
        fish -= 1
        fish[fish<0] = 6
        if newFish>0:
            fish = np.concatenate((fish, 8*np.ones(newFish, dtype=int)))
        if day%10==0:
            print(f'on day {day}: {len(fish)} fish')

    ### part 2
    print('')
    fish = np.genfromtxt('input.txt', delimiter=',', dtype=int)

    fishHist = np.histogram(fish, bins=range(10))[0]
    for day in range(1,nDays+1):
        newFish = fishHist[0]
        fishHist = np.append(fishHist[1:], newFish)
        fishHist[6] += newFish
        if day%40==0 or day==256:
            print(f'on day {day}: {np.sum(fishHist)} fish')

if __name__=='__main__':
    main()
