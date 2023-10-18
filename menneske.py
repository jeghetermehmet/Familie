class Menneske:
    def __init__(self, navn, alder):
        self._er_forelder = False
        self._barn = []
        self._navn = navn
        self._alder = alder
    def har_fodselsdag(self):
        self._alder += 1
        print("Hurra!", self._navn, "er nå:" + str(self._alder))
    def bytt_navn(self, nyttnavn):
        self._navn = nyttnavn
    def faar_barn(self, navn):
        menneske = Menneske(navn, 0)
        self._barn.append(menneske)
        self._er_forelder = True
        print("Gratulerer", self._navn + "!", "Du får et barn som heter", navn)
    def hent_navn(self):
        return self._navn
    def hent_barn(self):
        return self._barn
    def hent_alder(self):
        return self._alder 
    