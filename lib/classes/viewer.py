class Viewer:
    
    all = []

    def __init__(self, username):
        self.username = username
        Viewer.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if type(username) == str and 6 <= len(username) <= 16 and not hasattr(self, 'username'):
            self._username = username
        else:
            raise Exception

    def reviews(self):
        from classes.review import Review
        return [review for review in Review.all if review.viewer == self]
    
    def reviewed_movies(self):
        from classes.movie import Movie
        return [review.movie for review in self.reviews()]

    def has_reviewed_movie(self, movie):
        if movie in self.reviewed_movies():
            return True
        else: 
            return False
