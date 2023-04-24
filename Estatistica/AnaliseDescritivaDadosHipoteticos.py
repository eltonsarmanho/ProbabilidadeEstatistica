
import math
import pandas as pd

def loadData():
    data = pd.read_csv("https://raw.githubusercontent.com/"
                       "eltonsarmanho/ProbabilidadeEstatistica/"
                       "master/Dados/dadosHipoteticos.csv")
    print(data.describe())
    print(data.info())

    #https://gist.github.com/aishwarya8615/89d9f36fc014dea62487f7347864d16a
    data = pd.read_csv(
        "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
    )
    print(data.describe())
    print(data.info())
    #https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales
    data_url = "https://raw.githubusercontent.com/plotly/datasets/master/supermarket_Sales.csv"
    data = pd.read_csv(data_url)

    print(data.describe())
    print(data.info())


    data_url = "https://raw.githubusercontent.com/eltonsarmanho/ProbabilidadeEstatistica/master/Dados/projetoIOT_Covid.csv"
    data = pd.read_csv(data_url)

    print(data.describe())
    print(data.info())

    data_url = "https://raw.githubusercontent.com/eltonsarmanho/ProbabilidadeEstatistica/master/Dados/uber.csv"
    data = pd.read_csv(data_url)

    #https://www.kaggle.com/datasets/yasserh/uber-fares-dataset?select=uber.csv
    print(data.describe())
    print(data.info())


if __name__ == '__main__':
   loadData()
