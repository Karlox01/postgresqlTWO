import psycopg2


# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()  # Cursor object is another way to say list or an array essentially anything we query from database will become part of cursor and we will have to use for loop to access it 

# Query 1 - select all records from the Artist" table
# cursor.execute('SELECT * FROM "Artist"') # Absolute must to use single quotes to wrap query , And double quotes to wrap values


# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" Table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" =  %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])


# Query 5 - Select only the albums with "ArtistId" #51 on the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])
 
# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(results)