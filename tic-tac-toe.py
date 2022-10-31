import turtle
import random
import functools
import time

# Setup Turtle Screen
screen = turtle.Screen()
screen.title('Tic Tac Toe')
screen.bgcolor("azure2")
screen.bgcolor("AliceBlue")
screen.bgcolor("beige")
screen.setup(width=800, height=800)

delay = 0.1

#Draw Board
board = turtle.Turtle()
board.shape('circle')
board.pensize(3)
board.penup()
board.goto(-200, 166.5)
board.color('antiquewhite4')
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

#Instruction Text
instructions = turtle.Turtle()
instructions.color('SkyBlue4')
instructions.up()
instructions.hideturtle()
instructions.goto(0, -300)
instructions.write('Please select a number between 1 - 9. You are player "X".', align='center', font=('Times New Roman', 18, 'normal'))

#Message Screen
message = turtle.Turtle()
message.color('ForestGreen')
message.up()
message.hideturtle()
message.goto(0, -250)
message.write("It's your turn first.", align='center', font=('Times New Roman', 20, 'italic'))

#Variables:
board_coordinates = ((-133.17, 166.5), (0, 166.5),
                        (133.34, 166.5), (-133.17, 33), (0, 33), (133.34, 33), (-133.34, -100), (0, -100), (133.34, -100))
board_status = ["", "", "",
                "", "", "",
                "", "", ""]
board_turtles = []
winner = False

#Functions:

#Draw Player (X and O) Symbols:

def write_x(x, y, color = 'black'):
    global board_turtles
    turtle.color(str(color), 'black')
    turtle.up()
    turtle.hideturtle()
    turtle.goto(x, y)
    turtle.write('X',
    align='center', font=('Courier', 90, 'normal'))
    board_turtles.append(turtle)

def write_o(x, y, color = 'black'):
    global board_turtles
    turtle.color(str(color), 'black')
    turtle.up()
    turtle.hideturtle()
    turtle.goto(x, y)
    turtle.write('O',
    align='center', font=('Courier', 90, 'normal'))
    board_turtles.append(turtle)

# Check for Win or Tie:

def checkRow():
    global winner

    if board_status[0] == board_status[1] == board_status[2] and board_status[0] != "":
        winner = board_status[0]
        return [0, 1, 2]
    elif board_status[3] == board_status[4] == board_status[5] and board_status[3] != "":
        winner = board_status[3]
        return [3, 4, 5]
    elif board_status[6] == board_status[7] == board_status[8] and board_status[6] != "":
        winner = board_status[6]
        return [6, 7, 8]
    else:
        return False

def checkColumn():
    global winner
    if board_status[0] == board_status[3] == board_status[6] and board_status[0] != "":
        winner = board_status[0]
        return [0, 3, 6]
    elif board_status[1] == board_status[4] == board_status[7] and board_status[1] != "":
        winner = board_status[1]
        return [1, 4, 7]
    elif board_status[2] == board_status[5] == board_status[8] and board_status[2] != "":
        winner = board_status[3]
        return [2, 5, 8]
    else:
        return False

def checkDiagonal():
    global winner
    if board_status[0] == board_status[4] == board_status[8] and board_status[0] != "":
        winner = board_status[0]
        return [0, 4, 8]
    elif board_status[2] == board_status[4] == board_status[6] and board_status[4] != "":
        winner = board_status[2]
        return [2, 4, 6]
    else:
        return False

def update_user_choice(index_val):
    if board_status[index_val] == "" and winner is False:
        board_status[index_val] = "X"
        write_x(board_coordinates[index_val][0],
                board_coordinates[index_val][1], 'black')
        return True
    elif board_status[index_val] == "O":
        update_message("Please choose a valid number.")
        return False
    elif board_status[index_val] == "X":
        update_message(
            "Number previously selected. Please choose a valid number.")
        return False

def check_status(player):
    row_result = checkRow()
    column_result = checkColumn()
    diagonal_result = checkDiagonal()

    if row_result:
        # Change Winning Values to Another Color:
        if player == 'X':
            for i in row_result:
                write_x(board_coordinates[i][0],
                board_coordinates[i][1], ('LightSalmon3'))
        else:
            for i in row_result:
                write_o(board_coordinates[i][0],
                board_coordinates[i][1], ('LightSalmon3'))
        update_message(f"{player} has won the game.")
        return True
    #Check Column:
    elif column_result:
        # Change Winning Values to Another Color:
        if player == 'X':
            for i in column_result:
                write_x(board_coordinates[i][0],
                        board_coordinates[i][1], ('LightSalmon3'))
        else:
            for i in column_result:
                write_o(board_coordinates[i][0],
                        board_coordinates[i][1], ('LightSalmon3'))
        update_message(f"{player} has won the game.")
        return True
    #Check Diagonal
    elif diagonal_result:
        # Change Winning Values to Another Color:
        if player == 'X':
            for i in diagonal_result:
                write_x(board_coordinates[i][0],
                        board_coordinates[i][1], ('LightSalmon3'))
        else:
            for i in diagonal_result:
                write_o(board_coordinates[i][0],
                        board_coordinates[i][1], ('LightSalmon3'))
        update_message(f"{player} has won the game.")
        return True
    #Check for a Tie
    elif "" not in board_status:
        update_message(f"The game has ended in a tie.")
        return True
    # No win in any direction:
    else:
        return False

def computer_turn():
    def update_board(position):
        write_o(board_coordinates[position][0],
                board_coordinates[position][1], ('black'))
        board_status[position] = "O"
        check_status("O")
        if not winner and "" in board_status:
            update_message("It's your turn again.")
            return
        else:
            return

    double_pairs = ((0, 1, 2), (1, 2, 0), (0,2,1), (3, 4, 5), (3, 5, 4), (4, 5, 3), (6, 7, 8), (6, 8, 7), (7, 8, 6), (0, 4, 8), (4, 8, 0), (0, 8, 4), (2, 4, 6), (2, 6, 4), (6, 4, 2), (0, 3, 6), (3, 6, 0), (0, 6, 3), (1, 4, 7), (1, 7, 4), (4, 7, 1), (2, 5, 8), (5, 8, 2), (2, 8, 5))
    # Check for Self Double Pairs:
    for position in double_pairs:
        if board_status[position[0]] == "O" and board_status[position[1]] == "O" and board_status[position[2]] == "":
            update_board(position[2])
            return
    # Block Opponent Double Pairs:
    for position in double_pairs:
        if board_status[position[0]] == "X" and board_status[position[1]] == "X" and board_status[position[2]] == "":
            update_board(position[2])
            return
    #Take middle position if it's available:
    if board_status[4] == "":
        update_board(4)
        return
    # Random Move if No Conditions Above Were Met:
    while True:
        position = random.randint(0, 8)
        if board_status[position] == "":
            update_board(position)
            return
        else:
            continue

def update_message(text):
    message.clear()
    message.write(text, align='center', font=('Times New Roman', 20, 'italic'))

def restart_game():
    global board_status, winner
    time.sleep(4)
    board_status = ["", "", "",
                    "", "", "",
                    "", "", ""]
    winner = False
    update_message(f"New game. Please make your selection.")
    # Clear the board of X and O turtles:
    for turtle in board_turtles: 
        turtle.clear()
    return

def run_game(keypress_val):
    #Checks if a valid keypress selection was made:
    keypress_result = update_user_choice(keypress_val)
    if keypress_result:
        selection_result = check_status("X")
        if selection_result:
            restart_game()
            return
        # If the player didn't win, the computer will take a turn:
        if winner is False and "" in board_status:
            computer_turn()
            computer_result = check_status("O")
            if winner or "" not in board_status or computer_result:
                restart_game()
                return

# Keypress Event Listeners
screen.onkeypress(functools.partial(run_game, 0), "1")
screen.onkeypress(functools.partial(run_game, 1), "2")
screen.onkeypress(functools.partial(run_game, 2), "3")
screen.onkeypress(functools.partial(run_game, 3), "4")
screen.onkeypress(functools.partial(run_game, 4), "5")
screen.onkeypress(functools.partial(run_game, 5), "6")
screen.onkeypress(functools.partial(run_game, 6), "7")
screen.onkeypress(functools.partial(run_game, 7), "8")
screen.onkeypress(functools.partial(run_game, 8), "9")
screen.listen()

screen.mainloop() #Keeps the program running until exited as the program waits for keypress events.