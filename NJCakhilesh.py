import sqlite3
connection=sqlite3.connect('FavMovies.db')
cursor=connection.cursor()


command1=""" CREATE TABLE IF NOT EXISTS FavMovies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT, director TEXT,year INTEGER) """

cursor.execute(command1)


cursor.execute(" INSERT INTO FavMovies VALUES ('Airlift','Akshay Kumar','Nimrat Kaur','Raja Krishna Menon',2016)")
cursor.execute(" INSERT INTO FavMovies VALUES ('Chichorre','Sushant Singh Rajput','Shradha kapoor','Nitesh Tiwari',2019)")
cursor.execute(" INSERT INTO FavMovies VALUES ('Mimi','Panakj Tripati','Kriti Sanon','Laxman Utekar',2021)")
cursor.execute(" INSERT INTO FavMovies VALUES ('Inception','LeonardoDeCaprio','Marion Cotillard','Cristopher Nolan',2010)")



cursor.execute("SELECT * FROM FavMovies")
results=cursor.fetchall()


cursor.execute("SELECT * FROM FavMovies WHERE actor='Amitabh Bachchan' ")
results2=cursor.fetchall()

#print the results
print(results)

print(results2)