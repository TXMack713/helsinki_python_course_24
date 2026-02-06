#!usr/bin/env python 3

def sort_by_seasons(items: list):
    def season_sorter(items: list):
        return items["seasons"]

    return sorted(items, key=season_sorter)

if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    for show in sort_by_seasons(shows):
        print(f"{show['name']} {show['seasons']} seasons")# Write your solution here:
