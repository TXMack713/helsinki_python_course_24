# write your solution here
def read_fruits():
    fruits = {}
    with open("fruits.csv") as file:
        for line in file:
            # data = line.readline()
            data_separated = line.split(";")
            fruits[data_separated[0]] = float(data_separated[1])
    return fruits

if __name__ == "__main__":
    read_fruits()
