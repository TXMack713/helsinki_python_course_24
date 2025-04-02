# Write your solution here
def oldest_person(people: list):
    birth_year = []
    for x in people:
        birth_year.append(x[1])
    birth_year.sort()
    oldest = ""
    for person in people:
        if person[1] == birth_year[0]:
            oldest = person[0]
    return oldest

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))