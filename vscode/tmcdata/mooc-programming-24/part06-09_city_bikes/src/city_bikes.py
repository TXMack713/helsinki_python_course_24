# Write your solution here
import math

def get_station_data(filename: str):
    file_input = []
    station_info = {}
    if filename == "":
        filename = "stations1.csv"

    with open(filename) as file:
        for line in file:
            # print("Line info", line)
            line_input = line.split(";")
            file_input.append(line_input)
        
    count = 1
    while count < len(file_input):
        station_info[file_input[count][3]] = (float(file_input[count][0]), float(file_input[count][1]))
        # print(file_input[count])
        count += 1

    # print("Station Info", station_info)
    return station_info

def distance(stations: dict, station1: str, station2: str):
    lat1 = stations[station1][1]
    lat2 = stations[station2][1]
    long1 = stations[station1][0]
    long2 = stations[station2][0]
    x_km = (long1-long2) * 55.26
    y_km = (lat1-lat2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    start_station = ""
    end_station = ""
    station_list = []
    for key, value in stations.items():
        station_list.append(key)
    for station in station_list:
        for key, value in stations.items():
            if key == station:
                continue
            else:
                current_distance = distance(stations, station, key)
                # print("Current distance", current_distance, station, key)
                if current_distance >= max_distance:
                    start_station = station
                    end_station = key
                    max_distance = current_distance
    return (start_station, end_station, max_distance)


if __name__ == "__main__":
    station_data = get_station_data("stations1.csv")
    d1 = distance(station_data, "Designmuseo", "Hietalahdentori")
    print(d1)
    d2 = distance(station_data, "Viiskulma", "Kaivopuisto")
    print(d2)
    station1, station2, greatest = greatest_distance(station_data)
    print(station1, station2, greatest)
