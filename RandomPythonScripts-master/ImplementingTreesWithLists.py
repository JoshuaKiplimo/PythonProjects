def BinaryTree(r):
    return[r,[],[]] #creates a root node with 2 empty subtrees,index1 -left, index 2 right

#insert a new left subtree by adding elements to the second list


#left subtrees

def insertleft(root, newBranch):
    t = root.pop(1)#first obtained a list which could possibly be empty

    if len(t) > 1:
        root.insert(1,[newBranch,t,[]]) #new branch, left (r) and right(empty)
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertright(root, newBranch):
    t = root.pop(2)#first obtained a list which could possibly be empty

    if len(t) > 1:
        root.insert(2,[newBranch,[], t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootValue(root):
    #Function that gets the value of root
    #Root is at position 0
    return root[0]
def setRootValue(root, newVal):
    #To set a new value to be root
    root[0] = newVal
def getLeftChild(root):
    #Gets the left child which is in index 1
    return root[1]
def getRightChild(root):
    #Gets right child which is in index 2
    return root[2]




r = BinaryTree(3)
insertright(r,7) #takes in the root and an item,7
