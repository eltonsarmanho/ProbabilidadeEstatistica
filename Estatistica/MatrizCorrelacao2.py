#Importando bibliotecas
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('../Dados/iris.csv')
print(df.describe())

df = df[['sepal.length','sepal.width','petal.length']]
corrMatrix = df.corr()
sn.heatmap(corrMatrix, annot=True)
plt.show()