# temperatur.py
import os

# 5.1

def hent_temperaturdok(filnavn):
    # Henter data fra maks temperatur per måned-csv og returnerer i en ordbok
    maks_temperaturer = {}
    with open(filnavn, "r", encoding="utf-8") as fil:
        for linje in fil:
            kolonner = linje.strip().split(",")
            måned = kolonner[0]
            temperatur = float(kolonner[1])
            maks_temperaturer[måned] = temperatur
    return  maks_temperaturer

# Finner mappe og fil
current_dir = os.path.dirname(__file__)
filnavn = os.path.join(current_dir, "max_temperatures_per_month.csv")

# Test av funksjonen
temperatur_data = hent_temperaturdok(filnavn)
print(temperatur_data)



# 5.2
# Prosedyre som tar inn to argumenter: ordbok med varmeste temperaturer, og fil som inneholder daglige temperaturer

def varmeste_temp(maks_temperaturer, filnavn):
    # ordbok med varmeste temperaturer og filnavn på fil med daglige temperaturer
    with open(filnavn, "r", encoding="utf-8") as fil:
        for linje in fil:
            kolonner = linje.strip().split(",")
            måned = kolonner[0]
            dag = kolonner[1]
            daglig_temperatur = float(kolonner[2])

            måned_dag = f"{dag} {måned}"

            if måned in maks_temperaturer and daglig_temperatur > maks_temperaturer[måned]:
                print(f"Ny varmerekord på {måned_dag}: {daglig_temperatur} grader celsius. "
                f"(gammel varmerekord var {maks_temperaturer[måned]} grader celsius).")

# Finner mappe og fil
filnavn_daglig = os.path.join(current_dir, "max_daily_temperature_2018.csv")

# test av funksjonen
varmeste_temp(temperatur_data, filnavn_daglig)
 

# 5.3

def oppdatert_varmeste_temp(maks_temperaturer, filnavn):
    # ordbok med varmeste temperaturer og filnavn på fil med daglige temperaturer
    with open(filnavn, "r", encoding="utf-8") as fil:
        for linje in fil:
            kolonner = linje.strip().split(",")
            måned = kolonner[0]
            dag = kolonner[1]
            daglig_temperatur = float(kolonner[2])

            if måned in maks_temperaturer and daglig_temperatur > maks_temperaturer[måned]:
                maks_temperaturer[måned] = daglig_temperatur

    return maks_temperaturer

# Finner mappe og fil
filnavn_daglig = os.path.join(current_dir, "max_daily_temperature_2018.csv")

# test av funksjonen
oppdatert_temp_data = oppdatert_varmeste_temp(temperatur_data, filnavn_daglig)

for måned in oppdatert_temp_data:
    if oppdatert_temp_data[måned] > temperatur_data[måned]:
        print(f"Ny varmerekord for {måned}: {oppdatert_temp_data[måned]} grader celsius.")

print(oppdatert_temp_data)