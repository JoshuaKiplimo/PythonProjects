import threading #one thread controls each color
import random #
import os #to clear the c=screen before rendring another screen 
import time 


tree = list(open('tree.txt').read().rstrip())

def coloured_dot(color):
	if color == 'red':
		return f'\033[91m🔴\033[0m'
	if color == 'yellow':
		return f'\033[91m🟡\033[0m'
	if color == 'green':
		return f'\033[91m🟢\033[0m'
	if color == 'blue':
		return f'\033[91m🔵\033[0m'
	
def lights(color,indexes):
	off = True
	while True:
		for idx in indexes:
			tree[idx] = coloured_dot(color) if off else '🟢'
		os.system('cls' if os.name== 'nt' else 'clear')
		print(''.join(tree))
		off = not off
		time.sleep(random.uniform(.5, 1.5))

#variables to store position of list 
yellow = []
red = []
blue = []
green = []


for i, c in enumerate(tree): #enumerate keeps count of our enumerations 
	if c == "Y":
		yellow.append(i) #replace the positions with the color emojis....
		tree[i] = '🟡'
	if c == "R":
		red.append(i)
		tree[i] = '🔴'
	if c == "G":
		green.append(i)
		tree[i] = '🟢'

	if c == "B":
		blue.append(i)
		tree[i] = '🔵'



ty = threading.Thread(target= lights, args =('yellow', yellow))
tr = threading.Thread(target= lights, args =('red', red))
tg = threading.Thread(target= lights, args =('green', green))
tb = threading.Thread(target= lights, args =('blue',blue))

for t in [ty, tr, tg, tb]:
	t.start()
for t in [ty, tr, tg, tb]:
	t.join()
