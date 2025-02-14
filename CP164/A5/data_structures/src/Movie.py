"""
-------------------------------------------------------
Movie class definition.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""


class Movie:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    MIN_RATING = 0
    MAX_RATING = 10
    FIRST_YEAR = 1888
    GENRES = ("science fiction", "fantasy", "drama",
              "romance", "comedy", "zombie", "action",
              "historical", "horror", "war", "mystery")
    # Defines a range of valid integer genre codes:
    GENRE_CODES = range(len(GENRES))

    @staticmethod
    def genres_menu():
        """
        -------------------------------------------------------
        Creates a string of Movie genres in the format:
           0 science fiction
           1 fantasy
           2 drama
           ...
        Use: s = Movie.genres_menu()
        Use: print(Movie.genres_menu())
        -------------------------------------------------------
        Returns:
            string - A numbered string of Movie genres.
        -------------------------------------------------------
        """
        string = "Genres\n"

        for i in range(len(Movie.GENRES)):
            string += f"""{i:2d} {Movie.GENRES[i]}
"""
        return string

    def __init__(self, title, year, director, rating, genres):
        """
        -------------------------------------------------------
        Initializes a Movie object.
        Use: movie = Movie(title, year, director, rating, genres)
        -------------------------------------------------------
        Parameters:
            title - movie title (str)
            year - year of release (int)
            director - name of director (str)
            rating - rating of 1 - 10 from IMDB (float)
            genres - numbers representing movie genres_menu (list of int)
        Returns:
            A new Movie object (Movie)
        -------------------------------------------------------
        """
        assert year >= Movie.FIRST_YEAR, f"Movie year must be >= {Movie.FIRST_YEAR}"
        assert rating is None or Movie.MIN_RATING <= rating <= Movie.MAX_RATING, \
            f"Movie ratings must be between {Movie.MIN_RATING} and {Movie.MAX_RATING}"
        assert genres is None or genres == [] or \
            min(genres) in Movie.GENRE_CODES, \
            f"Invalid genre code {min(genres)}"
        assert genres is None or genres == [] or \
            max(genres) in Movie.GENRE_CODES, \
            f"Invalid genre code {max(genres)}"

        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genres = genres

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of movie data.
        Use: print(movie)
        Use: print( "{}".format(movie))
        Use: string = str(movie)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of movie (str)
        -------------------------------------------------------
        """
        # Generate the list of genres as a string.
        genres_list = self.genres_string()

        string = f"""Title:    {self.title}
Year:     {self.year}
Director: {self.director}
Rating:   {self.rating}
Genres:   {genres_list}"""
        return string

    def __eq__(self, other):
        """
        -------------------------------------------------------
        Compares this movie against another movie for equality.
        Use: movie == other
        -------------------------------------------------------
        Parameters:
            other - other movie to compare to (Movie)
        Returns:
            result - True if title and year match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) == \
            (other.title.lower(), other.year)
        return result

    def __lt__(self, other):
        """
        -------------------------------------------------------
        Determines if this movie comes before another movie.
        Use: movie < other
        -------------------------------------------------------
        Parameters:
            other - movie to compare to (Movie)
        Returns:
            result - True if movie precedes other, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.title.lower(), self.year) < \
            (other.title.lower(), other.year)
        return result

    def __le__(self, other):
        """
        -------------------------------------------------------
        Determines if this movie precedes or is or equal to another movie.
        Use: movie <= other
        -------------------------------------------------------
        Parameters:
            other - movie to compare to (Movie)
        Returns:
            result - True if this movie precedes or is equal to other,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self < other or self == other
        return result

    def genres_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of genres based upon the
        current movie object's integer genres list.
        e.g.: [0, 2] returns "science fiction, drama"
        Use: string = movie.genres_string()
        -------------------------------------------------------
        Returns:
            string - string of genres (str)
        -------------------------------------------------------
        """
        string = ""

        if self.genres is not None:

            for genre in self.genres[:-1]:
                string += Movie.GENRES[genre] + ", "
            # do last genre separately to avoid trailing comma
            string += Movie.GENRES[self.genres[-1]]
        return string

    def genres_list_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of genre indexes based upon the
        current movie object's integer genres list.
        e.g.: [0, 2] returns "0,2"
        Use: string = movie.genres_list_string()
        -------------------------------------------------------
        Returns:
            string - string of genre indexes (str)
        -------------------------------------------------------
        """
        string = ""

        if self.genres is not None:

            for genre in self.genres[:-1]:
                string += str(genre) + ","
            # do last genre separately to avoid trailing comma
            string += str(self.genres[-1])
        return string

    def write(self, fv):
        """
        -------------------------------------------------------
        Writes a single line of movie data to an open file fv
        in the format
              title|year|director|rating|code
        Use: movie.write(fv)
        -------------------------------------------------------
        Parameters:
            fv - an already open file of movie data (file)
        Returns:
            None
        -------------------------------------------------------
        """
        fv.write("{}|{}|{}|{}|{}\n"
                 .format(self.title, self.year, self.director,
                         self.rating, self.genres_list_string()))
        return

    def key(self):
        """
        -------------------------------------------------------
        Creates a formatted string of movie key data.
        Use: key = movie.key()
        -------------------------------------------------------
        Returns:
            string - the formatted contents of movie key (str)
        -------------------------------------------------------
        """
        string = f"{self.title}, {self.year}"
        return string

    def __hash__(self):
        """
        -------------------------------------------------------
        Generates a hash value from a movie name.
        Use: h = hash(movie)
        -------------------------------------------------------
        Returns:
            value - the total of the characters in the name string
                multiplied by the year (int > 0)
        -------------------------------------------------------
        """
        value = 0

        for c in self.title:
            value = value + ord(c)
        value *= self.year
        return value
