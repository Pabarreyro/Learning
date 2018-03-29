#  Construct website with favorite movies containing:
#  1. Title
#  2. Synopsis
#  3. Poster image
#  4. Trailer -  opens youtube trailer (function = )
#  Construct the parent class here and access it from another file
import webbrowser


class Movie:  # We will access this by importing the file and passing media.Movie()
    """Provides warehouse to store movie-related information. """  # Provides __doc__ info

    VALID_RATINGS = {"G", "PG", "PG-13", "R", "NR"}  # Predefined class variable

    def __init__(self, title, synopsis, poster_img_url, trailer_url):
        self.title = title
        self.synopsis = synopsis
        self.poster = poster_img_url
        self.trailer = trailer_url

    def play_trailer(self):
        webbrowser.open(self.trailer)  # Opens browser and opens trailer url


