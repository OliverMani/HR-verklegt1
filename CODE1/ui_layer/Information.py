class InformationScreen:
    def __init__(self):
        self.info = """
Help screen:

P - Info:
        Opnar þinn prófíl og sýnir allar helstu upplýsingar um þig

V - Notanlegar skipanir: "L" "R" "x" "x"
    "L" = Leitar eftir skýrsluID og sýnir skýrsluna og spyr hvort þú viljir bæta við skýrslu
    "R" = Raðar upp verkbeiðnum eftir áfangastað
    "" = 
    "" =
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
    "C" = Býr til nýja fasteign í kerfinu
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
            Býr til nýjan hlut í ákveðinni skrá og það fer eftir því hvað þú valdir síðast. Eins 
            og t.d. Þú ýtir á "S" og síðan "C", þá býrðu til nýjan starfsmann. Þessi takki virkar í 
            Starfsmönnum, Fasteignum ef þú ert yfirmaður. Í (V)erkbeiðnir er hægt að búa til nýja 
            verkbeiðni fyrir fasteign.

#CVS - Er best notað í (V)erkbeiðnir (ID+CVS), en virkar hvar sem er í kerfinu
#        Info:
#            Býr til nýja verkskýrslu, þú skrifar ID á verkbeiðninni sem þú ert að búa til

Q - Forritið hættir að keyra

L - Er notanlegt í (S)tarfsmenn, (V)erkbeiðnir, (F)asteign og "VS"
        Info:
            Þú notar þessa skipun til að leita í kerfinu eftir einhverju sérstöku og það fer eftir á 
            hvaða skjá þú varst síðast á. Ef þú varst síðast á (S)tarfsmenn og skrifar "C", þá býrðu
            til nýjan starfsmann.

R - Er notanlegt í (S)tarfsmenn, (V)erkbeiðnir, (F)asteign
        Info:
            Þú notar þessa skipun til að raða hlutum eftir áfangastað, eins og í (S)tarfsmenn, þar er 
            hægt að raða starfsmönnum eftir áfangastað og í (F)asteign er hægt að raða öllum fasteignum
            sem eru á ákveðnum áfangastað.

A - Er notanlegt í (V)erkbeiðnir, (F)asteign og (S)tarfsmenn
        Info:
            Þessi skipun sýnir lista yfir öllu sem hægt er að sjá varðandi ákveðin hlut. Að nota þessa
            skipun í (F)asteign skilar öllum fasteignum sem fyrirtækið hefur á skrá.
"""

    def render(self):
        ''' prentar út Hjálparskjáinn '''
        print(self.info)