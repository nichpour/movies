import webbrowser

# creating the class Movie, which will be imported to the favorite movies doc


class Movie():
    """This class defines the movie prperties and initiates the trailer"""

    # initializing the instance, once it's created
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        """The inputs for the movie are the title, storyline, poster image,
        and trailer"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    # opening the trailer from the web browser using the imported webbrowser
    def show_trailer(self):
        """the function opens the trailer URL"""
        webbrowser.open(self.trailer_youtube_url)
