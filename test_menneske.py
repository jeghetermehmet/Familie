from menneske import Menneske
def hovedprogram():
    Ole = Menneske("Ole", 23)
    print(Ole.hent_navn(), Ole.hent_alder(), "år")
    
    Ole.bytt_navn("Håland")
    Ole.har_fodselsdag()
    Ole.faar_barn("Kari")

    print("Barna til", Ole.hent_navn() + ":")
    allebarn = Ole.hent_barn()
    for barn in allebarn :
        print(barn.hent_navn())



hovedprogram()