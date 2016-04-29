def num(x):
	import random
	x=random.rendint(1,100);
	print(str(x)+"\t")

control=1
intentos=5

while (control==1):
	x=int
	pista=int(input("desea una pista? (perdera 1 intento), ""\n"" seleccione su respuesta:"
		"\n""1)si"
		"\n""2)no"))
	if (pista==1):
		if x < 50:
			print "es un numero menor a 50"
		else:
			print "es un numero mayor a 50"
		intentos=intentos-1
	else:
		numingresado=int(input("ingrese un numero mayor a 0 y menor a 101:"))

		if (numingresado < x):
			print "el numero ingresado es menor al numero aleatorio"
			intentos= intentos-1
		elif (numingresado > x):
			print " el numero ingresado es menor al numero aleatorio"
			intentos= intentos-1
		else:
			print "el numero ingresado es correcto, FELICIDADES!"
	control=int(input("desea seguir jugando?" "\n" "seleccione su repuesta:" 
	"\n" "1)si"
	"\n" "2)no"))
else:
	print "gracias por jugar,buena suerte la proxima vez"









