import pygame
import sqlite3


# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((850, 800))
pygame.display.set_caption("Database Viewer")

# Connect to the database
conn = sqlite3.connect('users2.db')
cursor = conn.cursor()

def get_players():
    # Retrieve all players from the database
    cursor.execute('SELECT * FROM users')
    players = cursor.fetchall()
    return players

def display_players(players):
    # Display the players on the Pygame screen
    font = pygame.font.Font(None, 24)           #creates a new font object from the file
    y = 50
    for player in players:
        player_text = f"ID: {player[0]} | email: {player[1]}  | player1: {player[2]} | player2: {player[3]} | password: {player[4]}"
        text_surface = font.render(player_text, True, (0, 0, 0))    #font.render draws a new text on the surface
        screen.blit(text_surface, (50, y))
        y += 30

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))    #fills the color white as the background

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Retrieve and display the players from the database
    players = get_players()
    display_players(players)

    pygame.display.flip()     #update the full display surface to the screen

# Close the database connection
conn.close()

# Quit Pygame
pygame.quit()

