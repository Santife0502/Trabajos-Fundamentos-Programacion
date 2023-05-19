
	# Programa para calcular la Velocidad Media y la Aceleracion
	# Version 1.0
	# Desarrollado por Santiago Gomez y Mario Andres Palma 
	# Definicion de variables
op= int()
v_inicial = float()
v_final = float()
tiempo = float()
dist = float()
ac = float()
	# Declaracion de variables
v_inicial = 0.0
v_final = 0.0
tiempo = 0.0
	# Entradas
print("Menu de seleccion")
print("1: Velocidad Media")
print("2: Aceleracion")
print("3: Velocidad Final si se tiene el Tiempo")
print("4: Velocidad Final si se tiene la Distancia")
print("5: Distancia si se tiene la Velocidad Final")
print("6: Distancia si no tiene la Velocidad Final")
print("Elija una opcion ")
op = int(input())
	# Procesos y Salidas
if op>6:
		print("Ingreso un numero no valido")
else:
		if op<1:
			print("Ingreso un numero no valido")
		else:
			if op==1:
				print("Digite el valor de la Velocidad Inicial en K/h")
				v_inicial = float(input())
				print("Digite el valor de la Velocidad Final en K/h")
				v_final = float(input())
				vm = v_final+v_inicial/2
				print("Para calcular la Velocidad Media de un objeto se usa la formula Velocidad Final+Velocidad Inicial/2 ")
				print("La Velocidad Media fue de: ",vm," K/h")
			elif op==2:
				print("Digite el valor de la Velocidad Inicial en K/h")
				v_inicial = float(input())
				print("Digite el valor de la Velocidad Final en K/h")
				v_final = float(input())
				print("Digite el valor del Tiempo de Aceleracion en s")
				tiempo = float(input())
				ac = v_final-v_inicial/tiempo
				print("Para calcular la Aceleracion de un objeto se usa la formula Velocidad Final-Velocidad Inicial/Tiempo")
				print("La Aceleracion tuvo un valor de: ",ac," m/s^2")
			elif op==3:
				print("Digite el valor de la Velocidad Inicial en m/s")
				v_inicial = float(input())
				print("Digite el valor de la Aceleracion")
				ac = float(input())
				print("Digite el valor de el Tiempo en s")
				tiempo = float(input())
				v_final = v_inicial+ac*tiempo
				print("Para calcular la Velocidad Final de un objeto se usa la formula Velocidad Inicial+ Aceleracion*Tiempo ")
				print("La velocidad Final fue de: ",v_final)
			elif op==4:
				print("Digite el valor de la Velocidad Inicial en m/s")
				v_inicial = float(input())
				print("Digite el valor de la Aceleracion")
				ac = float(input())
				print("Digite el valor de la Distancia m ")
				dist = float(input())
				v_final = v_inicial*v_inicial+2*ac*dist
				print("Para calcular la Velocidad Final de un objeto se usa la formula Velocidad Inicial^2+2*Aceleracion*Distancia")
				print("La velocidad Final fue de: ",v_final)
			elif op==5:
				print("Digite el valor de la Velocidad Final en m/s")
				v_final = float(input())
				print("Digite el valor de la Velocidad Inicial en m/s")
				v_inicial = float(input())
				print("Digite el valor de el Tiempo en s")
				tiempo = float(input())
				dist = (v_final-v_inicial/2)*tiempo
				print("Para calcular la Distancia de un objeto se usa la formula (Velocidad Final-Velocidad Inicial/2)*Tiempo ")
				print("La Distancia fue de: ",dist,"m/s")
			elif op==6:
				print("Digite el valor de la Velocidad Inicial en m/s")
				v_inicial = float(input())
				print("Digite el valor de la Aceleracion")
				ac = float(input())
				print("Digite el valor de el Tiempo en s")
				tiempo = float(input())
				dist = v_inicial*tiempo+1/2*ac*tiempo*tiempo
				print("Para calcular la Distancia de un objeto se usa la formula Velocidad Inicial*Tiempo+1/2*Aceleracion*Tiempo^2 ")
				print("La Distancia fue de: ",dist)

0
5