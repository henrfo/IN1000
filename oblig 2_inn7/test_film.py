from film import Film

def test_film():
    # __init__
    print("Oppretter to filmer")

    # Opprett to film-objekter med tittel og produksjonsår du velger selv
    film1 = Film("La Haine", 1995)
    film2 = Film("Stalker", 1979)

    print("Henter to filmer")
    print(f"Film 1: {film1.hent_tittel()} ({film1._år})")
    print(f"Film 2: {film2.hent_tittel()} ({film2._år})")
    # <fyll ut og fjern # på print-setningen>

    # hent_tittel
    # Skriv ut tittel på de to filmene
    print("Skriver ut titler på to filmer")
    print(f"Tittel på film 1: {film1.hent_tittel()}")
    print(f"Tittel på film 2: {film2.hent_tittel()}")
    # <fyll ut og fjern # på print-setningen>

    # ny_skuespiller
    # Legg til to skuespillere og deres roller for en av filmene, skriv ut alt om filmen
    print("Legger til to skuespillere og rolle i film 1")
    film1.ny_skuespiller("Vincent Cassel", "Vinz")
    film1.ny_skuespiller("Hubert Koundé", "Hubert")
    # print("Legger til to skuespillere")
    # <fyll ut og fjern # på print-setningen>
    print()

    # Prøv å legge inn en av skuespillerne igjen, med en ny rolle, og sjekk at rollen ikke blir endret
    print("Tester ulovlig innlegging av skuespiller")
    # <fyll ut og fjern # på print-setningen>
    film1.ny_skuespiller("Vincent Cassel", "Black Swan")


    # skriv_ut_film
    # Skriv ut all informasjon om begge filmer du har lagt inn
    print("Skriver ut all info om to filmer:")
    # <fyll ut og fjern # på print-setningen>
    film1.skriv_ut_film()
    film2.skriv_ut_film()
    print()

    # hent_alle_skuespiller_navn
    # Skriv ut skuespillernes navn for den filmen som har to
    print("Henter og skriver ut alle skuespillernavn for en film:")
    skuespillere = film1.hent_skuespiller_navn()
    print(skuespillere)
    # <fyll ut og fjern # på print-setningen>
    print()

    # sjekk_periode
    # Sjekk om en film du har lagt inn er i en periode du velger
    # (velg periode som skal gi True og sjekk at dette blir resultatet)
    print ("Sjekker at en film er i oppgitt periode")
    periode1 = film1.sjekk_periode(1990, 2000)
    print(f"Film 1 er fra perioden 1990-2000: {periode1}")
    # <fyll ut og fjern # på print-setningen>
    print()

    # Sjekk om en film er i en periode som skal gi False
    # (velg samme årstall til begge argumenter og sjekk resultat er False)
    print ("Sjekker at en film ikke kan være produsert før og etter samme år")
    periode2 = film1.sjekk_periode(1995, 1995)
    print(f"Film 1 er fra perioden 1995-1995: {periode2}")
    # <fyll ut og fjern # på print-setningen>
    print()

    # sjekk_tittel
    # Sjekk om en film har en tittel som starter på en streng som du selv velger
    print ("Sjekker om starten på en films tittel kjennes igjen")
    resultat1 = film1.sjekk_tittel("La")
    print(f"Film 1 har tittel som starter på 'La': {resultat1}")

    resultat2 = film2.sjekk_tittel("Stalk")
    print(f"Film 2 har tittel som starter på 'Stalk': {resultat2}")

    resultat3 = film1.sjekk_tittel("Al")
    print(f"Film 1 har tittel som starter på 'Al': {resultat3}")
    # <fyll ut og fjern # på print-setningen>
    print()

    
    # __str__
    # Skriv ut film-objekt med print
    print("Skriver ut en film med print (test av __str__)")
    print(film1)
    print(film2)
    # <fyll ut og fjern # på print-setningen>
    print()

    
    # test __eq__ (frivillig)
    print ("tester __eq__ med to ulike filmer:")
    print(f"Er 'La Haine' lik 'Stalker'? Svar: {film1 == film2}")

    # <fyll ut og fjern # på print-setningen>
    print("\nTester __eq__ med to like filmer:")
    print(f"Er 'La Haine' lik 'La Haine'? Svar: {film1 == film1}")

    # <fyll ut og fjern # på print-setningen>


test_film()