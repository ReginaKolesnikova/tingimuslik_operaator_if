
#Ülesanne 1
nimi=input("Mis on sinu nimi?")
if nimi.isalpha() and nimi.isupper():
    if nimi=="JUKU":
        print("Lähme kinno")
        try:
            vanus=int(input(f"Kui vana sa oled {nimi}?"))
            if vanus<0:
                print("Viga!")
            elif vanus<=6:
                print("Tasuta")
            elif vanus<15:
                print("Lastepilet")
            elif vanus<65:
                print("Täispilet")
            elif vanus<100:
                print("Sooduspilet")
            else:
                print("Nii palju!!!")
        except:
            print("Täisarv oli vaja sisestada")
    else:
        print("Ootan Juku")
else:
    print("Segatud sõne")


#Ülesanne 2 (variant 1)
nimi1=input("1. Mis on sinu nimi? ")
nimi2=input("2. Mis on sinu nimi? ")
nimed=["Kirill","Gleb"]
if nimi1.isalpha() and nimi2.isalpha():
    if (nimi1 in nimed) and (nimi2 in nimed):
        print("Nad on pinginaabrid")
    else:
        print("Nad ei ole naabrid")
else:
    print("Viga")


#Ülesanne 2 (variant 2)
if (nimi1=="Kirill" and nimi2=="Gleb") or (nimi2=="Kirill" and nimi1=="Gleb"):
   print("Nad on pinginaabrid")
else:
   print("Nad ei ole naabrid")


#Ülesanne 3
try:
    a=float(input("Toa pikkus: "))
    b=float(input("Toa laius: "))
    S=a*b
    print(f"Põranda pindala on {S} m**2")
    vastus=input("Kas tahad remondi teha? (Jah-1/Ei-0") #Jah/ei JAH,jah
    if vastus.upper()=="JAH" or vastus=="1":
        print("Remont")
        hind=float(input("Ühe meetri hind: "))
        summa=hind*S
        print(f"Remondi kulud: {summa} eur")
    elif vastus.upper()=="EI" or vastus=="0":
        print("-")
    else:
        print("Ei saa aru")
except:
    print("Numbrid!!!")



#Ülesanne 4
hind=float(input("Kui palju see maksab?"))
if hind>700:
     print("Soodus 30%")
     soodus=(hind*30)/100
     print(f"Hind soodustusega on {soodus}")
else:
     print("Viga! Hind on vähem 700 eur!")



#Ülesanne 5
temperatuur=float(input("Kui palju kraadi õues?"))
if temperatuur<18 or temperatuur==18:
     print("Temperatuur vähem kui soovitav toasoojus talvel")
else:
     print("Temperatuur üle 18 kraadi")



#Ülesanne 6
pikkus=float(input("Kui pikk sa oled (cm)"))
try:
   if pikkus<100:
       print("Viga! Nii vähe!")
   elif pikkus<150:
        print("Ta on lühike")
   elif pikkus<180:
        print("Ta on keskmine")
   elif pikkus<210:
        print("Ta on pikk")
   else:
        print("Viga! Nii palju!")
except:
    print("Numbrid!!!")


#Ülesanne 7
sugu=str(input("Naine või mees?(N-naine, M-mees)"))
if sugu=="N" or sugu=="M":
 try:
    if sugu=="N":
       pikkus=float(input("Kui pikk sa oled (cm)"))
       if pikkus<150:
          print("Viga! Nii vähe!")
       elif pikkus<160:
          print("Ta on lühike")
       elif pikkus<170:
          print("Ta on keskmine")
       elif pikkus<190:
          print("Ta on pikk")
       else:
          print("Viga! Nii palju!")
    elif sugu=="M":
       pikkus=float(input("Kui pikk sa oled (cm)"))
       if pikkus<160:
          print("Viga! Nii vähe!")
       elif pikkus<170:
          print("Ta on lühike")
       elif pikkus<180:
          print("Ta on keskmine")
       elif pikkus<210:
          print("Ta on pikk")
       else:
          print("Viga! Nii palju!")
 except:
    print("Viga!")
else:
    print("Viga! Vale andmed!")
