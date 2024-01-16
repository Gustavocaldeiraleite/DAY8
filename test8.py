from DAY8 import combine

def test1():
    assert combine("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def test2():
    assert combine('') == []

def test3():
    assert combine('2') == ["a","b","c"]

if __name__ == '__main__':
    test1()
    test2()
    test3()
    print('all tests passed')
    