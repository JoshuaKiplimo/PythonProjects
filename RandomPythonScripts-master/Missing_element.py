#You have two arays, the second array has been shuffled and an element removed, find out which element has been removed 

#solution 1 - Brute Force 

def finder(arr1, arr2):
   
    for element2 in arr1:
        
        if element2 not in arr2:
            print(element2)

# solution 2 using an inbuilt method zip 

def finder2(arr1, arr2):
	arr1.sort()
	arr2.sort()

	for elem1, elem2 in zip(arr1, arr2):#zip() maps the similar index of multiple containers 
		if elem1 != elem2:
			return elem1



print(finder2([1,2,3,4,5],[5,4,3,2]))