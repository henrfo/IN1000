# Beskrivelse: Funksjoner som kan brukes i andre filer (addere, telle bokstaver i tekst)
# 1. adder(tall1, tall2) -> returnerer summen av to tall
# 2. og 3. tell_forekomst(min_tekst, min_bokstav) -> teller antall forekomster av en bokstav i en tekst (og skiller mellom liten og stor bokstav)


# 1.1
# Funksjon som adderer to heltall
def adder(tall1, tall2):
    return tall1 + tall2

# Test av addere-funksjonen
print(f"Resultat av addisjon av 2 og 3 er: {adder(2, 3)}")
print(f"Resultat av addisjon av 5 og 7 er: {adder(5, 7)}")



# 1.2 og 1.3
# Funksjon som looper gjennom tekst og teller forekomst av bokstav
def tell_forekomst(min_tekst, min_bokstav):
    teller = 0
    for tegn in min_tekst:
        if tegn == min_bokstav:
            teller += 1
    return teller

# Input fra bruker
min_tekst = input("Skriv inn tekst her: ")
min_bokstav = input("Skriv en bokstav her: ")

# Test av tell_forekomst-funksjon
antall = tell_forekomst(min_tekst, min_bokstav)
print(f"Bokstaven '{min_bokstav}' forekommer {antall} ganger i teksten.")