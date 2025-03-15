# brukernavn.py
# Program for å legge til nye UiO-brukernavn


# 4.1
def lag_brukernavn(fullt_navn):
    # Funksjon som lager brukernavn basert på fullt navn
    fornavn, etternavn = fullt_navn.split() # splitter navnet i fornavn og etternavn
    brukernavn = (fornavn + etternavn[0]).lower() # setter sammen fornavn og etternavn, og gjør alt til små bokstaver
    return brukernavn

print(lag_brukernavn("Ola Nordmann"))
print(lag_brukernavn("Kari Nordmann"))


# 4.2
def lag_epost(brukernavn, suffix):
    return f"{brukernavn}@{suffix}"

print(lag_epost("olan", "uio.no"))
print(lag_epost("karin", "student.matnat.uio.no"))


# 4.3 - prosedyre skriv ut eposter
ordbok = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"} # ordbok med brukernavn og suffix
          
def skriv_ut_eposter(ordbok):
    for brukernavn, suffix in ordbok.items():
        epost = lag_epost(brukernavn, suffix)
        print(f"E-post for {brukernavn}: {epost}")

# Test av funksjonen
skriv_ut_eposter(ordbok)


# 4.4
# Ny ordbok for brukere
brukere = {}

# Kommando fra bruker
kommando = input("Skriv inn 'i' for å legge til bruker, 'p' for å vise epost, 's' for å avslutte:").strip().lower()

while kommando != "s": # Kjører frem til vi skriver "s" for å avslutte
    if kommando == "i":
        navn = input("Skriv inn navn: ").strip()
        suffix = input("Skriv inn epost-suffix: ").strip()
        brukernavn = lag_brukernavn(navn) # lager brukernavn
        brukere[brukernavn] = suffix # legger i ordboken
        print(f"Bruker {brukernavn} er lagt til")

    elif kommando == "p":
        skriv_ut_eposter(brukere) # skrive ut alle eposter

    else:
        print("Ugyldig kommando")

    # Ny kommando fra bruker
    kommando = input("Skriv inn 'i' for å legge til bruker, 'p' for å vise epost, 's' for å avslutte:").strip().lower()

print("Programmet avsluttes")