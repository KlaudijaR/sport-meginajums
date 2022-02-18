def menedzeris_f(reitingu_skaits,reitings,zvaigznes,apmekletajs,paroles,treneris_apraksts,treneri_v,bildes,darbalaiki,telpas,aprikojums,abonetaji,abonementi,abonesanas_skaits):
  jautājumi=("nē")
  if aprakstu_parb==("jā"):
    for i in range (len(treneri_v)):
      print(f"vārds:{treneri_v[i]} apraksts:{treneris_apraksts[i]}")
    zvaigznes_parb=str(input("vai gribat redzēt treneru reitingus?:"))
    if zvaigznes_parb==("jā"):
      for i in range (len(treneri_v)):
        print(f"vārds:{treneri_v[i]} reitings:{zvaigznes[i]}")
    bildes_main=str(input("vai gribat mainīt bildes?: "))
    if bildes_main==("jā"):
      for i in range (len(bildes)):
        bildes[i]=str(input(f"iekopējiet bildes linu {telpas[i]} telpai: "))
    aprikojums_main=str(input("vai gribat mainīt aprīkojuma sarakstu?: "))
    if aprikojums_main==("jā"):
      for i in range (len(aprikojums)):
        aprikojums[i]=str(input(f"ierakstat pilnu aprīkojuma uzskaitījumu {telpas[i]} telpai: "))
    darbalaiki_main=str(input("Gribat mainīt darbalaiku?: "))
    if darbalaiki_main==("jā"):
      for i in range (len(darbalaiki)):
        darbalaiki[i]=str(input(f"ievadiet {telpas[i]} laikus: "))
    treneris_jaut=str(input("vai gribat pievienot jaunu treneri?: "))
    if treneris_jaut==("jā"):
      treneri_v.append(str(input("ievadiet trenera vārdu uzvārdu: ")))
      paroles.append(str(input("ievadi trenera paroli: ")))
    abonetaji_skaits_jaut=str(input(" katra abonementa veida skaitu?"))
    if abonetaji_skaits_jaut==("jā"):
      for i in range (len(abonementi)):
        print(f"{abonementi[i]} cilvēki pieteikušies: {abonesanas_skaits[i]}")
    abonetaji_jaut=str(input(" Vai gribat redzēt abonējošos cilvēkus?"))
    if abonetaji_jaut==("jā"):
      print(abonetaji)