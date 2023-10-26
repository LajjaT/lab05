# Lab 04

# part 1

# TODO: YOUR is_vowel() FUNCTION GOES HERE
def is_vowel(letter):
    if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
        return False
    else:
        return True

#test
#print(is_vowel('a'))
#print(is_vowel('b'))

# part 2

# TODO: YOUR count_vowels_iter() FUNCTION GOES HERE
def count_vowels_iter(sentence):
    count = 0
    for i in range(len(sentence)):
        if(sentence[i] == 'a' or sentence[i] == 'e' or sentence[i] == 'i' or sentence[i] == 'o' or sentence[i] == 'u'):
            count+=1
    return count

#test    
#print(count_vowels_iter('bears eating breakfast'))

# part 3

# TODO: YOUR count_vowels_rec() FUNCTION GOES HERE
def count_vowels_rec(sentence):
    count = 0
    
    if len(sentence) == 0:
        return 0
    
    the_sentence = sentence[0]
    
    if (the_sentence == 'a' or the_sentence == 'e' or the_sentence == 'i' or the_sentence == 'o' or the_sentence == 'u'):
       # print(sentence)
        return 1 + count_vowels_rec(sentence[1:]) #combine 1 for the count AND calling the function again
    
    else:
        return count_vowels_rec(sentence[1:])

    #sentence
#test print(count_vowels_rec('bears eating breakfast'))

    
# part 4

# TODO: YOUR myreduce() FUNCTION GOES HERE
def my_reduce(values, start_val, op):
    current_value = start_val
    for value in values:
        current_value = op(current_value, value)
    return current_value

values = [1, 2, 3, 4, 5]
current_value = my_reduce(values, 0,  lambda x,y: x + y)
#test 
# print(current_value)