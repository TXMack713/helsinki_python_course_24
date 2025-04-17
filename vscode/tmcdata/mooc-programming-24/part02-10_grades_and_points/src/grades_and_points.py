# Write your solution here
score = int(input("How many points [0-100]:"))

if 0 > score or score > 100:
    print("Grade: impossible!")
elif 0 < score < 50:
    print("Grade: fail")
elif 50 <= score <= 59:
    print("Grade: 1")
elif 60 <= score <= 69:
    print("Grade: 2")
elif 70 <= score <= 79:
    print("Grade: 3")
elif 80 <= score <= 89:
    print("Grade: 4")
elif 90 <= score <= 100:
    print("Grade: 5")

