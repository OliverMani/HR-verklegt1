

class Help:
    def __init__(self):
        self.help = f"""
P ----- Info:
            Opnar þinn prófíl og sýnir allar helstu upplýsingar um þig

V ----- Notanlegar skipanir: "x" "x" "x" "x"
        Info:
            Sýnir verkbeiðnir fyrir þinn vinnustað og WorkRequestID fyrir hverja verkbeiðni, þar inni getur þú búið til 
            nýja verkbeiðni, leitað eftir ákveðinni verkbeiðni eftir WorkRequestID (Ef þú vilt skoða verkbeiðni númer 3 
            þá ýtir þú á "L" og síðan "3"). Þegar þú ert búin/n að leita þá kemur fyrst upp upplýsingar um verkbeiðnina 
            og fyrir neðan það kemur upp skýrslan sem skráð er á verkbeiðnina ef skýrsla er til fyrir þessa verkbeiðni. 

F ----- Notanlegar skipanir: "L" "R" "A" "C" ""
        Info:
            Sýnir fasteignir fyrir áfangastaðinn sem þú ert skráð/ur á. 


S ----- Info:
            Sýnir starfsmenn sem eru skráðir á þínum vinnustað.


VS ---- Er notanlegt í (F)asteign, (V)erkbeiðnir og (S)tarfsmenn
        Notanlegar skipanir: "" "" "" "" ""
        Info:
            Sýnir verkskýrslur fyrir þinn vinnustað, og ef notað er í (F)asteign, þá getur þú séð allar verkskýrslur
            fyrir ákveðinni fasteign. Með því að vera inni í (F)asteign og síðan skrifa fasteignarID-ið og "VS", þá 
            birtast allar skýrslur varðandi þessa fasteign. Það er einnig hægt að nota "VS" í (S)tarfsmenn. Þar skrifar
            þú starfsmannsID og "VS" fyrir aftan, þá færðu verksýrslurnar sem þessi starfsmaður hefur skráð.

C ----- Býr til nýjan hlut í ákveðinni skrá og það fer eftir því hvað þú valdir síðast. 
        Eins og t.d. Þú ýtir á "S" og síðan "C", þá býrðu til nýjan starfsmann.
        Þessi takki virkar í Starfsmönnum, Fasteignum ef þú ert yfirmaður. 
Q ----- Forritið hættir að keyra


L -----
R -----





"""

    def render(self):
        pass