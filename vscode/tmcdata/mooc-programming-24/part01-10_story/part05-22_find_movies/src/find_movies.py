# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie_info = {}
    movie_info["name"] = name
    movie_info["director"] = director
    movie_info["year"] = year
    movie_info["runtime"] = runtime
    database.append(movie_info)

def find_movies(database: list, search_term: str):
    movie_list = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            movie_list.append(movie)
    return movie_list

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)