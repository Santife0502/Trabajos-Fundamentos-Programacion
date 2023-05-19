import random
import pandas as pd
Equipos=["Aguilas Doradas", "Alianza Petrolera", "America de Cali",
          "Atletico Bucaramanga", "Atletico Junior", "Atletico Nacional",
            "Deportivo Cortulua" ,"Deportes Tolima", "Deportivo Cali" ,
              "Deportivo Pasto" , "Deportivo Pereira" , "Envigado FC" ,
                "Independientes Medellin" , "Independientes Santa Fe",
                  "Jaguares de Cordoba" , "La Equidad", "Millonarios" ,
                    "Once Caldas", "Patriotas FC" , "Union Magdalena"]
partidos = []
for i in range((len(Equipos))):
    for j in range(i+1, len(Equipos)):
        partido = [Equipos[i], Equipos[j]]
        partidos.append(partido)      
resultados = []
for partido in partidos:
    goles_local = random.randint(0, 5)
    goles_visitante = random.randint(0, 3)
    resultado = [partido[0], partido[1], goles_local, goles_visitante]
    resultados.append(resultado)
goles = {}
partidos_ganados = {}
partidos_empatados = {}
partidos_perdidos = {}
Puntos = {}
for equipo in Equipos:
    goles[equipo] = 0
    partidos_ganados[equipo] = 0
    partidos_empatados[equipo] = 0
    partidos_perdidos[equipo] = 0
    Puntos[equipo] = 0
        
for resultado in resultados:
    goles[resultado[0]] += resultado[2]
    goles[resultado[1]] += resultado[3]
if resultado[2] > resultado[3]:
    partidos_ganados[resultado[0]] += 1
    Puntos[resultado[0]] += 3 
    partidos_perdidos[resultado[1]] += 1
elif resultado[2] == resultado[3]:
    partidos_empatados[resultado[0]] += 1
    Puntos[resultado[0]] += 1
    partidos_empatados[resultado[1]] += 1
    Puntos[resultado[1]] += 1
else:
    partidos_ganados[resultado[1]] += 1
    Puntos[resultado[1]] += 3 
    partidos_perdidos[resultado[0]] += 1
print("=========================================== Tabla de Resultados ==========================================")
print("==========================================================================================================")
print("             Equipo             |     Puntos    |     Goles     |    Ganados    |   Empatados   | Perdidos")
print("==========================================================================================================")
for equipo in Equipos:
    print("{:<30} | {:<15} | {:<15} | {:<10} | {:<14} | {:<12}".format(equipo, Puntos[equipo], goles[equipo], partidos_ganados[equipo],
                                                                  partidos_empatados[equipo], partidos_perdidos[equipo]))
print("==========================================================================================================")