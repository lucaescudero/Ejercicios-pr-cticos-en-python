print ("Sistema vacasional \n")

nom = input ("Ingrese su nombre por favor: ")
clave = int (input ("Ingrese su clave de area: "))
antiguedad = float (input("Indique sus años trabajados: "))

if clave == 1:
    if antiguedad > 0 and antiguedad <= 1:
        print (nom, ", te corresponden 6 dias de vacasiones")
    elif antiguedad >= 2 and antiguedad <= 6:
        print (nom, ", te corresponden 14 dias de vacasiones")
    elif antiguedad >= 7:
        print (nom, ", te corresponden 20 dias de vacasiones")
    else:
        print (nom, ", no te corresponden dias de vacasiones")
elif clave == 2:
    if antiguedad > 0 and antiguedad <= 1:
        print (nom, ", te corresponden 7 dias de vacasiones")
    elif antiguedad >= 2 and antiguedad <= 6:
        print (nom, ", te corresponden 15 dias de vacasiones")
    elif antiguedad >= 7:
        print (nom, ", te corresponden 22 dias de vacasiones")
    else:
        print (nom, ", no te corresponden dias de vacasiones")

elif clave == 3:
    if antiguedad > 0 and antiguedad <= 1:
        print (nom, ", te corresponden 10 dias de vacasiones")
    elif antiguedad >= 2 and antiguedad <= 6:
        print (nom, ", te corresponden 20 dias de vacasiones")
    elif antiguedad >= 7:
        print (nom, ", te corresponden 30 dias de vacasiones")
    else:
        print (nom, ", no te corresponden dias de vacasiones")

else:
    print ("La clave ingresada no es valida.")