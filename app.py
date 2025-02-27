from flask import Flask, render_template, request, redirect, url_for
from data_management.sqlite_data_manager import SQLiteDataManager
import requests
import os

app = Flask(__name__)
db_manager = SQLiteDataManager('data/movieapp.db')
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
OMDB_API_URL = "http://www.omdbapi.com/?apikey={}&t={}"


def fetch_movie_details(title):
    """
    Fetches movie details from OMDb API.
    :param: title (str): The title of the movie.
    :returns: dict: A dictionary with movie details (title, year, rating, poster) or None if not found.
    """
    response = requests.get(OMDB_API_URL.format(OMDB_API_KEY, title))
    movie_data = response.json()

    if movie_data.get("Response") == "True":
        return {
            "Title": movie_data["Title"],
            "Year": int(movie_data["Year"]),
            "Director": movie_data["Director"],
            "Rating": movie_data["imdbRating"] if movie_data["imdbRating"] != "N/A" else 0.0,
            "Poster": movie_data["Poster"]
        }
    else:
        return None


@app.route('/')
def home():
    """
    Renders the homepage displaying all users.
    :return: Rendered template for the homepage.
    """
    users = db_manager.get_all_users()
    return render_template('users.html', users=users)


@app.route('/users/<int:user_id>')
def user_movies(user_id):
    """
    Displays all movies of a specific user.
    :param: user_id (int): The ID of the user.
    :return: Rendered template displaying user's movies.
    """
    user = db_manager.get_user_by_id(user_id)
    movies = db_manager.get_user_movies(user_id)
    return render_template('user_movies.html', user=user, movies=movies)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    """
    Handles adding a new user.
    Displays a form (GET) and processes form submission (POST).
    :return: Redirects to home page after user creation or renders the form.
    """
    if request.method == 'POST':
        name = request.form['name']
        db_manager.add_user(name)
        return redirect(url_for('home'))
    return render_template('add_user.html')


@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """
    Deletes a user and redirects to the home page.

    :param user_id: The ID of the user to delete.
    :type user_id: int
    :return: Redirects to the home page.
    :rtype: flask.Response
    """
    db_manager.delete_user(user_id)
    return redirect(url_for('home'))



@app.route('/users/<int:user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id):
    """
    Handles adding a new movie for a user.
    Fetches movie details from OMDb API and saves the movie in the database.
    :param: user_id (int): The ID of the user who is adding the movie.
    :return: Rendered template displaying the add movie page.
    """
    movie = None
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        movie = fetch_movie_details(movie_name)
        print(movie)
        if movie:
            db_manager.add_movie(
                user_id,
                movie['Title'],
                movie['Director'],
                movie['Year'],
                movie['Rating'],
                movie['Poster']
            )
            return render_template('add_movie.html', user_id=user_id, movie=movie)
        else:
            return "Movie not found!", 404
    user = db_manager.get_user_by_id(user_id)
    return render_template('add_movie.html', user_id=user_id, movie=None)


@app.route('/users/<int:user_id>/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(user_id, movie_id):
    """
    Handles updating an existing movie for a user.
    Fetches the current movie details and allows editing.
    :param: user_id (int): The ID of the user.
    :param: movie_id (int): The ID of the movie to update.
    :return: Redirects to user's movie page after update or renders the form.
    """
    movie = db_manager.get_movie_by_id(movie_id)
    if request.method == 'POST':
        db_manager.update_movie(
            movie_id,
            name=request.form['name'],
            director=request.form['director'],
            year=int(request.form['year']),
            rating=float(request.form['rating'])
        )
        return redirect(url_for('user_movies', user_id=user_id))
    user = db_manager.get_user_by_id(user_id)
    return render_template('update_movie.html', user=user, movie=movie)


@app.route('/users/<int:user_id>/delete_movie/<int:movie_id>')
def delete_movie(user_id, movie_id):
    """
    Handles deleting a movie from a user's list.
    :param: user_id (int): The ID of the user.
    :param: movie_id (int): The ID of the movie to delete.
    :return:
    """
    db_manager.delete_movie(movie_id)
    return redirect(url_for('user_movies', user_id=user_id))


if __name__ == '__main__':
    app.run(debug=True)
