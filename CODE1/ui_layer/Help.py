

class Help:
    def __init__(self):
        self.help = f"""
P - Info:
        Opnar þinn prófíl og sýnir allar helstu upplýsingar um þig

V - Notanlegar skipanir: "x" "x" "x" "x"
        
        Info:
            Sýnir verkbeiðnir fyrir þinn vinnustað og WorkRequestID fyrir hverja verkbeiðni, þar 
            inni getur þú búið til nýja verkbeiðni, leitað eftir ákveðinni verkbeiðni eftir 
            WorkRequestID (Ef þú vilt skoða verkbeiðni númer 3 þá ýtir þú á "L" og síðan "3"). 
            Þegar þú ert búin/n að leita þá kemur fyrst upp upplýsingar um verkbeiðnina og fyrir 
            neðan það kemur upp skýrslan sem skráð er á verkbeiðnina ef skýrsla er til fyrir 
            þessa verkbeiðni. 

F - Notanlegar skipanir: "L" "R" "A" "C" "CVS" "númer/ID"
    "L" = Getur leitað eftir fasteignID og fengið upplýsingar varðandi fasteignina
    "R" = Getur raðað fasteignum upp eftir áfangastað
    "A" = Þú sérð allar fasteignir sem fyrirtækið hefur á skrá
    "C" = Búa til nýja fasteign í kerfinu
    "CVS" = Býr til nýja verkskýrslu fyrir fasteign
    "númer/ID" = Sýnir fasteignina með þetta ID og getur þar bætt við verkbeiðni fyrir fasteignina

        Info:
            Sýnir fasteignir fyrir áfangastaðinn sem þú ert skráð/ur á. 


S - Notanlegar skipanir: "L" "R" "A" "C" "númer/ID" 
    "L" = Leitar með nafni eða ID og sýnir upplýsingar um starfsmanninn
    "R" = Sýnir starfsmenn sem skráðir eru á áfangastað
    "A" = Sýnir alla starfsmenn NaNair
    "C" = Býr til nýjan starfsmann með þínu inputti
    "númer/ID" = Sýnir starfsmann með ID-ið sem þú vildir finna

        Info:
            Sýnir starfsmenn sem eru skráðir á þínum vinnustað.


VS - Er notanlegt í (F)asteign, (V)erkbeiðnir og (S)tarfsmenn
     Notanlegar skipanir: "x" "x" "x" "x" "x"

        Info:
            Sýnir verkskýrslur fyrir þinn vinnustað, og ef notað er í (F)asteign, þá getur þú séð 
            allar verkskýrslur fyrir ákveðinni fasteign. Með því að vera inni í (F)asteign og síðan 
            skrifa fasteignarID-ið og "VS", þá birtast allar skýrslur varðandi þessa fasteign. Það 
            er einnig hægt að nota "VS" í (S)tarfsmenn. Þar skrifar þú starfsmannsID og "VS" fyrir 
            aftan, þá færðu verksýrslurnar sem þessi starfsmaður hefur skráð.


C - Er Notanlegt í (S)tarfsmenn, (V)erkbeiðnir og (F)asteign

        Info:
            Býr til nýjan hlut í ákveðinni skrá og það fer eftir því hvað þú valdir síðast. 
            Eins og t.d. Þú ýtir á "S" og síðan "C", þá býrðu til nýjan starfsmann.
            Þessi takki virkar í Starfsmönnum, Fasteignum ef þú ert yfirmaður. 


Q - Forritið hættir að keyra


L - Er notanlegt í (S)tarfsmenn, (V)erkbeiðnir, (F)asteign og "VS"

        Info:
            Þú notar þessa skipun til að leita í kerfinu eftir einhverju sérstöku og það fer eftir á 
            hvaða skjá þú varst síðast á. Ef þú varst síðast á (S)tarfsmenn og skrifar "C", þá býrðu
            til nýjan starfsmann.


R -





"""

    def render(self):
        pass