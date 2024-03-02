from tkinter import *
import random

def next_turn(row, column): # Function to handle the next turn of the game
    # row and columns are the passing arguments hence added here
    global player

    # Check if the button clicked is empty and there's no winner yet
    if buttons[row][column]['text'] == "" and check_winner() is False:
        # Set the button text to the current player's symbol (X or O)
        buttons[row][column]['text'] = player

        # If there's no winner yet, switch to the next player's turn
        if check_winner() is False:
            if player == "X":
                player = "O"
                label.config(text=("O"+"'s Turn"))
            else:
                player = "X"
                label.config(text=("X"+"'s Turn"))
        else: # If there's a tie, display "Tie" and change button colors to red
            if check_winner() == "Tie":
                label.config(text="Tie")
                for r in range(3):
                    for c in range(3):
                        buttons[r][c].config(bg="red")
            else: # If there's a winner, display who won and highlight winning buttons in green
                label.config(text=(f"{player} Wins"))
                highlight_winner_buttons()

#######################################################################################################
def highlight_winner_buttons(): # Function to highlight the winning buttons in green
    # Check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return

    # Check columns
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return

    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return

#######################################################################################################
def check_winner(): # Function to check for a winner or a tie
# check all of the different win conditions
# return TRUE if Win and FALSE if no winner yet and TIE if its a Tie

# we need to check the text of each button in each row
    for row in range(3): # check the Horizontal win conditions i.e. if 3 values are same then its a win
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    for row in range(3): # check the Vertical win conditions i.e. if 3 values are same then its a win
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True

    # check the Diagonal (Left-Right) win conditions i.e. if 3 values are same then its a win
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    # check the Diagonal (Right-Left) win conditions i.e. if 3 values are same then its a win
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    elif not empty_spaces(): # If there are no empty spaces left, it's a tie
        return "Tie"
    else:
        return False

#######################################################################################################
def empty_spaces(): # Function to check if there are any empty spaces left
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

#######################################################################################################
def new_game(): # Function to start a new game

    global player
    player = random.choice(players)
    label.config(text=player+"'s Turn")

    # we have to reset all buttons
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

#######################################################################################################

# Initialize the Tkinter window
window = Tk()
window.title("Tic-Tac-Toe")

# list of players
players = ["X", "O"]
player = random.choice(players)

# 2D list of buttons
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

# Label to display whose turn it is
label = Label(text= player + "'s turn", font = ('monotype corsiva' , 40))
label.pack(side="top")

# Button to restart the game
reset_button = Button(text="Restart Game", font=("calibri", 20), command= new_game) #command will call the "new_game" function
reset_button.pack(side="top")

# Frame to hold the buttons
frame = Frame(window)
frame.pack()

# Create buttons in a grid layout
for row in range(3):
    # inner for loop is incharge of columns
    for column in range(3):
        #we're adding buttons to the frame and frame to the window
        buttons[row][column] = Button(frame, text="", font=("calibri", 20), width=5, height=2,
                                      command = lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row,column=column)

# Start the Tkinter event loop
window.mainloop()
