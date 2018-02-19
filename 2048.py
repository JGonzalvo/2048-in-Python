from msvcrt import getch
import random
board_size=4
gameStart=True
global board
board=[[0] * board_size for i in range(board_size)]
max_tries=board_size*board_size*3
rand_choices=[2]
board=[[0,1,1,0],
	   [0,0,2,2],
	   [2,1,1,0],
	   [2,2,2,2]]
def pick_pos():
	ctr=0
	while True:
		rand_pos_x=random.randrange(0, board_size)
		rand_pos_y=random.randrange(0, board_size)
		ctr+=1
		if board[rand_pos_x][rand_pos_y]==0:
			break;
		if ctr==max_tries:
			break;
	return rand_pos_x,rand_pos_y,ctr

def flip(board,ctr):
	if ctr==0:
		return board
	for x in range(0,ctr):
		temp=list(zip(*board[::-1]))
		board=temp
	return board
	
def move(line):
	temp=[]
	line = list(map(int, line))
	for x in range(0,board_size):
		if line[x]!=0:
			temp.append(line[x])
	for x in range(len(temp),board_size):
		temp.append(0)
		
	for x in range(0,board_size-1):
		if temp[x]==temp[x+1]:
			temp[x]*=2
			temp[x+1]=0
			x+=1
	del line[:]		
	for x in range(0,board_size):
		if temp[x]!=0:
			line.append(temp[x])
	for x in range(len(line),board_size):
		line.append(0)
	return line
	
def keyPress(direction,board):
#0 is left
#1 is down
#2 is right
#3 is up
	temp=flip(board,direction)
	board=temp
	temp=[]
	for x in board:
		temp.append(move(x))
	board=temp

	board=flip(board,4-direction)
	
	return board
	

while gameStart:
	key = ord(getch())
	if key == 27: #ESC
		break
	elif key == 13: #Enter
		print("Enter")
	elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
		key = ord(getch())
		if key == 80: #Down arrow
			board=keyPress(1,board)
		elif key == 72: #Up arrow
			board=keyPress(3,board)
		elif key == 75: #Left arrow
			board=keyPress(0,board)
		elif key == 77: #Right arrow
			board=keyPress(2,board)
		x,y,tries=pick_pos()
		if tries==max_tries:
			print("Game Over") # GameOver
		else:
			board=list(map(list, board))
			board[0][0]=2
		for x in board:
			print(x)
		print("\n")




