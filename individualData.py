import pandas as pd

bd = pd.read_csv("./players_20.csv")

columns = bd.columns.values
print(columns)

print("\n")

futbolColombiano = bd[bd["nationality"]=="Colombia"]
#print(futbolColombiano)

print("Datos estadísticos sobre los jugadores colombianos (2020):")
print("\n")

#Promedio de altura:
print("Promedio de altura de los jugadores colombianos:")
promedioAltura = futbolColombiano[["height_cm"]].describe()
print(round(promedioAltura,2))
print("\n")

#jugadores colombiano mas altos:
print("Jugadores más altos:")
masAltos = futbolColombiano[futbolColombiano["height_cm"]>194]
print(masAltos[["short_name","height_cm","club"]])


#jugadores más bajos:
print("\n")
print("Jugadores más bajos:")
masAltos = futbolColombiano[futbolColombiano["height_cm"]<164]
print(masAltos[["short_name","height_cm","club"]])

print("\n")
print("Promedio de peso de los jugadores colombianos:")
promediopeso = futbolColombiano[["weight_kg"]].describe()
print(round(promediopeso,2))
print("\n")

#Jugadores más pesados:
print("Jugadores más pesados:")
masPesados = futbolColombiano[futbolColombiano["weight_kg"]>90]
print(masPesados[["short_name","weight_kg","club"]])

#Jugadores con menor peso:
print("\n")
print("Jugadores con menor peso:")
masPesados = futbolColombiano[futbolColombiano["weight_kg"]<60]
print(masPesados[["short_name","weight_kg","club"]])

print("\n")

#Jugadores con más overall
print("Jugadores con mayor overall:")
masOverall = futbolColombiano[futbolColombiano["overall"]>80]
print(masOverall[["short_name","overall","club"]])

#Jugadores más jovnes y veeteranos:
print("\n")
print("\n")
print("Jugadores más jóvenes:")
masJovenes = futbolColombiano[futbolColombiano["age"]<18]
print(masJovenes[["short_name","age","club"]])

print("\n")
print("\n")
print("Jugadores más veteranos:")
masVeteranos = futbolColombiano[futbolColombiano["age"]>35]
print(masVeteranos[["short_name","age","club"]])

#Mejores arqueros
arquerosColombianos = futbolColombiano[futbolColombiano["player_positions"]== "GK"]

#Tiros al arco
print("\n")
print("Mejores atajadores:")
mejoresAtajadores = arquerosColombianos[arquerosColombianos["goalkeeping_diving"]>70]
print(mejoresAtajadores[["short_name","goalkeeping_diving","club"]])


print("\n")
print("Arqueros que mejor manejan el balón con los pies:")
mejoresConLosPies = arquerosColombianos[arquerosColombianos["goalkeeping_kicking"]>70]
print(mejoresConLosPies[["short_name","goalkeeping_kicking","club"]])


print("\n")
print("Arqueros con los mejores reflejos:")
mejoresreflejos = arquerosColombianos[arquerosColombianos["goalkeeping_reflexes"]>70]
print(mejoresreflejos[["short_name","goalkeeping_reflexes","club"]])



#Mejores con la cabeza:
#attacking_heading_accuracy
print("\n")
print("Jugadores con mayor precisión en el remate de cabeza:")
mayorPrecision = futbolColombiano[futbolColombiano["attacking_heading_accuracy"]>75]
print(mayorPrecision[["short_name","attacking_heading_accuracy","club","player_positions"]])

#Mejores Finalizadores
#attacking_finishing
print("\n")
print("Mejores finalizadores:")
mejorFinalizacion = futbolColombiano[futbolColombiano["attacking_finishing"]>75]
print(mejorFinalizacion[["short_name","attacking_finishing","club","player_positions"]])



#Mejor dribbling
#skill_dribbling
print("\n")
print("Jugadores con mejor regate:")
mejorDribbling = futbolColombiano[futbolColombiano["skill_dribbling"]>80]
print(mejorDribbling[["short_name","skill_dribbling","club","player_positions"]])

#Mejor pegada
#shooting
print("\n")
print("Jugadores con mejor pegada:")
mejorPegada = futbolColombiano[futbolColombiano["shooting"]>75]
print(mejorPegada[["short_name","shooting","club","player_positions"]])


#international_reputation
#Reputación internacional
print("\n")
print("Jugadores con mayor reputación internacional:")
reputacionInt = futbolColombiano[futbolColombiano["international_reputation"]>2]
print(reputacionInt[["short_name","international_reputation","club","player_positions"]])