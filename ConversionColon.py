def numerico(cadena):
	try:
		float(cadena)
		return True
	except ValueError:
		return False

print ("Digite la cantidad de dolares a convertir")
dolar=float(input())

if numerico(dolar):

	conversion=dolar*8.75
	print("La conversion de $",dolar, "dolares a colones es C","{:.2f}".format(conversion))

else:
	print("La cantidad ingresada no es de tipo numerico")