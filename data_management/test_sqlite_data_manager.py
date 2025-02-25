from data_management.sqlite_data_manager import SQLiteDataManager

# Datenbank-Manager mit Test-Datenbank starten
db_manager = SQLiteDataManager("test_movieapp.db")

# Test: Nutzer hinzufügen
user_id = db_manager.add_user("Alice")
print(f"User Alice added with ID: {user_id}")

# Test: Alle Nutzer abrufen
users = db_manager.get_all_users()
print("All users:", [(user.id, user.name) for user in users])

# Test: Film für Nutzer hinzufügen
movie_id = db_manager.add_movie(user_id, "Inception", "Christopher Nolan", 2010, 9.0)
print(f"Movie Inception added with ID: {movie_id}")

# Test: Alle Filme für den Nutzer abrufen
movies = db_manager.get_user_movies(user_id)
print("Alice's movies:", [(movie.id, movie.name, movie.director, movie.year, movie.rating) for movie in movies])

# Test: Film aktualisieren
db_manager.update_movie(movie_id, rating=9.5)
updated_movies = db_manager.get_user_movies(user_id)
print("Updated movies:", [(movie.id, movie.name, movie.rating) for movie in updated_movies])

# Test: Film löschen
db_manager.delete_movie(movie_id)
movies_after_delete = db_manager.get_user_movies(user_id)
print("Movies after deletion:", [(movie.id, movie.name) for movie in movies_after_delete])

# Test: Nutzer löschen
db_manager.delete_user(user_id)
users_after_delete = db_manager.get_all_users()
print("Users after deletion:", [(user.id, user.name) for user in users_after_delete])
