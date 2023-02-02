import pandas as pd
#import matplotlib.pyplot as plt
fd = pd.read_csv("./players_20.csv")

columns = fd.columns.values
print(columns)

print("\n")

head = fd[["short_name", "club", "age", "nationality", "potential", "player_positions"]].head(3)
print(head)
print("\n")

#Análisis de equipos del fútbol colombiano

print("\n")
print("Atlético Nacional:")
atlNacional = fd[fd["club"] == "Atlético Nacional"]
print(atlNacional[["short_name", "age", "overall", "potential", "nationality", "player_positions"]])

print("\n")
print("Tabla de overall & potential de los jugadores de Atl. Nacional:")
mean_ov_pot_ANplayers = atlNacional[["overall", "potential"]].describe()
print(round(mean_ov_pot_ANplayers,2))

print("\n")
print("Tabla de edad, talla y peso:")
means_atlN = atlNacional[["age","height_cm","weight_kg"]].describe()
print(round(means_atlN,2))

print("\n")
print("Lista de salarios de menor a mayor en euros:")
wageList = atlNacional.sort_values("wage_eur")
print(wageList[["short_name", "age", "wage_eur"]])

print("\n")
print("Anális general de salarios y valor del jugador en euros:")
wageAnalysis = atlNacional[["wage_eur","value_eur"]].describe()
print(round(wageAnalysis,2))

print("\n")
print("\n")


#Datos globales del equipo
print("Datos globales en ataque del equipo:")
global_atl = atlNacional[["attacking_finishing","attacking_crossing"]].describe()
print(round(global_atl,2))

print("\n")
print("Datos globales defensivos del equipo:")

atl_def = atlNacional[["defending_marking","defending",]].describe()
print(round(atl_def,2))

print("\n")

#jugadores internacionales:
print("Jugadores internacionales en el equipo:")
internacinalesAN = atlNacional[atlNacional["nationality"]!="Colombia"]
print(internacinalesAN[["short_name","nationality", "player_positions"]])

print("\n")
print("\n")
print("\n")

#Deportivo Independiente Medellín:
print("Deportivo Independiente Medellín:")

dim = fd[fd["club"] == "Independiente Medellín"]
print(dim[["short_name", "age", "overall", "potential", "nationality", "player_positions"]])


print("\n")
print("Tabla de overall & potential de los jugadores del DIM:")
ov_pot_dim = dim[["overall", "potential"]].describe()
print(round(ov_pot_dim,2))

print("\n")
print("Tabla de edad, talla y peso:")
means_dim = dim[["age","height_cm","weight_kg"]].describe()
print(round(means_dim,2))

print("\n")
print("Lista de salarios de menor a mayor en euros:")
wage_dim_list = dim.sort_values("wage_eur")
print(wage_dim_list[["short_name", "age", "wage_eur"]])

print("\n")
print("Anális general de salarios y valor del jugador en euros::")
wageAnalysis_dim = dim[["wage_eur", "value_eur"]].describe()
print(round(wageAnalysis_dim,2))

print("\n")
print("\n")

#Datos globales del equipo
print("Datos globales en ataque del equipo:")
global_dim = dim[["attacking_finishing","attacking_crossing"]].describe()
print(round(global_dim,2))

print("\n")
print("Datos globales defensivos del equipo:")

dim_def = dim[["defending_marking","defending"]].describe()
print(round(dim_def,2))

print("\n")

#jugadores internacionales:
print("Jugadores internacionales en el equipo:")
internacinalesDIM = dim[dim["nationality"]!="Colombia"]
print(internacinalesDIM[["short_name","nationality", "player_positions"]])







