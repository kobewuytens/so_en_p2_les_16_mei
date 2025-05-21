class Kandidaat:
    def __init__(self, naam):
        self._naam = naam
        self._stemmen = []

    def geef_stem(self, stem):
        self._stemmen.append(stem)

    def aantal_stemmen(self):
        return len(self._stemmen)

    def get_naam(self):
        return self._naam

    def __str__(self):
        return f"{self._naam} ({self.aantal_stemmen()} stemmen)"


class Stem:
    def __init__(self, kandidaat):
        self._kandidaat = kandidaat

    def __str__(self):
        return f"Stem op {self._kandidaat.get_naam()}"


class Kiezer:
    def __init__(self, naam):
        self._naam = naam

    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self._naam} heeft gestemd op {kandidaat.get_naam()}")


# ----------------------------
# Kandidaten aanmaken
# ----------------------------
kandidaten = [
    Kandidaat("Severine Vermeire"),
    Kandidaat("Peter Lievens"),
    Kandidaat("Tine Baelmans")
]

# ----------------------------
# Kiezers aanmaken
# ----------------------------
kiezers = [
    Kiezer("Dirk"),
    Kiezer("Jan"),
    Kiezer("Maria")
]

# ----------------------------
# Stemmen laten uitbrengen
# ----------------------------
kiezers[0].stem(kandidaten[0])  # Kobe stemt op Jan
kiezers[1].stem(kandidaten[1])  # Tina stemt op Fatima
kiezers[2].stem(kandidaten[0])  # Ahmed stemt op Jan

# ----------------------------
# Resultaten tonen
# ----------------------------
print("\nStemresultaten:")
for kandidaat in kandidaten:
    print(kandidaat)
