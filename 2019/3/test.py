import sys

def main():
    list1 = [1 ,[2 ,3]]
    list2 = [3,4,5, [2,3],1]

    for el in list1:
        if el in list2:
            print(el)

main()