
#reversing a string

#solution 1
# word = " Hi, Are you ready to go? "

# word= word.strip().split(" ")
# word.reverse()
# word = ' '.join(word)



#solution 2
word = " I am ready to go "
def reverse(word):
    length = len(word)
    words = []
    i = 0 
    while i < length:
        if word[i] != ' ':
            starting_word = i
            
            while i < length and word[i] != ' ':
                i += 1
            words.append(word[starting_word:i])
                
        i +=1   
        
    return ' '.join(words[::-1])

print(reverse(word))