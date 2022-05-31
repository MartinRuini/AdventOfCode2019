import numpy as np

def main():
    inFile = 'input.txt'
    data   = np.genfromtxt(inFile)
    change = np.diff(data)
    hasIncreased = change>0
    nIncreases   = np.sum(hasIncreased)
    print(nIncreases)

if __name__=='__main__':
    main()
