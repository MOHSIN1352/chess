

import sqlite3

# Create a connection to the database
conn = sqlite3.connect('users2.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create a users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             email TEXT UNIQUE NOT NULL,
             username TEXT UNIQUE NOT NULL,
             username2 TEXT UNIQUE NOT NULL,
             password TEXT NOT NULL
             )''')

# Function to add a new user to the database
def add_user(email,username, username2, password):
    c.execute("INSERT INTO users (email, username, username2, password) VALUES (?, ?, ?, ?)",
              (email, username, username2, password))
    conn.commit()
    #print("Registered successfully!")

# Function to check if a username and password match
def login(email, username,username2, password):
    c.execute("SELECT * FROM users WHERE email=? AND username=? AND username2=? AND password=?", (email, username, username2, password))
    result = c.fetchone()
    if result:
        print("Registration successful!")
        return result[0] # return the user's ID
    else:
        print("Incorrect username or password.")
        return None
    


email = input("Enter your email: ")
username = input("Enter first player: ")
username2 = input("Enter second player:")
password = input("Enter your password:")


# Example usage
add_user(email, username,username2, password)
login(email, username,username2, password)

    


