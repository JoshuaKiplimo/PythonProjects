arr = [1,2,3,4,5,6,7,8,9,10]
print(len(arr)//2)


#SIMPLIFIED FIRST SOLUTION 

def binarysearch(arr, elem):
    lower = 0
    upper = len(arr) - 1
    


    while lower < upper:
        middle = (lower + upper)//2 #mid index
        #edge case
        if arr[middle] == elem:
            print (str(elem)+ ' found at ' + str(middle))
            break
        elif arr[middle] < elem :
            lower = middle +1 
            
        else:# middle is greater than element
            upper = middle -1
            



#RECURSIVE SOLUTION



def rec_search(arr, elem):
    #edge case
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if elem == mid:
            return True
        else:
            if elem < arr[mid]:
                return rec_search(arr[:mid],elem)#upto but not including the middle array
            else:
                return rec_search(arr[mid+1:],elem)
    
        

print(rec_search(arr,12))