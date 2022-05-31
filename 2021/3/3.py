import numpy as np

def main():
    inFile = 'input.txt'
    data = np.genfromtxt(inFile, delimiter=1, dtype=int)
    nBitsPerRow = data.shape[1]

    ### part 1
    gammaRate = np.zeros(nBitsPerRow, dtype=int)
    for ibit in range(nBitsPerRow):
        if np.sum(data[:,ibit])>len(data)/2:
            gammaRate[ibit] = 1

    gammaRateStr   = ''.join(map(str,gammaRate))
    epsilonRateStr = ''.join(map(str,1-gammaRate))
    gammaRateInt   = int(gammaRateStr, 2)
    epsilonRateInt = int(epsilonRateStr, 2)
    powerConsumption = gammaRateInt*epsilonRateInt
    print(f'power consumption = {powerConsumption}')

    ### part 2
    maskOxygen = np.ones(len(data), dtype=bool)
    maskCO2    = np.ones(len(data), dtype=bool)
    for ibit in range(nBitsPerRow):
        if np.sum(data[maskOxygen,ibit])>=np.sum(maskOxygen)/2:
            maskOxygen *= (data[:,ibit]==1)
        else:
            maskOxygen *= (data[:,ibit]==0)
        if np.sum(maskOxygen)==1:
            break
    else:
        print('maskOxygen loop finished with {np.sum(maskOxygen)} numbers left')

    for ibit in range(nBitsPerRow):
        if np.sum(data[maskCO2,ibit])>=np.sum(maskCO2)/2:
            maskCO2 *= (data[:,ibit]==0)
        else:
            maskCO2 *= (data[:,ibit]==1)
        if np.sum(maskCO2)==1:
            break
    else:
        print('maskCO2 loop finished with {np.sum(maskCO2)} numbers left')

    oxyGenRatingStr = ''.join(map(str,*data[maskOxygen]))
    CO2scrRatingStr = ''.join(map(str,*data[maskCO2]))
    oxyGenRatingInt = int(oxyGenRatingStr, 2)
    CO2scrRatingInt = int(CO2scrRatingStr, 2)
    lifeSupportRating = oxyGenRatingInt*CO2scrRatingInt
    print(f'life support rating = {lifeSupportRating}')

if __name__=='__main__':
    main()
