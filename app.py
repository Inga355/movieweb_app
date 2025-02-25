from flask import Flask, render_template
from data_management.sqlite_data_manager import SQLiteDataManager

app = Flask(__name__)
data_manager = SQLiteDataManager('data/movieapp.db')


@app.route('/')
def home():
    return "Welcome to MovieWeb App!"


@app.route('/users')
def users():
    users = data_manager.get_all_users()
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug=True)
