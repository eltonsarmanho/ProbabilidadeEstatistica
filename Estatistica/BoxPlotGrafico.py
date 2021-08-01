import  pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt

if __name__ == '__main__':
    familia1=  [20, 20, 20, 20, 20]
    familia2 = [20, 24, 20, 16, 20]
    familia3 = [12, 28, 24, 20, 16]
    familia4 = [36, 32, 20, 8, 4]
    data = [familia1,familia2,familia3,familia4]

    df = pd.DataFrame(data,columns=['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4','Semana 5'])
    print(df)
    print(df['Semana 1'].describe())

    # Seleciona primeiro quartil
    q1 = df['Semana 1'].quantile(.25)
    # Seleciona Terceiro quartil
    q3 = df['Semana 1'].quantile(.75)
    DIQ = q3-q1;
    outliers = [q1-1.5*DIQ,q3+1.5*DIQ]
    print("Intervalo dos outliers %s " % outliers)

    boxplot = df.boxplot()
    plt.show()