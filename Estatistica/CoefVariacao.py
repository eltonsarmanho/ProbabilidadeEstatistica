import numpy as np
import pandas as pd
#Cria vetor Simples
data = [88, 85, 82, 97, 67, 77, 74,
        86, 81, 95, 77, 88, 85, 76, 81, 82]
#Define a função CV
cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
#Calcula CV
print("Cv : %s" % cv(data))


#Lendo a partir de um dataset
#data = pd.read_csv("https://raw.githubusercontent.com/eltonsarmanho/ProbabilidadeEstatistica/master/Dados/iris.csv")
data = pd.read_csv("../Dados/iris.csv")

#Calcular considerando todos os elementos do dataset
data_colunasNumericas = data.drop(['variety'],axis=1)#Remove Coluna Categorica
print("Calcular considerando todos os elementos do dataset")
print(data_colunasNumericas.apply(cv))

#Calcular considerando as classes ou variedades de plantas
print("Calcular considerando as classes ou variedades de plantas")

print(data.groupby(['variety'])['petal.width'].std() / data.groupby(['variety'])['petal.width'].mean())


