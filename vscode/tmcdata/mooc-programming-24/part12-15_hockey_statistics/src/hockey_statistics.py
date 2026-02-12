#!/usr/bin/env python 3

import json

def get_file():
    file_name = input("Please enter the name of the file: ")
    with open(file_name) as file:
        data = file.read()

    stats = json.loads(data)
    file.close()
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
                    return f"{player["name"]:20} {player["team"]:>3} {player["goals"]:3} + {player["assists"]:>2} =  {points:>2}"
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
        return self.__stats

    def most_goals(self):
        return self.__stats

def order_by_games(item: list):
    return item["games"]

def order_by_points(item: list):
    players = {}
    final_list = []
    for player in item:
        points = player["assists"] + player["goals"]
        if points not in players:
            players[points] = []
            players[points].append(player)
        else:
            players[points].append(player) 
    for point, persons in players.items():
        point_list = sorted(persons, key=order_by_goals)
        for entry in point_list:
            final_list.append(entry)
    return final_list

def order_by_goals(item: list):
    players = {}
    final_list = []
    for player in item:
        goals = item["goals"]
        if goals not in players:
            players[goals] = []
            players[goals].append(player)
        else:
            players[goals].append(player) 
    for goal, persons in players.items():
        goal_list = sorted(persons, key=order_by_games)
        for entry in goal_list:
            final_list.append(entry)
    return final_list

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
            team_players = sorted(self.__stats.team_players(team), key = order_by_points, reverse = True)
            for player in team_players:
                print(self.__stats.get_player(player["name"].strip()))
        except ValueError:
            self.erroneous_input()

    def get_country_players(self):
        country = input("Country abbreviation: ")
        try:
            country_players = sorted(self.__stats.country_players(country), key = order_by_points, reverse = True)
            for player in country_players:
                print(self.__stats.get_player(player["name"].strip()))
        except ValueError:
            self.erroneous_input()

    def most_points(self):
        how_many = int(input("how many: "))
        players = sorted(self.__stats.most_points(), key = order_by_points, reverse = True)
        count = 0
        while count < how_many:
            player = players[count]
            print(self.__stats.get_player(player["name"].strip()))
            count += 1

    def most_goals(self):
        how_many = int(input("how many: "))
        players = sorted(self.__stats.most_goals(), key = order_by_goals, reverse = True)
        count = 0
        while count < how_many:
            player = players[count]
            print(self.__stats.get_player(player["name"].strip()))
            count += 1

    def execute(self):
        while True:
            print("")
            command = input("command: ")
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

