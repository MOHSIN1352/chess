import pygame
import sqlite3

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Connect to the database
conn = sqlite3.connect('chess1.db')
c = conn.cursor()

# Retrieve all game entries from the database
c.execute('SELECT * FROM game_entries')
entries = c.fetchall()

# Display the game entries in the Pygame screen
font = pygame.font.SysFont('Arial', 20)
y = 50
for entry in entries:
    player1 = entry[1]
    player2 = entry[2]
    winner = entry[3]
    start_time = entry[4]
    duration = entry[5]


    text = f"| {player1} vs {player2} | winner: {winner} | start time: {start_time} | duration: {duration} | "
    
    label = font.render(text, True, (0 ,0, 0))
    screen.fill((255, 255, 255))
    screen.blit(label, (50, y))
    y += 30

# Update the Pygame display
pygame.display.update()

# Wait for the user to close the Pygame window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            conn.close()
            quit()
