# word = 'AAABBBCCCDDDDDDEEEEFFF'

# length = len(word)
# i = 0
# while i < length:
#     first_word = word[0]
#     if word[i+1] == first_word:


def compress(s):
    #compressing without checking 

    r = ''
    l= len(s)
    if l == 0:
        return ''
    if l == 1:
        return s+'1'   


   last = s[0]
   count = 1 
   i = 1   
   
   while i < l:
       if s[i] == s[i-1]:
           count += 1
       else:
           r = r + s[]