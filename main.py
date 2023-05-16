import pandas as pd


class Names:
    numNames = 0
    #################
    # Implement the class Names
    #################

    def __init__(self, n, g, c):
        self._name = n
        self._gender = g
        self._count = c
        Names.numNames += 1


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
    cnt = 0
    print(f'################ Names starting with {key} ################')
    for v in nlist:
        if v.name.startswith(key):
            print(v)
            cnt += 1
    print(f'################ Total {cnt} names found ################')
    return cnt


def main():
    nlist = makeList('ca2021.txt')
    sortbyCount(nlist)
    printList(nlist)
    ret = printName(nlist, 'D')
    ret = printName(nlist, 'R')


if __name__ == '__main__':
    main()
