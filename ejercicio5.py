A =float(input("ingrese el valor del primer numero:   "))
B = float(input("ingrese el valor del segundo numero:   "))

A = pow(A,2)

if A<B:
	print (" el segundo es mayor que el cuadrado del primero ")
elif A==B:
	print (" el segundo es el cuadrado exacto del primero ")
else:
	print (" el segundo es menor que el cuadrado del primero ")
