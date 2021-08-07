import math
import pandas as pd
if __name__ == '__main__':
    df = [3.2,4.1,4.9 , 5.0 , 7.3 , 6.7 , 6.6 , 7.4 , 7.1 , 4.0 , 5.5 , 5.4 , 6.5 , 6.5 , 7.1 , 5.2 , 8.3 , 5.7 , 6.8,  6.4]
    df.sort()
    #Ordena os elementos
    #print(df)

    n = len(df);
    #print("Valor de n é %s" % n)

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


