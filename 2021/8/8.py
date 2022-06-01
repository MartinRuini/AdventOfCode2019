import numpy as np
from pdb import set_trace

def main():
    occurrence1478 = 0
    nSegmentsInDigit = {
            0 : 6,
            1 : 2,
            2 : 5,
            3 : 5,
            4 : 4,
            5 : 5,
            6 : 6,
            7 : 3,
            8 : 7,
            9 : 6
            }
    sumOutputs = 0
    with open('input.txt') as f:
        for line in f.readlines():
            digitDict = { digit : [] for digit in range(10)}
            segmentDict = {}
            output = line.strip().split(' | ')[1].split(' ')
            uniqueDigits = line.strip().split(' | ')[0].split(' ')
            for digit in output:
                if len(digit) in (2,3,4,7):
                    occurrence1478 += 1
            for digit in uniqueDigits:
                for number,nSegments in nSegmentsInDigit.items():
                    if len(digit)==nSegments:
                        if sorted(digit) not in digitDict[number]:
                            digitDict[number] += [sorted(digit)]
            for number,segmentCombinations in digitDict.items():
                if len(segmentCombinations)==1:
                    digitDict[number] = segmentCombinations[0]
            for segment in digitDict[7]:
                if not segment in digitDict[1]:
                    segmentDict['a'] = segment
                    break
            for segmentCombination in digitDict[6]:
                if digitDict[1][0] not in segmentCombination:
                    digitDict[6] = segmentCombination
                    segmentDict['c'] = digitDict[1][0]
                    segmentDict['f'] = digitDict[1][1]
                elif digitDict[1][1] not in segmentCombination:
                    digitDict[6] = segmentCombination
                    segmentDict['c'] = digitDict[1][1]
                    segmentDict['f'] = digitDict[1][0]
                else:
                    continue
                break
            for segment in digitDict[4]:
                for segmentCombination in digitDict[0]:
                    if segmentCombination==digitDict[6]: continue
                    if segment not in segmentCombination:
                        digitDict[0] = segmentCombination
                        segmentDict['d'] = segment
                        break
                else:
                    continue
                break
            digitDict[9] = [segmentCombination for segmentCombination in digitDict[9] if (segmentCombination!=digitDict[6]) and (segmentCombination!=digitDict[0])]
            digitDict[2] = [segmentCombination for segmentCombination in digitDict[2] if segmentDict['f'] not in segmentCombination]
            digitDict[3] = [segmentCombination for segmentCombination in digitDict[3] if (segmentDict['c'] in segmentCombination) and (segmentDict['f'] in segmentCombination)]
            digitDict[5] = [segmentCombination for segmentCombination in digitDict[5] if segmentDict['c'] not in segmentCombination]
            for number,segmentCombinations in digitDict.items():
                if len(segmentCombinations)==1:
                    digitDict[number] = segmentCombinations[0]
            outputstr = ''
            for digit in output:
                for number, segments in digitDict.items():
                    if sorted(digit)==segments:
                        outputstr += str(number)
                        break
            sumOutputs += int(outputstr)

    print(f'occurrence of 1,4,7,8: {occurrence1478}')
    print(f'sum of outputs: {sumOutputs}')

if __name__=='__main__':
    main()
