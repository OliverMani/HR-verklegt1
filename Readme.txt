----------------------------------------[ Hópur 42 ]----------------------------------------
Hönnun: 
    inni í þessari möppu eru frumgerðirnar af fyrstu pródótýpunni.
    Hver skrá heitir eftir skjánum sem hún sýnir.

csv_files:
    Eins og nafnið gefur lit kynna þá eru allar csv skrárnar geymdar í þessari möppu.
    þetta eru skrárnar sem geyma allar upplýsingar um gögn sem forritið birtir.
    Destinations.csv -> upplýsingar um áfangastaði.
    Employees.csv -> upplýsingar um starfsmenn.
    Properties.csv -> upplýsingar um fasteignir.
    WorkReports.csv -> upplýsingar um verkskýrslur.
    WorrkRequests.csv -> upplýsingar um verkbeiðnir.

CODE1:
    Þessi mappa geymir allann kóðann. 
    Storagelayer:
        Hérna eru skrárnar sem lesa úr csv skránum geymdar.
        Hver skrá fylgir csv skrá og heita sama nafni auk SL til að greina í 
        sundur að þær tilheyri Storagelayer.
        Allar skrárnar virka eins það er fall sem les inn csv skránna línu fyrir línu
        til að geta notað listann á öðrum stöðum í forritinu. Svo er fall sem breytir
        upplýsingum í csv skránni og annað sem uppfærir skránna (með nýju upplýsingunum)
        Svo er líka lítið fall sem sér til þess að það er alltaf auð lína í csv skránni 
        þetta kemur í veg fyrir að það komi villa þegar við viljum svo bæta við nýrri línu
        í skránna.
        Síðast en alls ekki síst er svo SLAPI skráin sem tengir öl föllin í storage layer við 
        LogicLayer skrárnar.

    Model:
        Það er sér model skrá fyrir hverja csv skrá. 
        Þeir halda utan um þær upplýsingar sem eru skráðar í línurnar í csv.
        hver breyta í init fallinu eru dálkarnir í csv skránni. 
        Þessar skrár og föll eru svo notur í Storagelayer og áfram. 
        Má segja að þetta sé eins og notkurskonar eyðublað til að lesa og skrifa
        inn í csv skránna.

    LogicLayer:
        Þessar skrár taka við upplýsingum frá Storagelayer. Möppurnar í LogicLayer eru 
        allar merktar með LL tila að greina í sundur frá öðrum skjölum. 
        Hérna fer fram öll flokkunin, röðunin og hugsunin ef svo má segja. Enn og aftur
        eru skránum skipt eftir csv heitunum að viðbættri login skrá. 
        Í þessum föllum er öll virknin hvað má og hvað ekki, flokkunin á hvaða upplýsingar
        eiga að skila sér o.fl.
        Eing og í Storagelayer þá er einnig sér mappa í LogicLayer, LLAPI sem sér um að 
        geyma öll föllin í LogicLayer möppunum svo að hægt sé að kalla í þau í næsta layeri
        eða ui_layer.

    ui_layer:
        Hérna er sér skrá fyrir þá skjái sem byrtast í forritinu. Hver skrá sér um að birta
        réttar upplýsingar eftir því hvað slegit er inn.
        Aðal skjárinn er main menu skjalið, hann sér um að birta valmyndina (línan sem er efst á 
        hverjum skjá) og taka við hvaða aðgerð á að  ( Slá in aðgerð: )
        Tekið er við því sem var slegið inn og réttur skjár birtur í samræmi við það.
        Það er mismunandi hvað byrtist á hverjum skjá og hvað hægt er að gera eftir því hvaða
        stöðu notandinn hefur.
        Í klösunum og föllunum í skránun í þessari möppu er svo kallað í klasana sem eru tengdir
        í LLAPI skránni.
        


    




