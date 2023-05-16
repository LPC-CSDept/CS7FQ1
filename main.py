import pandas as pd


class Names:
    numNames = 0
    def __init__(self, n, g, c):
        self._name = n
        self._gender = g
        self._count = c
        Names.numNames += 1
    #################
    # Implement the class Names
    #################


def makeList(filename):
    df = pd.read_csv(filename, delimiter='\s+')
    namelist = []
    #################
    # Code your program
    #################
    return namelist


def sortbyCount(nlist):
    #################
    # Code your program
    #################


def printList(nlist):
    print(f'Total number of Names: {Names.numNames}')
    for v in nlist:
        print(v)


def printName(nlist, key):
    return cnt


def main():
    nlist = makeList('ca2021.txt')
    sortbyCount(nlist)
    printList(nlist)
    ret = printName(nlist, 'D')
    ret = printName(nlist, 'R')


if __name__ == '__main__':
    main()
