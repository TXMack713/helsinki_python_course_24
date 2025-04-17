# Write your solution here
def create_tuple(x: int, y: int, z: int):
    
    my_list = [x, y, z]
    my_list.sort()
    sum = 0
    for x in my_list:
        sum += x
    the_tuple = (my_list[0], my_list[2], sum)
    return the_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
