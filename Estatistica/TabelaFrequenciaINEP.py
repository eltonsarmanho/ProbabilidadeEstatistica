import math

import numpy as np
import pandas as pd
if __name__ == '__main__':

    data = pd.read_csv("../Dados/inep_saeb_merge_fatorial_2017.csv",
                       delimiter='\t')

    aux = data[['ID_MUNICIPIO', 'MEDIA_5EF_LP', 'MEDIA_5EF_MT']]
    print(aux.describe())
    filter = data['ID_MUNICIPIO'] == 1502103;
    df_pa = data[filter];
    df = df_pa['MEDIA_5EF_LP'].dropna(axis=0)


    print(df)
    df = np.sort(df)

    #Ordena os elementos
    #print(df)
    n = len(df);
    print("Valor de n é %s" % n)

    # Amplitude dos dados = Valor maior dos registros - menor valor
    indice_maior = n - 1
    indice_menor = 0
    at = df[indice_maior] - df[indice_menor]
    if (n > 25):
        k = math.sqrt(n)
    else:
        k = 1 + 3.22 * math.log(n)

    # O valor de amplitude de classe pode ser arredondado para um número inteiro, geralmente para facilitar a interpretação da tabela.
    h = at / k
    h = math.ceil(h)
    frequencias = []

    # Menor valor da série
    menor = round(df[indice_menor], 1)

    # Menor valor somado a amplitude
    menor_amp = round(menor + h, 1)
    valor = menor
    while valor < df[indice_maior]:
        frequencias.append('{} - {}'.format(round(valor, 1), round(valor + h, 1)))
        valor += h


    # Discretização dos valores em k faixas, rotuladas pela lista criada anteriormente
    freq_abs = pd.qcut(df, len(frequencias), labels=frequencias)
    print(freq_abs)
    print(pd.value_counts(freq_abs,sort=False,normalize=True))
    #print(pd.value_counts(freq_abs, sort=False))


