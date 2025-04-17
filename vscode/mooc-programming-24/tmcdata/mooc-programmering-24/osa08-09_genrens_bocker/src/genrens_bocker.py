# ÄNDRA INTE NEDANSTÅENDE KLASS Bok
# Skapa din lösning efter Bok-klassen

class Bok:
    def __init__(self, namn: str, forfattare: str, genre: str, ar: int):
        self.namn = namn
        self.forfattare = forfattare
        self.genre = genre
        self.ar = ar

    # Detta möjliggjör en vettig utskrift för bokobjekt med print-funktionen
    def __repr__(self):
        return f"{self.namn} ({self.forfattare}), {self.ar} - genre: {self.genre}"

# -----------------------------
# Skapa din lösning här
