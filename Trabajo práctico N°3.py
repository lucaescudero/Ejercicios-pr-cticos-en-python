print ("\n Programa para determinar que número es mas grande de los tres\n")

num_1 = float (input(" Ingrese el primer número: "))
num_2 = float (input(" Ingrese el segundo número: "))
num_3 = float (input(" Ingrese el tercer número: "))


if num_1 > num_2 and num_1 > num_3:
    print ("El numero mas grande es: ", round (num_1))
elif num_2 > num_1 and num_2 > num_3:
    print ("El numero mas grande es: ",round (num_2))
elif num_3 > num_1 and num_3 > num_2:
    print ("El numero mas grande es: ",round (num_3))
