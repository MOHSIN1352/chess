import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='Mohsin@1352',
                              host='localhost', database='itachi')
cursor = cnx.cursor()

# Retrieve all rows from the table
query = "SELECT * FROM best_chess_games"
cursor.execute(query)
for row in cursor:
    print(row)

# Close the cursor and database connection
cursor.close()
cnx.close()
