from statistics import mean

class Movie:
    
    all = []

    def __init__(self, title):
        self.title = title
        Movie.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if type(title) == str and len(title)  > 0:
            self._title = title
        else:
            raise Exception

    def reviews(self):
        from classes.review import Review
        return [review for review in Review.all if review.movie == self]
    
    def reviewers(self):
        from classes.review import Review
        return [review.viewer for review in self.reviews()]
    
    def average_rating(self):
        return mean([review.rating for review in self.reviews() if review.movie == self])

    @classmethod
    def highest_rated(cls):
        top_movie = None
        top_rating = 0
        for movie in cls.all:
            if movie.average_rating() > top_rating:
                top_rating = movie.average_rating()
                top_movie = movie
            
        return top_movie
