import pandas as pd
import  numpy as np

def toAdjacencyList(dataFrame):
    adjacencyList_from = set(dataFrame.to_numpy().transpose().tolist()[0])
    adjacencyList_from.update(dataFrame.to_numpy().transpose().tolist()[1])
    adjacencyList = dict()
    print(dataFrame)
    for i in adjacencyList_from:
        adjacencyList[i] = {"seguidos": [], "pageRank" : 0}
    for index, row in dataFrame.iterrows():
        adjacencyList[row["From"]]["seguidos"].append(row["To"])
    return adjacencyList

def aleatoriedad(adjacencyList,inicio):
    return adjacencyList[inicio]["seguidos"][np.random.randint(0,len(adjacencyList[inicio]["seguidos"]))]


dataFrame = pd.read_csv("Twitter_network_R.csv")
adjacencyList = toAdjacencyList(dataFrame)
inicio = list(adjacencyList)[np.random.randint(0, len(adjacencyList))]
rg = int(input("Ingrese el rango en el que quiere hacer esta opecion: ")) 
for i in range(0,rg):
    adjacencyList[inicio]["pageRank"] += 1 
    if (adjacencyList[inicio]["seguidos"] != []): 
        inicio = aleatoriedad(adjacencyList, inicio)
    else: 
        inicio = adjacencyList[list(adjacencyList)[np.random.randint(0, len(adjacencyList))]]
#pense en hacer yo una funcion quicksort para ahorrar memoria pero mejor voy a arreglar mi diccionario bonito para nada más llamar a la funcion jijiji, perdon Rodri atte: Isra
diccBonito = dict()
for key in adjacencyList:
    diccBonito[key] = adjacencyList[key]["pageRank"]
diccBonito = dict(sorted(diccBonito.items(), key =lambda item: item[1]))
for i in range(1,10):
    print(list(diccBonito)[-i])
#iniciso f
#1
#Matemáticas es que identifica con mucha facilidad estados de alta recurrencia, computacionales es su baja complejidad computacional
#y aplicaciones al mundo real, puede ayudarnos a encontar cosas de alta demanda en casi cualquier contexto
#2
# alguien podría solo seguirse a si mismo para que cuando el algoritmo llegue a el, entre en un loop
#3
# para contrarrestar el primer punto, añadiría una restricción en donde si un usuario solo se sigue a si mismo, volvemos a reelegir aleatoriamente
#4
#añadiendo pesos no uniformes en cada una de las aristas
