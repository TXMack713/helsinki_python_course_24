# Korrigera programmet
poang = int(input("Hur många poäng? "))
if poang < 100:
    poang *= 1.1
    print("Du fick 10 % i bonus")

if poang >= 100:
    poang *= 1.15
    print("Du fick 15 % i bonus")

print("Du har nu", poang, "poäng")
