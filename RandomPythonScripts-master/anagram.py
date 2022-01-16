#Anagaram solution 1 
#An anagram is a word formed from rearranging other letters 
# for example cat and tac 





#solution1
def anagram(word1, word2):
    #Remove the spaces
    word1 = sorted(word1.replace(' ', ''))
    word2 = sorted(word2.replace(' ', ''))
    print(word1, word2)
    

    if word1 == word2:
        print('True')
    else:
        print('False')


    
#solution2


def anagram2(word1, word2):
    word1 = word1.replace(' ', '')
    word2 = word2.replace(' ', '')

    if len(word1) != len(word2):
        return False
    
    else:
        count = {}
        for letter in word1:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        for letter in word2:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1

        for num in count:
            if count[num] != 0:
                return False
            else:
                return True
        




print(anagram2('cat dog', 'tac god'))
