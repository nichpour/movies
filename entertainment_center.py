# importing fresh tomatoes for the HTML and media for the Movie class.

import media
import fresh_tomatoes


# creating new instances of the Movie class.
inglorious_basterds = media.Movie(
    "Inglorious Basterds",
    "Jews get revenge on Nazis",
    "https://i.ebayimg.com/00/s/NzEwWDUyMA==/z/yzsAAOSwXeJYCqxO/$_58.JPG",
    "https://www.youtube.com/watch?v=KnrRy6kSFF0")
pulp_fiction = media.Movie(
    "Pulp Fiction", "Gangsters, Boxers, and Drugs",
    "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_"
    "poster.jpg",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
killers = media.Movie(
    "Killers Remake",
    "Sean/Logan's remake video of Read My Mind",
    "https://68.media.tumblr.com/32fa29e7865de2702c75ffb9bda1b432/"
    "tumblr_n64ybhTCCx1twcq4no1_500.png",
    "https://www.youtube.com/watch?v=nnKiycA7urc")

# making an array of all the movie instances.
movie_array = [inglorious_basterds, pulp_fiction, killers]

# running the fresh tomotoes open function with the movie array.
fresh_tomatoes.open_movies_page(movie_array)
