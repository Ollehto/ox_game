import copy

#f1 = ["   ","|","   ","|","   "]
#f2 = ["----------"]
#field =[f1,f2,f1,f2,f1]

#grid_number 
# 1 | 2 | 3 
#-----------
# 4 | 5 | 6 
#-----------
# 7 | 8 | 9 


class Ox:
	def __init__(self):
		#self.f1 = ["   ","|","   ","|","   "]
		#self.f2 = ["----------"]
		self.field = [[" 1 ","|"," 2 ","|"," 3 "],["-----------"],\
		[" 4 ","|"," 5 ","|"," 6 "],["-----------"],[" 7 ","|"," 8 ","|"," 9 "]]
		#self.field = copy.deepcopy(field)
		self.states = [0,0,0,0,0,0,0,0,0]#0-->null,1-->O,2-->X
		self.player = 2#1or2
		self.end_flag = 0 #1-->player1win,2-->player2win,3-->draw

	def update_state(self,grid_number,player):
		self.states[grid_number-1] = player
	
	

	def print_field(self):
		for line in self.field:
			print("\n",end="")
			for par in line:
				print(par,end="")
		print("\n")
		print("-------------------")
		print("\n")

	def conver_grid_number_to_offset(self,grid_number):
		if grid_number in (1,2,3):
			if grid_number == 1:(x,y)=(0,0)
			else:
				if grid_number == 2:(x,y) = (0,2)
				else:(x,y) = (0,4)
		if grid_number in (4,5,6):
			if grid_number == 4:(x,y)=(2,0)
			else:
				if grid_number == 5:(x,y)=(2,2)
				else:(x,y)=(2,4)
		if grid_number in (7,8,9):
			if grid_number == 7:(x,y)=(4,0)
			else:
				if grid_number == 8:(x,y)=(4,2)
				else:(x,y)=(4,4)
		return (x,y)

	def input_OX(self):
		print("input grid_number")
		while(1):
			grid_number =input()
			if grid_number in ('1','2','3','4','5','6','7','8','9'):
				if self.states[int(grid_number)-1] == 0:
					break	
		return int(grid_number)

	def change_field(self):#player-->(O,X)=(0,1)
		grid_number = self.input_OX()
		player = self.player
		(x,y) = self.conver_grid_number_to_offset(grid_number)
		if player == 1: kigou = " O "
		else:kigou = " X " 
		self.field[x][y] = kigou
		self.update_state(grid_number,player)
		#print(self.states)
	

	def player_change(self):
		if self.player ==1:
			self.player = 2
		else:
			self.player = 1

	def flag_control(self):
		states = self.states
		if states[0] == states[1] and states[1] == states[2] and states[0] != 0:
			self.end_flag = states[0]
		if states[3] == states[4] and states[4] == states[5] and states[3] != 0:
			self.end_flag = states[3]
		if states[6] == states[7] and states[7] == states[8] and states[6] != 0:
			self.end_flag = states[6]
		if states[0] == states[3] and states[3] == states[6] and states[0] != 0:
			self.end_flag = states[0]
		if states[1] == states[4] and states[4] == states[7] and states[1] != 0:
			self.end_flag = states[1]
		if states[2] == states[5] and states[5] == states[8] and states[2] != 0:
			self.end_flag = states[2]
		if states[0] == states[4] and states[4] == states[8] and states[0] != 0:
			self.end_flag = states[0]
		if states[2] == states[4] and states[4] == states[6] and states[2] != 0:
			self.end_flag = states[2]

		i =0
		while(1):#check is draw
			if states[i] == 0:
				break
			if i >= 8:
				self.end_flag  = 3
				break
			i += 1


def main():
	game1 = Ox()
	game1.print_field()

	print("player1 --> O, player2 --> X")
	print("")
	print("")
	while(1):
		print("player",game1.player,"'s turn")
		game1.change_field()

		game1.flag_control()
		game1.print_field()
		game1.player_change()
		if game1.end_flag != 0:
			if game1.end_flag == 1:
				print("player1 win!!")
			elif game1.end_flag ==2:
				print("player2 win!!")
			else:
				print("draw!!")
			break

if __name__ == "__main__":
	main()