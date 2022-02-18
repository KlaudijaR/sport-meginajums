import formulas
def apmekletajs_f(reitingu_skaits,reitings,zvaigznes,apmekletajs,paroles,treneris_apraksts,treneri_v,bildes,darbalaiki,telpas,aprikojums,abonetaji,abonementi,abonesanas_skaits,treneris_pieejams):
  jaut=("jā")
  velme=str(input("vai gribi trenēties viens, vai ar treneri?: "))
  if velme=="treneri" or velme=="ar treneri":
    bridinajums=str(input("(lai pieteiktos pie trenera tev jabūt abonētājam)Vai Jūs esi abonētajs?:"))
    if bridinajums==("jā"):
      while jaut==("jā"):
        telefons=str(input("ierakstiet savu personas kodu un telefona numuru:"))
        print(abonementi)
        abonements_pieteikt=(int(input("ievadiet abonementa kārtas ciparu ,skatoties no kreisāspuses (ar cipariem): ")))
        for i in range(len(abonetaji)):
          if abonetaji[i]==(f"tel. num., personas kods:{telefons} abonements:{abonementi[abonements_pieteikt-1]}"):
            print("sveiki, ievadītie dati pareizi!")
            darbiba=(int(input("Ko jūs vēlaties darīt?: 1.apskatīt treneru apraksus, 2.novērtēt treneri(rakstat ar cipariem")))
            if darbiba==(1):
             for i in range (len(paroles)):
               print(f"treneris/e: {treneri_v[i]} apraksts:   {treneris_apraksts[i]} pieejams: {treneris_pieejams[i]} reitings:{zvaigznes[i]}")
            if darbiba==(2):
              karta=int(input(f"kuru pēckārtas skatoties no kreisās malas sarakstā {treneri_v} treneri jūs gribat novērtēt (rakstat ar skaitļiem bez punkta) "))
              reitings[karta-1]+=int(input("ievadi zvaigžņu skaitu 1-5 veselos skaitļos?: "))
              reitingu_skaits[karta-1]+=1
            break
            jaut==("nē")
          if i==len(abonetaji)-1:
            print("Ievadīti nepareizi dati.")
            jaut=str(input("vai mēģināsiet velreiz?: "))
  else:
    telpas_izveles=str(input("vai gribi redzēt piedāvātās zāles un to darba laikus?: "))
    if telpas_izveles==("jā"):
      for i in range(len(telpas)):
        print(f"{telpas[i]} atvērta:{darbalaiki[i]}")
    bildes_izvele=str(input("vai gribat redzēt telpu bildes?: "))
    if bildes_izvele==("jā"):
      for i in range (len(bildes)):
        print(f"telpa:{telpas[i]} bildes links:{bildes[i]}")
    aprikojums_izvele=str(input("vai gribat redzēt aprīkojumu?: "))
    if aprikojums_izvele==("jā"):
      for i in range (len(aprikojums_izvele)):
        print(f"telpas:{telpas[i]} aprikojums: {aprikojums[i]}")
    abonements_jaut=str(input("vai gribat pieteikties uz treniņu?: "))
    if abonements_jaut==("jā"):
      print(abonementi)
      telefons=str(input("ierakstiet savu personas kodu un telefona numuru:"))
      abonements_pieteikt=(int(input("ievadiet abonementa kārtas ciparu ,skatoties no kreisāspuses (ar cipariem): ")))
      abonesanas_skaits[abonements_pieteikt-1]+=1
      abonetaji.append(f"tel. num., personas kods:{telefons} abonements:{abonementi[abonements_pieteikt-1]}")
    abonements_atcelt=str(input("vai gribat atcelt abonementu?: "))
    if abonements_atcelt==("jā"):
      telefons=str(input("ierakstiet savu personas kodu un telefona numuru:"))
      print(abonementi)
      abonements_pieteikt=(int(input("ievadiet abonementa kārtas ciparu ,skatoties no kreisāspuses (ar cipariem): ")))
      for i in range(len(abonetaji)):
        if abonetaji[i]==(f"tel. num., personas kods:{telefons} abonements:{abonementi[abonements_pieteikt-1]}"):
          abonesanas_skaits[abonements_pieteikt]-=1
          abonetaji.remove(f"tel. num., personas kods:{telefons} abonements:{abonementi[abonements_pieteikt-1]}")