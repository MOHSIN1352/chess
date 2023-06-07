import pygame
import sys
import sqlite3
import tkinter as tk


from tkinter import messagebox
from const import *
from game import Game
from square import Square
from move import Move



# Database connection (replace with your own code)
conn = sqlite3.connect('login2.db')

conn.execute('''CREATE TABLE IF NOT EXISTS users 
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL)''')


class Main:


    time_taken = pygame.time.get_ticks()

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainLoop(self):

        screen = self.screen
        game = self.game
        board=self.game.board
        dragger = self.game.dragger

        while True:      
            #show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                #click event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE


                    #if clicked the square has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        #valid piece (color)?
                        if piece.color == game.next_player:

                         board.calc_moves(piece, clicked_row, clicked_col,bool=True)
                         dragger.save_initial(event.pos)   #if any invalid move is played then it returned to the initial position 
                         dragger.drag_piece(piece)
                         #show methods
                         game.show_bg(screen)
                         game.show_last_move(screen)
                         game.show_moves(screen)
                         game.show_pieces(screen)

                #mouse motion
                elif event.type == pygame.MOUSEMOTION:   #it only works when the  piece and the position are saved in the above event type
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE
                    game.set_hover(motion_row,motion_col) 

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #show methoods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)

                #release event

                elif event.type == pygame.MOUSEBUTTONUP:

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        #create possible move
                        initial = Square(dragger.initial_row , dragger.initial_col)
                        final = Square(released_row , released_col)
                        move = Move(initial,final)

                        #asking if it is a valid move or not
                        if board.valid_move(dragger.piece, move):
                            #normal capture
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)

                            board.set_true_en_passant(dragger.piece)

                            #sounds
                            game.play_sound(captured)
                            #show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)  
                            #next turn
                            game.next_turn()

                    dragger.undrag_piece()



                #key press
                elif event.type == pygame.KEYDOWN:

                    #changing themes
                    if event.key == pygame.K_t:
                        game.change_theme()

                    #restart game
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board=self.game.board
                        dragger = self.game.dragger



                #quit application
                elif event.type ==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

           
            pygame.display.update()        



# Registration function
def register():
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the username already exists in the database
    cursor = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone() is not None:
        messagebox.showerror("Registration Error", "Username already exists. Please choose another one.")
        return
    
    # Add the new user to the database
    conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    messagebox.showinfo("Registration Successful", "Registration successful.")


# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the username and password match a user in the database
    cursor = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

    c = cursor.fetchone()
    if c:
        messagebox.showinfo("Login Successful", "Login successful.")
        window.destroy() #closes the window
        main = Main()
        main.mainLoop()
    else:
        messagebox.showerror("Login Error", "Invalid login credentials. Please try again.")

# Create the main window
window = tk.Tk()
window.geometry("800x800")
window.title("Login/Register")

# Username label and entry
username_label = tk.Label(window, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(window)
username_entry.pack(pady=10)
  
# Password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=10)

# Register button
register_button = tk.Button(window, text="Register", command=register)
register_button.pack(pady=10)

# Login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=10)


if __name__ == '__main__':
    window.mainloop()




# Close the database connection when the program exits
conn.close()

