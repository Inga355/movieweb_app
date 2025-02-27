from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from data_management.data_manager_interface import DataManagerInterface

Base = declarative_base()


class User(Base):
    """
    Represents a user in the MovieWeb application.
    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        movies (relationship): The list of movies associated with the user.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    movies = relationship('Movie', back_populates='user', cascade='all, delete-orphan')


class Movie(Base):
    """
    Represents a movie associated with a user.
    Attributes:
        id (int): The unique identifier of the movie.
        user_id (int): The ID of the user who owns this movie.
        name (str): The name of the movie.
        director (str): The director of the movie.
        year (int): The year of release.
        rating (float): The rating of the movie.
        poster (str, optional): The URL of the movie poster.
    """
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    director = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    poster = Column(String, nullable=True)
    user = relationship('User', back_populates='movies')


class SQLiteDataManager(DataManagerInterface):
    """
    Handles database operations using SQLite and SQLAlchemy.
    Attributes:
        engine (Engine): SQLAlchemy engine for the SQLite database.
        Session (sessionmaker): Factory for creating new session objects.
    """
    def __init__(self, db_file_name):
        """
        Initializes the database connection and creates tables if they do not exist.
        :param: db_file_name (str): The name of the SQLite database file.
        """
        self.engine = create_engine(f'sqlite:///{db_file_name}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_all_users(self):
        """
        Retrieves all users from the database.
        :return:  A list of all User objects.
        """
        session = self.Session()
        users = session.query(User).all()
        session.close()
        return users

    def get_user_by_id(self, user_id):
        """
        Retrieves a user by their ID.
        :param: user_id (int): The ID of the user.
        :return: The User object or None if not found.
        """
        session = self.Session()
        user = session.query(User).filter_by(id=user_id).first()
        session.close()
        return user

    def get_user_movies(self, user_id):
        """
        Retrieves all movies associated with a given user.
        :param: user_id (int): The ID of the user.
        :return: A list of Movie objects.
        """
        session = self.Session()
        movies = session.query(Movie).filter_by(user_id=user_id).all()
        session.close()
        return movies

    def add_user(self, name):
        """
        Adds a new user to the database.
        :param: name (str): The name of the new user.
        :return: The ID of the newly created user.
        """
        session = self.Session()
        new_user = User(name=name)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        session.close()
        return new_user.id

    def delete_user(self, user_id):
        """
        Deletes a user and all their associated movies from the database.
        :param: user_id (int): The ID of the user to delete.
        """
        session = self.Session()
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()

    def get_movie_by_id(self, movie_id):
        """
        Retrieves a movie by its ID.
        :param: movie_id (int): The ID of the movie.
        :return: The Movie object or None if not found.
        """
        session = self.Session()
        movie = session.query(Movie).filter_by(id=movie_id).first()
        session.close()
        return movie

    def add_movie(self, user_id, name, director, year, rating, poster):
        """
        Adds a new movie to the database.
        :param: user_id (int): The ID of the user adding the movie.
        :param: name (str): The title of the movie.
        :param: director (str):  The director of the movie.
        :param: year (int): The release year of the movie.
        :param: rating (float): The rating of the movie, using imdbRating.
        :param: poster (str): The URL of the movie poster.
        :return: The ID of the newly added movie.
        """
        session = self.Session()
        new_movie = Movie(user_id=user_id, name=name, director=director, year=year, rating=rating, poster=poster)
        session.add(new_movie)
        session.commit()
        session.refresh(new_movie)
        session.close()
        return new_movie.id

    def delete_movie(self, movie_id):
        """
        Deletes a movie from the database.
        :param: movie_id (int): The ID of the movie to delete.
        """
        session = self.Session()
        movie = session.query(Movie).filter_by(id=movie_id).first()
        if movie:
            session.delete(movie)
            session.commit()
        session.close()

    def update_movie(self, movie_id, name=None, director=None, year=None, rating=None):
        """
        Updates an existing movie's details in the database.
        :param: movie_id (int):The ID of the movie to update.
        :param: name (str): The new title of the movie (optional).
        :param: director (str): The new director of the movie (optional).
        :param: year (int): The new release year of the movie (optional).
        :param: rating (float): The new rating of the movie (optional).
        :return:
        """
        session = self.Session()
        movie = session.query(Movie).filter_by(id=movie_id).first()
        if movie:
            if name:
                movie.name = name
            if director:
                movie.director = director
            if year:
                movie.year = year
            if rating:
                movie.rating = rating
            session.commit()
        session.close()
