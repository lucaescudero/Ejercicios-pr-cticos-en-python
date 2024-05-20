'''Utilizar un maximo de 7 lineas de codigo.
mostrar desde el numero 0 hasta el 1597'''

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
# {0 1} {1 2} {3 5} {8 13} {21 34} {55 89} {144 233} {377 610} {987 1597}
#Ejemplo 1

#BASICO
x = 0 
x2 = 1
while x < 1597:
    print (x,x2, end=" ")
    x += x2
    x2 += x
print ("Fin")

#ALTERNATIVA (forma esperada con menos lineas de codigo):

num_1, num_2 = 0, 1
while num_2 <= 1957:
    print(num_1, num_2, end=" ")
    num_1 = num_1 + num_2
    num_2 = num_1 + num_2