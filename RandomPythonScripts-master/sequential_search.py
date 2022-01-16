
#sequential search solution 1 

def search(arr,element):
    for elem in arr:
        if elem == element:
            return str(element) + ' found at index position '+ str(arr.index(element))

    return 'Element not found'




print(search([1,2,3,4,5,5,6,7],9))

#sequential search using a while loop 

def search(arr, elem):
    position = 0 # where we are starting at
    found  = False # flag if not found 

    while position < len(arr) and found == False:
        if arr[position] == elem:
            found = True
        else:
            position += 1
    return found

print(search([1,2,3,4,5],8))