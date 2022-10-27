import turtle
import random
import functools
import time

def run_game():

    # Setup Turtle Screen
    screen = turtle.Screen()
    screen.title('Tic Tac Toe')
    screen.bgcolor("NavajoWhite2")
    screen.setup(width=800, height=800)

    delay = 0.1

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
    message.write("It's your turn first.", align='center', font=('Courier', 12, 'normal'))

    #Draw Player (X and O) Symbols
    def write_x(x, y, color = 'black'):
        turtle.color(str(color), 'black')
        turtle.up()
        turtle.hideturtle()
        turtle.goto(x, y)
        turtle.write('X',
        align='center', font=('Courier', 90, 'normal'))

    def write_o(x, y, color = 'black'):
        turtle.color(str(color), 'black')
        turtle.up()
        turtle.hideturtle()
        turtle.goto(x, y)
        turtle.write('O',
        align='center', font=('Courier', 90, 'normal'))

    #Variables:
    board_coordinates = ((-133.17, 166.5), (0, 166.5),
                        (133.34, 166.5), (-133.17, 33), (0, 33), (133.34, 33), (-133.34, -100), (0, -100), (133.34, -100))
    board_status = ["", "", "",
                    "", "", "",
                    "", "", ""]
    winner = False

    # Testing Only -- To Delete Later:
    # write_o(board_coordinates[0][0], board_coordinates[0][1], 'black')

    # write_x(board_coordinates[0][0], board_coordinates[0][1], 'black')

    # for item in board_coordinates:
    #     write_x(item[0], item[1], 'black')

    #Functions:

    # Check for Win or Tie:

    # Check Rows:
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

    # Check Columns:
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

    # Check Diagonals:
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
        if board_status[index_val] == "":
            board_status[index_val] = "X"
            write_x(board_coordinates[index_val][0],
                    board_coordinates[index_val][1], 'black')
            status = check_status("X")
            if winner is False or status:
                computer_turn()
            return
        elif board_status[index_val] == "O":
            update_message("Please choose a valid number.")
            return
        elif board_status[index_val] == "X":
            update_message(
                "Number previously selected. Please choose a valid number.")
            return

    def check_status(player):
        row_result = checkRow()
        column_result = checkColumn()
        diagonal_result = checkDiagonal()

        # Check Row
        if row_result:
            #Highlight the winning values:
            if player == 'X':
                for i in row_result:
                    write_x(board_coordinates[i][0],
                    board_coordinates[i][1], ('green'))
            else:
                for i in row_result:
                    write_o(board_coordinates[i][0],
                    board_coordinates[i][1], ('green'))
            # Update the message on the screen:
            update_message(f"{player} has won the game.")
            #Terminate the game:
            terminate_game()
            return False
    
        #Check Column
        elif column_result:
            # Highlight the winning values:
            if player == 'X':
                for i in column_result:
                    write_x(board_coordinates[i][0],
                            board_coordinates[i][1], ('green'))
            else:
                for i in column_result:
                    write_o(board_coordinates[i][0],
                            board_coordinates[i][1], ('green'))
            # Update the message on the screen:
            update_message(f"{player} has won the game.")
            # Terminate the game:
            terminate_game()
            return False

        #Check Diagonal
        elif diagonal_result:
            # Highlight the winning values:
            if player == 'X':
                for i in diagonal_result:
                    write_x(board_coordinates[i][0],
                            board_coordinates[i][1], ('green'))
            else:
                for i in diagonal_result:
                    write_o(board_coordinates[i][0],
                            board_coordinates[i][1], ('green'))
            # Update the message on the screen.
            update_message(f"{player} has won the game.")
            # Terminate the game:
            terminate_game()
            return False

        #Check for a Tie
        elif "" not in board_status:
            update_message(f"The game has ended in a tie.")
            # Terminate the game:
            terminate_game()
            return False
        else:
            return True

    def computer_turn():
        while True:
            position = random.randint(0, 8)
            if board_status[position] == "":
                write_o(board_coordinates[position][0],
                board_coordinates[position][1], ('black'))
                board_status[position] = "O"
                check_status("O")
                if not winner:
                    update_message("It's your turn again.")
                return 
            elif winner:
                return
            else:
                continue

    def update_message(text):
        message.clear()
        message.write(text,
        align='center', font=('Courier', 12, 'normal'))
        
    def terminate_game():
        global board_status, winner

        time.sleep(4)
        # turtle.Screen().clear()
        turtle.Screen().reset()
        board_status = ["", "", "",
                        "", "", "",
                        "", "", ""]
        winner = False
        exit()
        # screen.bye()
        # turtle.done()
        # run_game()
        # return

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

    screen.mainloop() #Keeps the program running until exited.

# screen.onkeypress(functools.partial(update_message, 'testing'), "0")

# screen.mainloop()

run_game()
# screen.mainloop()


# turtle.Screen().exitonclick()
