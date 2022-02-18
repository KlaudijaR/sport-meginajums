def treneris_f(apmekletajs,treneri_v,treneris_apraksts,paroles,treneris_pieejams,zvaigznes):
  atbilde=("jā")
  run=("turpināt")
  while atbilde==("jā"):
    v_parbaud=str(input("Ievadat savu vārdu un uzvārdu: "))
    pin_parbaud=str(input("Ievadi savu paroli: "))
    for i in range(len(treneri_v)):
      if v_parbaud==treneri_v[i] and pin_parbaud==paroles[i]:
        print("Sveiki teneri/e!")
        print("Ko vēlaties darīt?")
        while run==("turpināt"):
          izvele=str(input("Ievadiet jautājumu kārtas ciparu (bez punkta): "))
          if izvele==1:
            apraksts_main = str(input("Rakstat pilnu aprakstu ar jūsu gribētājām pārmaiņām: "))
            treneris_apraksts[i]=apraksts_main
          elif izvele==2:
            pieejams_main=str(input("Ievadiet savus pārmainītos   darba laikus, dienas: "))
            treneris_pieejams[i]=pieejams_main
          elif izvele==3:
            print(zvaigznes[i])
          run=str(input("Vai vēlaties turpinat vai iziet?: "))
          if run==("turpinat"):
            continue
          else:
            break

        atbilde=("nē")
        apraksts_jaut=str(input("Vai, vēlaties pārmainīt savu   aprakstu?:"))
        if apraksts_jaut==("jā"):
          apraksts_main=str(input("Rakstat pilnu aprakstu ar jūsu gribētājām pārmaiņām:"))
          treneris_apraksts[i]=apraksts_main
        pieejams_jaut=str(input("Vai gribat pārmainīt savas darba dienas laikus?: "))
        if pieejams_jaut==("jā"):
          pieejams_main=str(input("Ievadiet savus pārmainītos   darba laikus, dienas: "))
          treneris_pieejams[i]=pieejams_main
        zvaigznes_jaut=str(input("Vai gribat redzēt savu reitingu?: "))
        if zvaigznes_jaut==("jā"):
          print(formulas.reitings_f(reitingu_skaits,reitings)[i])
          break
        elif i==len(paroles)-1:
          print("Nepareizs vārds, vai parole.")
          atbilde=str(input("vai mēģināsiet velreiz?: "))
          if atbilde==("jā"):
            continue