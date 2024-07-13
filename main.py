import tkinter
from tkinter import messagebox
class TicTacToe:
    def __init__(self,root):
        self.root = root;
        self.root.title("Tic Tac Toe Game")
        self.curr_player = 'X'
        self.buttons = []
        self.turn_label = ''
        self.create_widget()
        
        
    def create_widget(self):
        self.turn_label = tkinter.Label(self.root, text=f"Player {self.curr_player}'s turn", font=('Arial', 18))
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)
        for row in range(3):
            button_row = []
            # self.buttons.append([])
            for col in range(3):
                button = tkinter.Button(self.root, text="", font=('Arial', 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_next_move(r, c))
                button.grid(row=row+1,column=col,padx=5,pady=5)
                button_row.append(button)
            self.buttons.append(button_row)
            for but in self.buttons:
                print(but)
            
    def on_next_move(self,row,col):
        
        print(f"{row+1}  and {col+1} was clicked")
        # row = row - 1
        # col = col 
        
        # 
                     
        # print(flag)
        
        if self.buttons[row][col].cget('text')=="":
            self.buttons[row][col].config(text=self.curr_player)
            # check if the move was valid and check if the winner is getting declared
            flag = True
            for i in range(3):
                for j in range(3):
                    if self.buttons[i][j].cget('text') != 'X' and self.buttons[i][j].cget('text') != 'O':
                        flag = False
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.curr_player} wins!")
                self.reset_game()
            elif flag==True:
                messagebox.showinfo("Tic-Tac-Toe", "Draw!")
                self.reset_game()
            else:
                self.curr_player = 'O' if self.curr_player=='X' else 'X'
                
        self.turn_label.config(text=f"Player {self.curr_player}'s turn")
                
                
                

            
    
    def check_winner(self):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                                [0, 4, 8], [2, 4, 6]] # Diagonals
        
        for comb in winning_combinations:
            if self.buttons[comb[0]//3][comb[0]%3].cget('text') == self.buttons[comb[1]//3][comb[1]%3].cget('text') == self.buttons[comb[2]//3][comb[2]%3].cget('text') != "":
                return True
        return False
    
    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
        self.curr_player = 'X'
        
            
        
        
if(__name__ == "__main__"):
    root = tkinter.Tk()
    app = TicTacToe(root)
    root.mainloop()
                
                
        
