class Hashtable(object):
	def __init__(self, size): #initializing by taking in the OBJECT, SIZE
		self.size = size #create size
		self.slots = [None] * self.size #multiply by self.size
		self.data = [None] * self.size #the empty space thta data can go into
	

	def put(self, key, data): #assigns data to the correct key
		#They key is used in a hash in the same way that an index is used in an array
		#The key determines where the value will be stored
        #put adds a new key-value pair to the map # We are going to use int keys
        hashvalue = self.hashfunction(key, len(self.slots))
        #we use its value to know where to put in the data





        if self.slots == None: #check if slots is empty
        	self.slots[hashvalue] = key #fill in key and data 
        	self.data[hashvalue] = data
        else:
        	if self.slots[hashvalue] == key: #if the key already exists, just replace the old value
        		self.data[hashvalue] = data
        	else: #finding next available slot
        		nextslot = self.rehash(hashvalue, len(self.slots))
        		#getting to next slot
        		while self.slots[nextslot] != None and self.slots[nextslot] != key:
        			nextslot = self.rehash(nextslot, len(self.slots))# basiclly if the next slot is occupied, we rehash the original nextslot until we find an empty space
                #set the new key if None
                if self.slots[nextslot] == None:
                	self.slots[nextslot] = key
                	self.data[nextslot] = data
                else:
                	self.data[nextslot] = data




    def hashfunction(self, key, size): 
    	
    	return key%size

    def rehash(self, oldhash, size):
    	return(oldhash+1)%size

    def get(self, key):
    	startslot = hashfunction(key,len(slot.size))#where we will begin searching

    	data = None
    	found = False # to monitor if we have found the value 
    	position = startslot
    	stop = False


    	while self.slots[position] != None and found != False and stop != False:

    		if self.slots[position] == key:
    			found = True
    			stop = True
    		else:
    			position = self.rehash(position, len(self.slots))
    	return data
def __getitem__(self, key):
	return self.get(key)
def __setitem__(self,key):
	return self.put(key,data)

#to implement 
# hash = Hashtable(size of your hashtable)
#hash = Hashtable(5)


