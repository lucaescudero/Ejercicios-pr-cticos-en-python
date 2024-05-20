print("Calculadora con una sola variable \n")

print("********************")
print("* Menú de opciones *")
print("********************")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto \n")

numero = int(input("Introduce la opción deseada:"))

if numero == 1:
    print ("elegiste suma \n")
    numero = int  ( input ("indique el primer número: "))
    numero += int (input("indique el segundo número: "))
    print ("El resultado de la suma es:", numero)
elif numero == 2:
    print ("elegiste resta \n")
    numero = int  ( input ("indique el primer número: "))
    numero -= int (input("indique el segundo número: "))
    print ("El resultado de la resta es:", numero)
elif numero == 3:
    print ("elegiste multiplicación \n")
    numero = int  ( input ("indique el primer número: "))
    numero *= int (input("indique el segundo número: "))
    print ("El resultado de la multiplicación es:", numero)
elif numero == 4:
    print ("elegiste división \n")
    numero = int  ( input ("indique el primer número: "))
    numero /= int (input("indique el segundo número: "))
    print ("El resultado de la división es:", numero)
elif numero == 5:
    print ("elegiste división entera \n")
    numero = int  ( input ("indique el primer número: "))
    numero //= int (input("indique el segundo número: "))
    print ("El resultado de la división entera es:", numero)
elif numero == 6:
    print ("elegiste exponente \n")
    numero = int  ( input ("indique el primer número: "))
    numero **= int (input("indique el segundo número: "))
    print ("El resultado del exponente es:", numero)
elif numero == 7:
    print ("elegiste modulo o resto \n")
    numero = int  ( input ("indique el primer número: "))
    numero %= int (input("indique el segundo número: "))
    print ("El resultado del modulo es:", numero)
else:
    print ("Opción no disponible")