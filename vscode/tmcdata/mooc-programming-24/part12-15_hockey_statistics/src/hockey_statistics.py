#!/usr/bin/env python 3

import json

def get_file():
    file_name = input("Please enter the name of the file: ")
    with open(file_name) as file:
        data = file.read()
    
    stats = json.loads(data)
    print(f"read the data of {len(stats)} players")
    # print(f"Stats: {stats}")
    # for entry in stats:
    #     print(entry)
    return stats

# player_info = get_file()

class PlayerStat:
    def __init__(self):
        self.__stats = get_file()

    def get_player(self, name: str):
        for player in self.__stats:
            try:
                if player["name"] == name:
                    points = player["assists"] + player["goals"]
                    return f"{player["name"]:20} {player["team"]:3} {player["goals"]:3} + {player["assists"]:1} = {points}"
            except:
                raise ValueError()
    
    def teams(self):
        return list(set([entry["team"] for entry in self.__stats]))
    
    def countries(self):
        return list(set([entry["nationality"] for entry in self.__stats]))

    def team_players(self, team: str):
        players = [entry for entry in self.__stats if entry["team"] == team]
        if len(players) == 0:
            raise ValueError ("Team does not exist in list")
        else:
            return players

    def country_players(self, nationality: str):
        players = [entry for entry in self.__stats if entry["nationality"] == nationality]
        if len(players) == 0:
            raise ValueError ("Country does not exist in list")
        else:
            return players

    def most_points(self):
        max_points = 0
        max_player = ""
        for entry in self.__stats:
            if (entry["assists"] + entry["goals"]) >= max_points:
                max_points = entry["assists"] + entry["goals"]
                max_player = entry
        return max_player

    def most_goals(self):
        max_goals = 0
        max_player = ""
        for entry in self.__stats:
            if entry["goals"] >= max_goals:
                max_goals = entry["goals"]
                max_player = entry
        return max_player

class PlayerStatApplication:
    def __init__(self):
        self.__stats = PlayerStat()

    def help(self):
        print("")
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search_for_player(self):
        try:
            name = input("name: ")
            player = self.__stats.get_player(name.strip())
            print(player)
        except ValueError:
            self.erroneous_input()

    def get_teams(self):
        teams = self.__stats.teams()
        for team in sorted(teams):
            print(team)
    
    def get_countries(self):
        countries = self.__stats.countries()
        for country in sorted(countries):
            print(country)

    def get_team_players(self):
        team = input("Team abbreviation: ")
        try:
            team_players = sorted(self.__stats.team_players(team))
            for player in team_players:
                print(player)
        except ValueError:
            self.erroneous_input()

    def get_country_players(self):
        country = input("Country abbreviation: ")
        try:
            country_players = sorted(self.__stats.country_players(country))
            for player in country_players:
                print(player)
        except ValueError:
            self.erroneous_input()

    def most_points(self):
        player = self.__stats.most_points()
        print(player)

    def most_goals(self):
        player = self.__stats.most_goals()
        print(player)

    def execute(self):
        while True:
            print("")
            command = input("command:")
            if command == "0":
                break
            elif command == "1":
                self.search_for_player()        
            elif command == "2":
                self.get_teams()            
            elif command == "3":
                self.get_countries()
            elif command == "4":
                self.get_team_players()
            elif command == "5":
                self.get_country_players()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            else:
                self.help()
    
    def erroneous_input(self):
        print("erroneous input")
        # self.execute()

application = PlayerStatApplication()
application.help()
application.execute()

