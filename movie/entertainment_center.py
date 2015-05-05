import media             # Import the Media class that defines the object Movie
import fresh_tomatoes

# Define instance of object movie: Toy Story

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "www.youtube.com/watch?v=KYz2wyBy3kc")

# Define instance of object movie: Avatar


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "www.youtube.com/watch?v=cRdxXPV9GNQ")

# Define instance of object movie: Prestige

prestige = media.Movie("Prestige",
                     "A story about rivalry between magician brothers",
                     "http://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                     "www.youtube.com/watch?v=o4gHCmTQDVI")

# Define instance of object movie: Interstellar

interstellar = media.Movie("Interstellar",
                     "A story about Space and time continuom",
                     "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                     "www.youtube.com/watch?v=zSWdZVtXT7E")

# Define instance of object movie: EuroTrip

eurotrip = media.Movie("EuroTrip",
                     "A story about Europe Trip",
                     "http://upload.wikimedia.org/wikipedia/en/d/db/Eurotrip_movie.jpg",
                     "www.youtube.com/watch?v=e9khnXfKf7g")


# Define instance of object movie: The Dark Knight

darkknight = media.Movie("The Dark Knight",
                     "A story about good and evil",
                     "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [toy_story, avatar, prestige, interstellar, eurotrip, darkknight]
fresh_tomatoes.open_movies_page(movies)
#print(toy_story.VALID_RATINGS)

