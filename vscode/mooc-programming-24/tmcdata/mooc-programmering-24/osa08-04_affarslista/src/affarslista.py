# ÄNDRA INTE NEDANSTÅENDE KLASS Affarslista!
# Skriv din lösning under klassen!
class Affarslista:
    def __init__(self):
        self.foremalen = []

    def mangden_foremal(self):
        return len(self.foremalen)

    def tillagg(self, foremal: str, mangd: int):
        self.foremalen.append((foremal, mangd))

    def foremal(self, n: int):
        return self.foremalen[n - 1][0]

    def mangd(self, n: int):
        return self.foremalen[n - 1][1]

# ----------------------
# Skapa din lösning här:
# ----------------------
