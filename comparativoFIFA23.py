import pandas as pd

bd = pd.read_csv("./fifa23_.csv")

columns = bd.columns.values
print(columns)



print("\n")
print("\n")
'''

'''


print("\n")
print("Manchester United:")
manUntd = bd[bd["Club Name"] == "Manchester United"]
print(manUntd[["Known As","Overall","Potential","Age","Height(in cm)","Weight(in kg)","Club Name","Value(in Euro)","Wage(in Euro)"]])

print("\n")
print("Jugadores con overall superior a 85:")
bestMUntdOv = manUntd[manUntd["Overall"]>85]
print(bestMUntdOv[["Known As","Overall"]])



print("\n")
print("Jugadores con potential superior a 85:")
bestMUntdPot = manUntd[manUntd["Potential"]>85]
print(bestMUntdPot[["Known As","Potential"]])


print("\n")
print("Promedio de salarios y valor en euros en el equipo:")
wageMU = manUntd[["Wage(in Euro)","Value(in Euro)"]].describe()
print(round(wageMU,1))

print("\n")
print("Promedio de peso, estatura y edad:")
manMeanH_W = manUntd[["Weight(in kg)","Height(in cm)","Age"]].describe()
print(round(manMeanH_W,2))

print("\n")
print("Jugadores más jóvenes:")
manYoungest = manUntd[manUntd["Age"]<20]
print(manYoungest[["Known As","Age"]])

print("\n")
print("Jugadores más veteranos:")
manOldest = manUntd[manUntd["Age"]>33]
print(manOldest[["Known As","Age"]])

print("\n")
print("Jugadores más altos:")
manTallest = manUntd[manUntd["Height(in cm)"]>190]
print(manTallest[["Known As","Height(in cm)"]])

print("\n")
print("Jugadores más bajos:")
manLowest = manUntd[manUntd["Height(in cm)"]<170]
print(manLowest[["Known As","Height(in cm)"]])

print("\n")
print("Jugadores más pesados:")
manHeaviest = manUntd[manUntd["Weight(in kg)"]>90]
print(manHeaviest[["Known As","Weight(in kg)"]])

print("\n")
print("Jugadores más livianos:")
manLightest = manUntd[manUntd["Weight(in kg)"]<65]
print(manLightest[["Known As","Weight(in kg)"]])



print("\n")
print("Mejor jugador del equipo (Cristiano Ronaldo):")
cr7 = bd[bd["Known As"] == "Cristiano Ronaldo"]
print(cr7[["Known As","Overall","Potential","Age","Height(in cm)","Weight(in kg)","Club Name","Value(in Euro)","Wage(in Euro)"]])


print("\n")
print("Algunas estadísticas de Cristiano Ronaldo:")
statCR7 = cr7[["Freekick Accuracy","Heading Accuracy","BallControl","Freekick Accuracy","Penalties"]]
print(round(statCR7,1))


print("\n")
print("\n")
'''

'''

print("\n")
print("Paris Saint Germain:")
psg = bd[bd["Club Name"] == "Paris Saint-Germain"]
print(psg[["Known As","Overall","Potential","Age","Height(in cm)","Weight(in kg)","Club Name","Value(in Euro)","Wage(in Euro)"]])

print("\n")
print("Jugadores con overall superior a 85:")
bestPSGOv = psg[psg["Overall"]>85]
print(bestPSGOv[["Known As","Overall"]])



print("\n")
print("Jugadores con potential superior a 85:")
bestPSGPot = psg[psg["Potential"]>85]
print(bestPSGPot[["Known As","Potential"]])


print("\n")
print("Promedio de salarios y valor en euros en el equipo:")
wagePSG = psg[["Wage(in Euro)","Value(in Euro)"]].describe()
print(round(wagePSG,1))

print("\n")
print("Promedio de peso, estatura y edad:")
psgMeanH_W = psg[["Weight(in kg)","Height(in cm)","Age"]].describe()
print(round(psgMeanH_W,2))

print("\n")
print("Jugadores más jóvenes:")
psgYoungest = psg[psg["Age"]<20]
print(psgYoungest[["Known As","Age"]])

print("\n")
print("Jugadores más veteranos:")
psgOldest = psg[psg["Age"]>33]
print(psgOldest[["Known As","Age"]])

print("\n")
print("Jugadores más altos:")
psgTallest = psg[psg["Height(in cm)"]>190]
print(psgTallest[["Known As","Height(in cm)"]])

print("\n")
print("Jugadores más bajos:")
psgLowest = psg[psg["Height(in cm)"]<170]
print(psgLowest[["Known As","Height(in cm)"]])

print("\n")
print("Jugadores más pesados:")
psgHeaviest = psg[psg["Weight(in kg)"]>90]
print(psgHeaviest[["Known As","Weight(in kg)"]])

print("\n")
print("Jugadores más livianos:")
psgLightest = psg[psg["Weight(in kg)"]<65]
print(psgLightest[["Known As","Weight(in kg)"]])



print("\n")
print("Mejor jugador del equipo (Lionel Messi):")
messi = bd[bd["Known As"] == "L. Messi"]
print(messi[["Known As","Overall","Potential","Age","Height(in cm)","Weight(in kg)","Club Name","Value(in Euro)","Wage(in Euro)"]])


print("\n")
print("Algunas estadísticas de Messi:")
statMessi = messi[["Freekick Accuracy","Heading Accuracy","BallControl","Freekick Accuracy","Penalties"]]
print(round(statMessi,1))


# Freekick Accuracy Heading Accuracy  BallControl   Freekick Accuracy