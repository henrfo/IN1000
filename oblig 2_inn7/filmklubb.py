from film import Film

class Filmklubb:
    def __init__(self):
        self._filmer = []

    def les_filmer_fra_fil(self, filnavn: str):
        with open(filnavn, "r", encoding="utf-8") as fil:
            for linje in fil:
                linje = linje.strip()
                if linje:
                    tittel, produksjonsår = linje.split(";")
                    film = Film(tittel, int(produksjonsår))
                    self._filmer.append(film)

    def skriv_ut_alle_filmer(self):
        for film in self._filmer:
            film.skriv_ut_film()
    
    def registrer_film(self):
        tittel = input("Tittel: ")
        produksjonsår = int(input("Produksjonsår: "))
        ny_film = Film(tittel, produksjonsår)
        if ny_film in self._filmer:
            print(f"Filmen {tittel} finnes allerede.")
        else:
            self._filmer.append(ny_film)
            print(f"Filmen {tittel} ble registrert.")

    def finn_film_tittel(self, tittel: str):
        for film in self._filmer:
            if film.sjekk_tittel(tittel):
                return film
        print(f"Fant ingen filmer med tittel som starter med '{tittel}'.")
        return None

    def legg_til_skuespillere(self, film: Film):
        while True:
            navn = input("Navn på skuespiller (trykk enter for å avslutte):")
            if navn == "":
                break
            rolle = input("Rolle: ")
            film.ny_skuespiller(navn, rolle)

    def finn_filmer_periode(self, år1: int, år2: int) -> list:
        filmer_i_periode = []
        for film in self._filmer:
            if film.sjekk_periode(år1, år2):
                filmer_i_periode.append(film)
        return filmer_i_periode