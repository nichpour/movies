import webbrowser

#creating the class Movie, which will be imported to the favorite movies doc
class Movie():

    #initializing the instance, once it's created
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #opening the trailer from the web browser using the imported webbrowser feature .open
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
