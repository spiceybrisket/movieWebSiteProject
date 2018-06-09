import webbrowser


class Movie():
    """This class provides a way to store movie related information

    Attributes:
        movie_title (str): A string of the movies title.
        movie_storyline (str): A string of the movies storyline.
        poster_image (str): A URL for the movies poster image`.
        trailer_youtube (str): A URL from the movies trailer on youtube`.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
