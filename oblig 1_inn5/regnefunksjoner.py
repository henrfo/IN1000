# Regnefunksjoner

# 3.1
def addisjon(tall1, tall2):
    return tall1 + tall2


# 3.2
# subtraksjon
def subtraksjon(tall1, tall2):
    return tall1 - tall2

# divisjon
def divisjon(tall1, tall2):
    return tall1 / tall2

# Asserts for subtraksjon
assert subtraksjon(10, 5) == 5
assert subtraksjon(-10, -5) == -5
assert subtraksjon(-10, 2) == -12

# Asserts for divisjon
assert divisjon(10, 2) == 5
assert divisjon(-10, -1) == 10
assert divisjon(-10, 2) == -5



# 3.3
def tommer_til_cm(tommer):
    assert tommer > 0, "Verdien må være større enn null" # gir beskjed til bruker om tall > 0
    return tommer * 2.54

# Test av funksjonen
assert tommer_til_cm(1) == 2.54
assert tommer_til_cm(2) == 5.08
assert tommer_til_cm(10) == 25.4



# 3.4
def skriv_beregninger():
    # Funksjon som tar inn to tall fra bruker, og utfører addisjon, subtraksjon, divisjon

    print("Utregninger: ")
    tall1 = float(input("Skriv inn tall nr 1 her: "))
    tall2 = float(input("Skriv inn tall nr 2 her: "))

    # Resultat av addisjon, subtraksjon, divisjon
    print(f"Resultatet av summering er: {addisjon(tall1, tall2)}")
    print(f"Resultatet av subtraksjon er: {subtraksjon(tall1, tall2)}")
    print(f"Resultatet av divisjon er: {divisjon(tall1, tall2)}")

    # Resultatet av tommer til cm
    print("Kovertering fra tommer til cm: ")
    tommer = float(input("Skriv inn et tall: "))
    print(f"Resultatet av tommer til cm er: {tommer_til_cm(tommer)}")


# 3.5 - test av skriv_beregninger-programmet
skriv_beregninger()