#!/usr/bin/env python 3

class Series():
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.ratings_average = 0

    def __str__(self):
        genre_list = self.genres
        genre_string = ", ".join(genre_list)
        if len(self.ratings) == 0:
            return f"{self.title} ({self.seasons} seasons)\n" \
            f"genres: {genre_string}\n" \
            "no ratings"
        else:
            return f"{self.title} ({self.seasons} seasons)\n" \
            f"genres: {genre_string}\n" \
                f"{len(self.ratings)} ratings, average {self.ratings_average:.1f} points"

    def rate(self, rating: int):
        if rating < 0 or rating > 5:
            raise ValueError("Invalid rating, ratings can only range from 0 to 5.")
        else:
            self.ratings.append(rating)
            self.ratings_total = 0
            for rate in self.ratings:
                self.ratings_total += rate
            self.ratings_average = self.ratings_total / len(self.ratings)

def minimum_grade(rating: float, series_list: list):
    searched_list = []
    for series in series_list:
        if series.ratings_average >= rating:
            searched_list.append(series)
    
    return searched_list

def includes_genre(genre: str, series_list: list):
    searched_list = []
    for series in series_list:
        for series_genre in series.genres:
            if series_genre == genre:
                searched_list.append(series)
            
    return searched_list


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    # print(s1.ratings_average)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
    # dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # dexter.rate(4)
    # dexter.rate(5)
    # dexter.rate(5)
    # dexter.rate(3)
    # dexter.rate(0)
    # print(dexter)
