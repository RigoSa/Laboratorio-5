dias =["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
nombre = []
kms = []
# Leo el número de conductores. Número de datos que voy a guardar en las listas
while True:
	num_conductores = int(input("¿Cuántos conductores tiene la empresa?:"))
	if num_conductores>0: break

# Recorro las listas hasta el número de conductores indicados
for indice_cond in range(0,num_conductores):
	nombre.append(input("Nombre del conductor %d:" % (indice_cond + 1)))
	#Leo los km realizados para cada día
	km_dias = []
	for indice_dias in range(0,7):
		km_dias.append(int(input("¿Cuántos km ha realizado el %s?:" % dias[indice_dias])))
	kms.append(km_dias)
# Recorro las listas para calcular el total de kilómetros
total_kms = []
for km in kms:
	total_kms.append(sum(km))
# Recorro las listas para mostrar la información de salida
for nombre, km in zip(nombre, total_kms):
	print("%s  ha realizado %d kms." % (nombre,km))
