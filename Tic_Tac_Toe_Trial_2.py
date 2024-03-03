import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        # Initialize the Tic Tac Toe game
        self.master = master
        self.master.title("Tic Tac Toe")  # Set the title of the window

        self.turn = 'X'  # Initialize the starting player
        self.board = [' ']*9  # Initialize the game board

        self.create_widgets()  # Create the GUI elements

    def create_widgets(self):
        # Create the graphical user interface (GUI) elements
        self.top_label = tk.Label(self.master, text="{}'s Turn".format(self.turn), font=("Monotype Corsiva", 30))
        # Label to display player's turn with larger font size
        self.top_label.pack()  # Pack the label onto the window

        self.buttons_frame = tk.Frame(self.master)  # Frame to hold the buttons
        self.buttons_frame.pack()  # Pack the frame onto the window

        self.buttons = []  # List to hold the buttons
        for i in range(3):
            row = []  # List to hold buttons in a row
            for j in range(3):
                button = tk.Button(self.buttons_frame, text='', width=10, height=4,
                                   font=("Calibri", 16),
                                   command=lambda i=i, j=j: self.on_button_click(i*3 + j))
                # Create a button with specified text, width, height, font, and command
                button.grid(row=i, column=j)  # Place the button in a grid layout
                row.append(button)  # Add the button to the row list
            self.buttons.append(row)  # Add the row to the buttons list

        self.restart_button = tk.Button(self.master, text="Restart", font=("Calibri", 20), command=self.restart)
        # Create a restart button with specified text, font, and command
        self.restart_button.pack()  # Pack the restart button onto the window

    def on_button_click(self, index):
        # Function to handle button clicks
        if self.board[index] == ' ':  # Check if the button is empty
            self.board[index] = self.turn  # Update the game board
            self.buttons[index // 3][index % 3].config(text=self.turn)
            # Update the button text to display the player's symbol
            if self.check_win():  # Check if a player has won
                self.display_winner()  # Display the winner
                self.disable_buttons()  # Disable all buttons
            elif self.check_tie():  # Check if the game is tied
                self.display_tie()  # Display the tie message
                self.disable_buttons()  # Disable all buttons
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'  # Switch player's turn
                self.top_label.config(text="{}'s Turn".format(self.turn))  # Update the turn label

    def disable_buttons(self):
        # Function to disable all buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)  # Disable the button

    def check_win(self):
        # Function to check if a player has won
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],
                 [0, 4, 8], [2, 4, 6]]  # Possible winning combinations

        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                # If all symbols in a winning combination are the same and not empty
                for index in line:
                    self.buttons[index // 3][index % 3].config(bg='green')
                    # Change the background color of winning buttons to green
                return True
        return False

    def check_tie(self):
        # Function to check if the game is tied
        return ' ' not in self.board  # If there are no empty spaces on the board

    def display_winner(self):
        # Function to display the winner
        winner = 'X' if self.turn == 'O' else 'O'  # Determine the winner
        self.top_label.config(text=f"{winner} Wins!")  # Update the turn label with winner message

    def display_tie(self):
        # Function to display the tie message
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(bg='red')  # Change the background color of all buttons to red
        self.top_label.config(text="It's a Tie!")  # Update the turn label with tie message

    def restart(self):
        # Function to restart the game
        self.turn = 'X'  # Reset the starting player
        self.board = [' ']*9  # Clear the game board
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', bg=self.master.cget('bg'), state=tk.NORMAL)
                # Reset the button text, background color, and enable all buttons
        self.top_label.config(text="{}'s Turn".format(self.turn))  # Update the turn label

def main():
    # Main function to create and run the game
    root = tk.Tk()  # Create the main window
    game = TicTacToe(root)  # Create an instance of the TicTacToe class
    root.mainloop()  # Run the Tkinter event loop

if __name__ == "__main__":
    main()
