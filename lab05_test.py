import lab05

def test_is_vowel():
    assert lab05.is_vowel('a') == True
    assert lab05.is_vowel('e') == True
    assert lab05.is_vowel('i') == True
    assert lab05.is_vowel('o') == True
    assert lab05.is_vowel('u') == True
    assert lab05.is_vowel('m') == False
    assert lab05.is_vowel('x') == False
    assert lab05.is_vowel('.') == False
    assert lab05.is_vowel(' ') == False

def test_count_vowels_iter():
    assert lab05.count_vowels_iter('rebel') == 2
    assert lab05.count_vowels_iter('livelihood') == 5
    assert lab05.count_vowels_iter('traditional') == 5
    assert lab05.count_vowels_iter('this is a sentence') == 6
    assert lab05.count_vowels_iter('cat') == 1
    assert lab05.count_vowels_iter('leonard') == 3
    assert lab05.count_vowels_iter('bcd') == 0

def test_count_vowels_rec():
    assert lab05.count_vowels_rec('rebel') == 2
    assert lab05.count_vowels_rec('livelihood') == 5
    assert lab05.count_vowels_rec('traditional') == 5
    assert lab05.count_vowels_rec('this is a sentence') == 6
    assert lab05.count_vowels_rec('cat') == 1
    assert lab05.count_vowels_rec('leonard') == 3
    assert lab05.count_vowels_rec('bcd') == 0

def mult(a, b):
    return a * b

def test_my_reduce():
    assert lab05.my_reduce([1,2,3,4,5], 1, mult) == 120
    assert lab05.my_reduce([1,2,3,4,5], 1, lambda a,b: a * b) == 120
    assert lab05.my_reduce([1,2,3,4,5], 0, lambda a,b: a * b) == 0
