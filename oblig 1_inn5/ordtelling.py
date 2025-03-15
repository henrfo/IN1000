# Funksjoner som teller antall bokstaver i ord, forekomst av ord i setning,
# og et hovedprogram "ordprogram", som teller ord i setning m.m.


# 2.1
def antall_bokstaver(ord):
    # returnerer antall bokstaver i ord
    return len(ord)

# Test av funksjonen 2.1
#print(antall_bokstaver("Heiaaaa"))
                    


# 2.2
def ordtelling (setning):
    # ordbok som teller forekomst av ord i setning
    ord_liste = setning.split() # deler setning opp i liste av ord
    ordbok = {} # oppretter en tom ordbok

    for ord in ord_liste:
        if ord in ordbok:
            ordbok[ord] += 1 # hvis ordet er i ordboken, øk antall med 1
        else:
            ordbok[ord] = 1 # hvis ikke, legg til ord med verdi 1

    return ordbok

# Test av funksjonen 2.2
#print(ordtelling("Hei på deg, hei på meg, hei til alle!"))



# 2.3
def ordprogram():
# program som tar inn setning fra bruker, teller ord i setning (2.2), frekvens av hvert unike ord,
# og hvor mange bokstaver i ordet (2.1).

    bruker_input = input("Skriv inn setning her: ") # input fra bruker

# Totalt antall ord per setning
    ord_liste = bruker_input.split() # deler setning opp i liste av ord
    antall_ord = len(ord_liste) # teller antall ord i setning
    print(f"Antall ord i setningen er: {antall_ord}")

# Ordtelling-funksjon - forekomst av hvert unike ord
    ord_frekvens = ordtelling(bruker_input) # funksjon fra 2.2
    print("Forekomsten av hvert unike ord:")
    for ord, antall in ord_frekvens.items():
        print(f"{ord}: {antall} ganger")

# Antall_bokstaver-funksjon - teller antall bokstaver per ord
    for ord in ord_liste:
        print(f"Ordet '{ord}' har {antall_bokstaver(ord)} bokstaver.") # funksjon fra 2.1

# Test av funksjonen 2.3
ordprogram()