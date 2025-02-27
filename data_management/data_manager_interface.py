from abc import ABC, abstractmethod

class DataManagerInterface(ABC):

    @abstractmethod
    def get_all_users(self):
        """Returns a list of all users."""
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        """Returns all movies for a given user."""
        pass

    def get_user_by_id(self, user_id):
        """Returns a user identified by ID"""
        pass

    @abstractmethod
    def add_user(self, name):
        """Adds a new user and returns the user ID."""
        pass

    @abstractmethod
    def delete_user(self, user_id):
        """Deletes a user and all their movies."""
        pass

    def get_movie_by_id(self, movie_id):
        """Returns a movie identified by ID"""
        pass

    @abstractmethod
    def add_movie(self, user_id, name, director, year, rating, poster):
        """Adds a movie to a specific user."""
        pass

    @abstractmethod
    def delete_movie(self, movie_id):
        """Deletes a movie by its ID."""
        pass

    @abstractmethod
    def update_movie(self, movie_id, name=None, director=None, year=None, rating=None):
        """Updates movie details, allowing partial updates."""
        pass
