# egenoppgave.py

from regnefunksjoner import tommer_til_cm

# Oppgavetekst
# Lag et program som henter inn skredderdata, konverter til tommer og legger det i en ordbok

filnavn = "skredder_data.csv" 

# 6.1
def skredder_mål_cm(filnavn):
    skredder_data_cm = {}

    with open(filnavn, "r", encoding="utf-8") as fil:
        for linje in fil:
            kolonner = linje.strip().split(",")
            navn = kolonner[0]
            mål = float(kolonner[1])
            skredder_data_cm[navn] = mål
    return skredder_data_cm


def skredder_mål_tommer(skredder_data_cm):
    skredder_data_tommer = {navn: tommer_til_cm(mål) for navn, mål in skredder_data_cm.items()}
    return skredder_data_tommer

print("Mål i cm:", skredder_data_cm)
print("Mål i tommer:", skredder_data_tommer)