from abc import ABC, abstractmethod
import random

# Abstracte basisklasse
class Persoon(ABC):
    def __init__(self, naam):
        self._naam = naam

    def get_naam(self):
        return self._naam

    def __str__(self):
        return self._naam

# Kandidaatklasse
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

# Subklasse voor rectorverkiezing
class RectorKandidaat(Kandidaat):
    def __init__(self, naam):
        super().__init__(naam)

    # Extra logica zou hier kunnen komen als het nodig is
    # bv. een beleidsvisie of ervaring

# Stemklasse
class Stem:
    def __init__(self, kandidaat):
        self._kandidaat = kandidaat

    def __str__(self):
        return f"Stem op {self._kandidaat}"

# Kiezerklasse
class Kiezer(Persoon):
    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self._naam} heeft gestemd op {kandidaat}")

# ----------------------
# Simulatie van verkiezing
# ----------------------

# Lijst van kandidaten
kandidaten = [
    RectorKandidaat("Tine Baelmans"),
    RectorKandidaat("Peter Lievens"),
    RectorKandidaat("Severine Vermeire")
]

# Lijst van kiezers
kiezers = [
    Kiezer("Maarten"),
    Kiezer("Lotte"),
    Kiezer("Sophie"),
    Kiezer("Wouter"),
    Kiezer("Tom"),
    Kiezer("Julie")
]

# Laat elke kiezer stemmen op een willekeurige kandidaat
for kiezer in kiezers:
    keuze = random.choice(kandidaten)
    kiezer.stem(keuze)

# Resultaten tonen
print("\n--- Verkiezingsresultaten rector ---")
for kandidaat in kandidaten:
    print(kandidaat)
