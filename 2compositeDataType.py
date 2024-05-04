class Movie:
    def __init__(self, title, year, have_watched, genres, director, cast):
        self.title = title
        self.year = year
        self.have_watched = have_watched
        self.genres = genres
        self.director = director
        self.cast = cast

def print_movie_info(movie):
    print("Title:", movie.title)
    print("Year of Release:", movie.year)
    print("Genres:", ', '.join(movie.genres))
    print("Director:", movie.director)
    print("Have Watched:", "Yes" if movie.have_watched else "No")
    print("Cast:")
    for actor, role in movie.cast.items():
        print("- {} as {}".format(actor, role))

def main():
    # Creating a movie instance
    movie = Movie(
        title="Inception",
        year=2010,
        have_watched=True,
        genres=["Action", "Adventure", "Sci-Fi"],
        director="Christopher Nolan",
        cast={"Leonardo DiCaprio": "Dom Cobb", "Ellen Page": "Ariadne", "Tom Hardy": "Eames"}
    )

    # Printing movie information
    print("Movie Information:")
    print_movie_info(movie)

if __name__ == "__main__":
    main()
