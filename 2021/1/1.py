import numpy as np

def main():
    inFile = 'input.txt'
    data   = np.genfromtxt(inFile)
    change = np.diff(data)
    hasIncreased = change>0
    nIncreases   = np.sum(hasIncreased)
    print(nIncreases)

    stride = 3
    slidingSummedData = np.zeros_like(data[:-stride+1])
    for i in range(len(slidingSummedData)):
        slidingSummedData[i] = np.sum(data[i:i+stride])
    print( np.sum(np.diff(slidingSummedData)>0) )

if __name__=='__main__':
    main()
