# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie_info = {}
    movie_info["name"] = name
    movie_info["director"] = director
    movie_info["year"] = year
    movie_info["runtime"] = runtime
    database.append(movie_info)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)