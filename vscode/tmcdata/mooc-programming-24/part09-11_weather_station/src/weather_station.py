#!usr/bin/env python 3

class WeatherStation():
    def __init__(self, name: str):
        self.__name = name
        self.__observations = []
    
    def add_observation(self, observation: str):
        if observation != "":
            self.__observations.append(observation)
        else:
            raise ValueError("Error! The observation field cannot be empty!")
        
    def latest_observation(self):
        if len(self.__observations) != 0:
            return self.__observations[-1]
        else:
            return ""
    
    def number_of_observations(self):
        return len(self.__observations)
    
    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
