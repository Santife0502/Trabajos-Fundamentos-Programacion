#Parcial 2 Fundamentos
Equipos= ["Aguilas Doradas", "Alianza Petrolera", "America de Cali", "Atletico Bucaramanga", "Atletico Junior", "Atletico Nacional", "Deportivo Cortulua" ,"Deportes Tolima", "Deportivo Cali" , "Deportivo Pasto" , "Deportivo Pereira" , "Envigado FC" , "Independientes Medellin" , "Independientes Santa Fe", "Jaguares de Cordoba" , "La Equidad", "Millonarios" , "Once Caldas", "Patriotas FC" , "Union Magdalena"]
print("Los Equipos son: ", Equipos)
#Listas de los Equipos que jugaran de locales y de visitantes
ListaLocal1=["Aguilas Doradas, Alianza Petrolera, America de Cali, Atletico Bucaramanga, Atletico Junior, Atletico Nacional, Deportivo Cortulua,Deportes Tolima, Deportivo Cali,Deportivo Pasto"]
ListaVisit1=["Deportivo Pereira, Envigado FC, Independientes Medellin, Independientes Santa Fe, Jaguares de Cordoba, La Equidad, Millonarios, Once Caldas, Patriotas FC, Union Magdalena"]
ListaLocal2=["Deportivo Pereira, Envigado FC, Independientes Medellin, Independientes Santa Fe, Jaguares de Cordoba, La Equidad, Millonarios, Once Caldas, Patriotas FC, Union Magdalena"]
ListaVisit2=["Aguilas Doradas, Alianza Petrolera, America de Cali, Atletico Bucaramanga , Atletico Junior, Atletico Nacional, Deportivo Cortulua, Deportes Tolima, Deportivo Cali,Deportivo Pasto"]
print("")
print("Los primeros Equipos que jugaran de Locales son: ", ListaLocal1)
print("")
print("Los primeros Equipos que jugaran de Visitantes son: ", ListaVisit1)
print("")
print("Los siguientes equipos que jugaran de locales son: ", ListaLocal2)
print("")
print("Los siguientes Equipos que jugaran de Visitantes son: ", ListaVisit2)
print("")
# Punto 1 
canPar=(20*2)-2
print("La cantidad de partidos que juega cada equipo", canPar )
print("")
# Punto 2, 3, 4 

      
import random
import pandas as pd

Equipos = ["Aguilas Doradas", "Alianza Petrolera", "America de Cali", "Atletico Bucaramanga", "Atletico Junior", "Atletico Nacional", "Deportivo Cortulua" ,"Deportes Tolima", "Deportivo Cali" , "Deportivo Pasto" , "Deportivo Pereira" , "Envigado FC" , "Independientes Medellin" , "Independientes Santa Fe", "Jaguares de Cordoba" , "La Equidad", "Millonarios" , "Once Caldas", "Patriotas FC" , "Union Magdalena"]

partidos = []
for i in range(len(Equipos)):
    for j in range(i+1, len(Equipos)):
        partido = [Equipos[i], Equipos[j]]
        partidos.append(partido)

resultados = []
for partido in partidos:
    goles_local = random.randint(0, 5)
    goles_visitante = random.randint(0, 3)
    resultado = [partido[0], partido[1], goles_local, goles_visitante]
    resultados.append(resultado)

posiciones = {"Equipos":Equipos, "resultados":resultados}
tabla=pd.DataFrame(posiciones)
print(tabla)




    


    

  
    



