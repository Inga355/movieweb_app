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


@app.route('/users')
def users():
    users = db_manager.get_all_users()
    return render_template('users.html')





if __name__ == '__main__':
    app.run(debug=True)
