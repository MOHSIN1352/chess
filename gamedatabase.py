import sqlite3


# Connect to the database
conn = sqlite3.connect('chess1.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS game_moves(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             game_id INTEGER,
             move_number INTEGER,
             player TEXT,
             move TEXT,
             FOREIGN KEY (game_id) REFERENCES game_entries (id)
)''')



# Create a table to store the game entries
c.execute('''CREATE TABLE IF NOT EXISTS game_entries (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             player1 TEXT,
             player2 TEXT,
             winner TEXT,
             start_time TEXT,
             end_time TEXT
             )''')



def game_entries(player1, player2, winner, start_time, end_time):
    c.execute("INSERT INTO game_entries (player1, player2, winner, start_time, end_time ) VALUES (?, ?, ?, ?, ?)",(player1,player2,winner,start_time,end_time))
    conn.commit()

def game_moves(move_number,player,move):
    c.execute("INSERT INTO game_moves(move_number,player,move) VALUES (?, ?, ?)",(move_number,player,move))
    conn.commit()


'''player1 = input("Enter player name: ")
player2 = input("Enter player2 name: ")
winner =  random.choices(player1,player2)    #currently using random because the game development is not yet complete on the level
start_time =time.ctime()   #shows the current time of the computer
end_time = input("Enter end-time: ")'''

player1 = input("Enter player1:  ")
player2 = input("Enter player2: ")
winner = input("Enter the winner: ")
start_time = input("Enter the start time: ")
end_time = input("Enter the duration: ")


game_entries(player1, player2, winner, start_time, end_time)



player = input("Enter the player that made the move")
move_number = input("Enter the move number: ")
move = input("Enter the move name: ")

game_moves(move_number,player,move)


# Commit changes and close the connection
conn.commit()
conn.close()



