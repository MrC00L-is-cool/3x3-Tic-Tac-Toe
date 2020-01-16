#Thanks to Asher Olson for help
#Set variables
#Class for 3x3 Grid
#+--------------+
#| A1 | A2 | A3 |
#|--------------|
#| B1 | B2 | B3 |
#|--------------|
#| C1 | C2 | C3 |
#+--------------+
class grid:
	def __init__(self, solved = "no", A1 = "1", A2 = "2", A3= "3", B1 = "4", B2 = "5", B3 = "6", C1 = "7", C2 = "8", C3 = "9"):
		self.solved = solved
		self.A1 = A1
		self.A2 = A2
		self.A3 = A3
		self.B1 = B1
		self.B2 = B2
		self.B3 = B3
		self.C1 = C1
		self.C2 = C2
		self.C3 = C3

	def checkwin(self):
		if self.A1 == self.A2 and self.A2 == self.A3:
			self.solved = curPlayer
		elif self.B1 == self.B2 and self.B2 == self.B3:
			self.solved = curPlayer
		elif self.C1 == self.C2 and self.C2 == self.C3:
			self.solved = curPlayer
		elif self.A1 == self.B1 and self.B1 == self.C1:
			self.solved = curPlayer
		elif self.A2 == self.B2 and self.B2 == self.C2:
			self.solved = curPlayer
		elif self.A3 == self.B3 and self.B3 == self.C3:
			self.solved = curPlayer
		elif self.A1 == self.B2 and self.B2 == self.C3:
			self.solved = curPlayer
		elif self.A3 == self.B2 and self.B2 == self.C1:
			self.solved = curPlayer
		else:
			self.solved = "no"
#May not need
	def checksolved(self):	
		if self.solved == True:
			pass
		else:
			pass

#End of Program
def endProg():
	curses.nocbreak()
	my_screen.keypad(0)
	curses.echo()
	curses.curs_set(1)
	curses.endwin()
	print("Finished")
	exit


def possibleMove(*coords):
	if move == 1:
		coordPlayed.insert(len.coordPlayed - 1, A1)
	elif move == 2:
		coordPlayed.insert(len.coordPlayed - 1, A2)
	elif move == 3:
		coordPlayed.insert(len.coordPlayed - 1, A3)
	elif move == 4:
		coordPlayed.insert(len.coordPlayed - 1, B1)
	elif move == 5:
		coordPlayed.insert(len.coordPlayed - 1, B2)
	elif move == 6:
		coordPlayed.insert(len.coordPlayed - 1, B3)
	elif move == 7:
		coordPlayed.insert(len.coordPlayed - 1, C1)
	elif move == 8:
		coordPlayed.insert(len.coordPlayed - 1, C2)
	elif move == 9:
		coordPlayed.insert(len.coordPlayed - 1, C3)
	else:
		pass

main = grid()
coordPlayed = ["roof"]
move = 0
curPlayer = "X"

#To check the os
import os
print(os.name)

#For Color
try:
	import curses
except:
	if os.name=='nt':
		print("You have been detected running windows, please run this command first")
		print("python -m pip install windows-curses")
		exit
	else:
		print("Something went wrong! Please try to install the Curses module")
		exit
screen = curses.initscr()
curses.start_color()
if curses.has_colors():
	#Basic
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	#1st Player
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
	#2nd Player
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
	#Selected
	curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
else:
	pass

#Test correct size
num_rows, num_cols = screen.getmaxyx()
if num_rows < 9:
	print("Please increase your terminal size")
	exit
if num_cols < 15:
	print("Please increase your terminal size")
	exit


#Set up GUI
win = curses.newwin(0, 0, curses.LINES - 1, curses.COLS - 1)
screen.addstr(0, 0, "┏━━━┳━━━┳━━━┓", curses.color_pair(1))
screen.addstr(1, 0, "┃  ?  ┃  ?  ┃  ?  ┃", curses.color_pair(1))
screen.addstr(2, 0, "┣━━━╋━━━╋━━━┫", curses.color_pair(1))
screen.addstr(3, 0, "┃  ?  ┃  ?  ┃  ?  ┃", curses.color_pair(1))
screen.addstr(4, 0, "┣━━━╋━━━╋━━━┫", curses.color_pair(1))
screen.addstr(5, 0, "┃  ?  ┃  ?  ┃  ?  ┃", curses.color_pair(1))
screen.addstr(6, 0, "┗━━━┻━━━┻━━━┛", curses.color_pair(1))
screen.addstr(8, 0, "Please enter the place you want to go: ", curses.color_pair(1))
screen.addstr(9, 0, "It is " + curPlayer + "'s turn", curses.color_pair(1))
#Apply screen changes
screen.refresh()
	
def winScreen(winner):
	screen.addstr(0, 0, "             ", curses.color_pair(1))
	screen.addstr(1, 0, "Congradulations   ", curses.color_pair(1))
	screen.addstr(2, 0, "       Player         ", curses.color_pair(1))
	screen.addstr(3, 0, winner + "!", curses.color_pair(1))
	#screen.addstr(4, 0, "┣━━━╋━━━╋━━━┫", curses.color_pair(1))
	#screen.addstr(5, 0, "┃  ?  ┃  ?  ┃  ?  ┃", curses.color_pair(1))
	#screen.addstr(6, 0, "┗━━━┻━━━┻━━━┛", curses.color_pair(1))
	screen.refresh
	curses.napms(6000)
	endProg()

def resetVars():
	main = grid()
	coordPlayed = ["roof"]
	move = 0
	curPlayer = "X"

def playerTurn():
	global main, coordPlayed, move, curPlayer
	screen.refresh
	square = screen.getch()
	if square == "1":
		main.A1 = curPlayer
	elif square == "2":
		main.A2 = curPlayer
	elif square == "3":
		main.A3 = curPlayer
	elif square == "4":
		main.B1 = curPlayer
	elif square == "5":
		main.B2 = curPlayer
	elif square == "6":
		main.B3 = curPlayer
	elif square == "7":
		main.C1 = curPlayer
	elif square == "8":
		main.C2 = curPlayer
	elif square == "9":
		main.C3 = curPlayer
	main.checkwin()
	if main.solved == "X":
		winScreen("X")
	elif main.solved == "O":
		winScreen("O")
	else:
		if curPlayer == "X":
			curPlayer = "O"
			playerTurn()
		else:
			curPlayer = "X"
			playerTurn()
	screen.refresh

#Play game
playerTurn()
