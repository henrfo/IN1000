class Film:
    def __init__(self, tittel: str, år: int):
        self._tittel = tittel
        self._år = år
        self._skuespillere = {}

    def hent_tittel(self) -> str:
        return self._tittel
    
    def ny_skuespiller(self, navn: str, rolle: str):
        if navn in self._skuespillere:
            print(f"Skuespiller {navn} finnes allerede i filmen {self._tittel}.")
        else:
            self._skuespillere[navn] = rolle
            print(f"Skuespiller {navn} med rolle {rolle} lagt til i filmen {self._tittel}.")

    def hent_skuespiller_navn(self) -> list[str]:
        return list(self._skuespillere.keys())
    
    def skriv_ut_film(self):
        print(f"Tittel: {self._tittel}")
        print(f"År: {self._år}")
        print(f"Skuespillere:")
        for navn, rolle in self._skuespillere.items():
            print(f" {navn} som {rolle}")

    def sjekk_periode(self, år1: int, år2: int) -> bool:
        return år1 < self._år < år2
    
    def sjekk_tittel(self, tittel_start: str) -> bool:
        if tittel_start == "":
            return True
        if len(tittel_start) > len(self._tittel):
            return False
        return self._tittel.startswith(tittel_start)
    
    def __str__(self) -> str:
        info = f"Tittel: {self._tittel}\nÅr: {self._år}\nSkuespillere:"
        for navn, rolle in self._skuespillere.items():
            info += f"\n {navn} som {rolle}"
        return info
    
    def __eq__(self, andre) -> bool:
        if not isinstance(andre, Film):
            return False
        return self._tittel == andre._tittel and self._år == andre._år