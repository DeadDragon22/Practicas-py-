def numerico(cadena):
	try:
		float(cadena)
		return True
	except ValueError:
		return False

print ("Digite la cantidad de colones a convertir")
colon=float(input())

if numerico(colon):

	conversion=colon*0.1143
	print("La conversion de $",colon, "colones a dolares es $","{:.2f}".format(conversion))

else:
	print("La cantidad ingresada no es de tipo numerico")