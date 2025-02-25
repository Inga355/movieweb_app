from flask import Flask, render_template
from data_management.sqlite_data_manager import SQLiteDataManager
import requests

app = Flask(__name__)
db_manager = SQLiteDataManager('data/movieapp.db')
OMDB_API_KEY = "api_key"
OMDB_API_URL = "http://www.omdbapi.com/?apikey={}&t={}"


@app.route('/')
def home():
    users = db_manager.get_all_users()
    return render_template('users.html', users=users)


@app.route('/users/<int:user_id>')
def user_movies(user_id):
    user = db_manager.get_user_by_id(user_id)
    movies = db_manager.get_user_movies(user_id)
    return render_template('user_movies.html', user=user, movies=movies)







if __name__ == '__main__':
    app.run(debug=True)
