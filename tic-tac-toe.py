import turtle
import random
import functools

# Setup Turtle Screen
screen = turtle.Screen()
screen.title('Tic Tac Toe')
screen.bgcolor("NavajoWhite2")
screen.setup(width=800, height=800)

delay = 0.1

#Instruction Section
instructions = turtle.Turtle()
instructions.color('black')
instructions.up()
instructions.hideturtle()
instructions.goto(0, -300)
instructions.write('Please select a number between 1-9. You are player "X".', align='center', font=('Courier', 12, 'normal'))

#Message Screen
message = turtle.Turtle()
message.color('green')
message.up()
message.hideturtle()
message.goto(0, -260)
message.write("It's your turn first.",
align='center', font=('Courier', 12, 'normal'))

#Draw Board
board = turtle.Turtle()
board.shape('circle')
board.pensize(3)
board.penup()
board.goto(-200, 166.5)
board.color('black')
board.pendown()
board.forward(400)
board.up()
board.goto(-200, 33.5)
board.pendown()
board.forward(400)
board.up()
board.goto(-66.5, 300)
board.pendown()
board.left(-90)
board.forward(400)
board.up()
board.goto(66.5, 300)
board.pendown()
board.forward(400)
board.up()
board.goto(-200, 300)
board.pendown()
board.right(-90)
board.forward(400)
board.right(90)
board.forward(400)
board.right(90)
board.forward(400)
board.right(90)
board.forward(400)
board.hideturtle()

#Draw Player (X and O) Symbols
def write_x(x, y): 
    turtle.color('black')
    turtle.up()
    turtle.hideturtle()
    turtle.goto(x, y)
    turtle.write('X',
    align='center', font=('Courier', 90, 'normal'))

def write_o(x, y):
    turtle.color('black')
    turtle.up()
    turtle.hideturtle()
    turtle.goto(x, y)
    turtle.write('O',
    align='center', font=('Courier', 90, 'normal'))


board_coordinates = ((-133.17, 166.5), (0, 166.5),
                    (133.34, 166.5), (-133.17, 33), (0, 33), (133.34, 33), (-133.34, -100), (0, -100), (133.34, -100))
board_status = ["", "", "",
                "", "", "",
                "", "", ""]
winner = ""

# Testing Only -- To Delete Later:
# write_o(board_coordinates[0][0], board_coordinates[0][1])

# write_x(board_coordinates[0][0], board_coordinates[0][1])

# for item in board_coordinates:
#     write_x(item[0], item[1])


def update_user_choice(index_val):
    if board_status[index_val] == "":
        board_status[index_val] = "X"
        write_x(board_coordinates[index_val][0], board_coordinates[index_val][1])
    return

#Check for Win or Tie

#Check Rows
def checkRow(board):
    global winner

    if board_status[0] == board_status[1] == board_status[2] and board_status[0] != "-":
        winner = board_status[0]
        return True
    elif board_status[3] == board_status[4] == board_status[5] and board_status[3] != "-":
        winner = board_status[3]
        return True
    elif board_status[6] == board_status[7] == board_status[8] and board_status[6] != "-":
        winner = board_status[6]
        return True

# Check the vertical columns:
def checkColumn(board_status):
    global winner
    if board_status[0] == board_status[3] == board_status[6] and board_status[0] != "-":
        winner = board_status[0]
        return True
    elif board_status[1] == board_status[4] == board_status[7] and board_status[1] != "-":
        winner = board_status[1]
        return True
    elif board_status[2] == board_status[5] == board_status[8] and board_status[2] != "-":
        winner = board_status[3]
        return True

# Check the two diagonals:
def checkDiag(board_status):
    global winner
    if board_status[0] == board_status[4] == board_status[8] and board_status[0] != "-":
        winner = board_status[0]
        return True
    elif board_status[2] == board_status[4] == board_status[6] and board_status[4] != "-":
        winner = board_status[2]
        return True

# def check_status():
#     #Check Horizontal
#     if checkRow(board_status):

#     #Check Vertical
#     elif checkColumn(board_status):

#     #Check Diagonal
#     elif checkDiag(board_status): 

#     #Check for a Tie
#     elif "" not in board_status:
        

# def computer_turn():
    


def update_message(text):
    message.clear()
    message.write(text,
    align='center', font=('Courier', 12, 'normal'))

# Keypress Event Listeners
screen.onkeypress(functools.partial(update_user_choice, 0), "1")
screen.onkeypress(functools.partial(update_user_choice, 1), "2")
screen.onkeypress(functools.partial(update_user_choice, 2), "3")
screen.onkeypress(functools.partial(update_user_choice, 3), "4")
screen.onkeypress(functools.partial(update_user_choice, 4), "5")
screen.onkeypress(functools.partial(update_user_choice, 5), "6")
screen.onkeypress(functools.partial(update_user_choice, 6), "7")
screen.onkeypress(functools.partial(update_user_choice, 7), "8")
screen.onkeypress(functools.partial(update_user_choice, 8), "9")
screen.listen()

# screen.onkeypress(functools.partial(update_message, 'testing'), "0")



screen.mainloop()

# turtle.Screen().exitonclick()
