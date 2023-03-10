
import math
import pandas as pd

def loadData():
    data = pd.read_csv("https://raw.githubusercontent.com/eltonsarmanho/ProbabilidadeEstatistica/master/Dados/dadosHipoteticos.csv")
    print(data.describe())
    print(data.info())

    df = pd.read_csv(
        "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
    )
    print(df.info())

    data_url = "https://raw.githubusercontent.com/plotly/datasets/master/supermarket_Sales.csv"
    sales = pd.read_csv(data_url)

    print(sales.info())


if __name__ == '__main__':
   loadData()
