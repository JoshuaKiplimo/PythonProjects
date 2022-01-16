#A binary search with python. 
my_list = [num for num in range(0, 101)] # create a list from 0 to 100

def find(listt, num):
	# it sould be sorted
	#create upper limit
	upper = len(listt)-1
	#create lower limit
	lower = 0
	
	global count
	count = 0 
	while lower <= upper: 
	    middle = int((upper + lower)/2)
	    count  += 1

	    if target == listt[middle] or target == listt[lower] or target == my_list[upper]:
	    	return True
	    	break
	    #if target is less than the mid value, the upper bound becomes the mid valie
	    elif target < listt[middle]:
	         upper = middle
	         middle = int((lower + upper)/2)
	    # if target is greater than the mid value, the lower bound becomes the mid value     
	    else:
	        lower = middle
	        middle = int((lower+upper)/2)

target = int(input('enter input: '))	        
	        
if find(my_list, target):
	print('Found! The number '+ str(target) +' was found after ' + str(count-1) + ' half slices')
else:
	print('not in the list')
