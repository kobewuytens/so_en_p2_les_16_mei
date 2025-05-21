from abc import ABC, abstractmethod

class Persoon(ABC):
    def __init__(self, naam):
        self._naam = naam

    def get_naam(self):
        return self._naam

    def __str__(self):
        return self._naam

class Kandidaat(Persoon):
    def __init__(self, naam):
        super().__init__(naam)
        self._stemmen = []

    def geef_stem(self, stem):
        self._stemmen.append(stem)

    def aantal_stemmen(self):
        return len(self._stemmen)

    def __str__(self):
        return f"{self._naam} ({self.aantal_stemmen()} stemmen)"

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self._faculteit = faculteit

    def get_faculteit(self):
        return self._faculteit

    def __str__(self):
        return f"{self._naam} - {self._faculteit} ({self.aantal_stemmen()} stemmen)"

class Stem:
    def __init__(self, kandidaat):
        self._kandidaat = kandidaat

    def __str__(self):
        return f"Stem op {self._kandidaat}"

class Kiezer(Persoon):
    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self._naam} heeft gestemd op {kandidaat}")

# ---- Simulatie ----

# Maak kandidaten aan
kandidaten = [
    DecaanKandidaat("Sophie De Winne", "Economie"),
    DecaanKandidaat("Prof. Janssens", "Letteren"),
    DecaanKandidaat("Dr. Vermeulen", "Ingenieurswetenschappen")
]

# Maak kiezers aan
kiezers = [
    Kiezer("Anna"),
    Kiezer("Bram"),
    Kiezer("Chloe"),
    Kiezer("Daan"),
    Kiezer("Emma")
]

# Laat kiezers stemmen
import random
for kiezer in kiezers:
    gekozen_kandidaat = random.choice(kandidaten)
    kiezer.stem(gekozen_kandidaat)

# Resultaten tonen
print("\n--- Verkiezingsresultaten decaan ---")
for kandidaat in kandidaten:
    print(kandidaat)
