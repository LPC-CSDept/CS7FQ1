import random
import main


def test_name():
    obj1 = main.Names('John', 'Female', 100)
    obj2 = main.Names('Mary', 'Female', 10)

    assert obj1.name == 'John'
    assert obj1.count == 100, 'expected 100 (numeric)'
    assert obj1.__str__ != None

    assert (obj1 > obj2) == True, 'expected True'
    assert (obj1 < obj2) == False, 'expected False'


def test_init():
    main.Names.numNames = 0
    ca = main.makeList('ca2021.txt')

    lenlist = len(ca)
    print(f'Total number of Names objects in the list: {lenlist}')
    assert lenlist == 200, "Invalid value. Expected 200"
    print(f'Class Attribute numNames:  {main.Names.numNames}')
    assert main.Names.numNames == 200, " 200 "
    assert ca.__str__ != None


def test_gt():
    ca = main.makeList('ca2021.txt')
    ca.sort(reverse=True)
    print('1st element after sorting', ca[0])
    assert ca[0].name == 'Noah', 'Expected Noah'


def test_printName():
    ca = main.makeList('ca2021.txt')
    ret = main.printName(ca, 'D')
    assert ret == 8, 'expected 8'
    ret = main.printName(ca, 'R')
    assert ret == 5, 'expected 5'
