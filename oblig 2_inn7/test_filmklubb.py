from film import Film
from filmklubb import Filmklubb

def testprogram():

    # __init__
    # Opprett Filmklubb-objekt
    print("oppretter Filmklubb-objekt")
    # <fyll ut og fjern # på print-setningen>
    klubb = Filmklubb()
    print()

    # les_filmer_fra_fil
    # Les inn filmer fra filen filmer.txt
    print("Leser filmer fra fil")
    # <fyll ut og fjern # på print-setningen>
    klubb.les_filmer_fra_fil("/Users/henrikformoe/Desktop/Desktop_M2/UiO_spring25/IN1000/oblig 2_inn7/filmer.txt")
    print()

    # skriv_ut_alle_filmer
    # Skriv ut all info om alle filmer, sjekk at alt er lest fra fil
    # <fyll ut>
    klubb.skriv_ut_alle_filmer()
    print()

    # registrer_film
    print("Registrerer ny film")
    # Legg inn en ny film med tittel og produksjonsår som leses fra terminal
    # <fyll ut og fjern # på print-setningen>
    klubb.registrer_film()
    print()
    # Skriv ut all info om alle filmer og sjekk at ny film ble registrert
    # <fyll ut>
    klubb.skriv_ut_alle_filmer()
    print()
    
    # Hvis _eq_ er implementert i Film og testes i registrer_film:
    print("Prøver å registrere film som allerede finnes")
    # <fyll ut og fjern # på print-setningen>
    klubb.registrer_film()
    print()    


    # finn_film_tittel
    print("Leter etter film med (start på) usannsynlig tittel")
    # Kall på metoden med et argument som ingen titler starter med
    # Bruk print eller assert for å sjekke at resultatet er som forventet
    # <fyll ut og fjern # på print-setningen>
    resultat = klubb.finn_film_tittel("TittelFinnesIkke")
    assert resultat == None
    print("Fant ingen filmer med denne titteleen")
    print()

    print("Leter etter film med (start på) tittel 'Hidden '")
    # Kall på metoden med argument "Hidden "
    # Bruk print eller assert for å sjekke at resultatet er som forventet
    # <fyll ut og fjern # på print-setningen>
    kjent_film = klubb.finn_film_tittel("Hidden ")
    assert kjent_film != None
    print()

    # legg_til_skuespillere
    print("Legg til skuespillere for en film" )
    # kall metoden på film-objektet du fikk returnert fra finn_film_tittel
    # (navn og rolle for to skuespillere du velger selv leses fra terminal)
    # <fyll ut og fjern # på print-setningen>
    klubb.legg_til_skuespillere(kjent_film)
    print()

    # Skriv ut all info om alle filmer og sjekk at resultatet er som forventet
    # <fyll ut>
    klubb.skriv_ut_alle_filmer()
    print()

    # finn_film_periode
    # Kall på metoden med argumentene etter=2000 og før=2024
    print("Leter ett filmer produsert etter 2000 og før 2024:")
    # Skriv ut titlene på filmer som returneres (bruk hent_tittel).
    # Kontroller at resultatene er som forventet
    # <fyll ut og fjern # på print-setningen>
    filmer = klubb.finn_filmer_periode(2000, 2024)
    for film in filmer:
        print(film.hent_tittel())
    print()

    # Kall på finn_film_periode med argumentene etter=2020 og før=2020
    print("Leter etter filmer produsert etter 2020 og før 2020:")
    # Kontroller at resultatet er som forventet (tom liste) med assert (evt skriv ut)
    # <fyll ut og fjern # på print-setningen>
    filmer = klubb.finn_filmer_periode(2020, 2020)
    assert len(filmer) == 0
    print()

    # Skriv ut all info om alle filmer og sjekk at resultatet er som forventet
    # <fyll ut>
    print("Oversikt over alle filmer:")
    klubb.skriv_ut_alle_filmer()

if __name__ == "__main__":
    testprogram()