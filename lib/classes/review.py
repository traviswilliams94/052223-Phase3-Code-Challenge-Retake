# from classes.movie import Movie
# from classes.viewer import Viewer

class Review:

    all = []
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        Review.all.append(self)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if type(rating) == int and 1 <= rating <= 5:
            self._rating = rating
        else:
            raise Exception

    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        from classes.viewer import Viewer
        if type(viewer) == Viewer:
            self._viewer = viewer
        else:
            raise Exception

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        from classes.movie import Movie
        if type(movie) == Movie:
            self._movie = movie
        else:
            raise Exception

