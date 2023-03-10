import itertools
from collections import Counter
import matplotlib.pyplot as plt
import statistics
import pandas as pd
import numpy as np
if __name__ == '__main__':
    a_0 = [0] * 25
    a_1 = [1] * 20
    a_2 = [2] * 3
    a_3 = [3] * 1
    a_4 = [4] * 1
    a= []
    a.extend(a_0)
    a.extend(a_1)
    a.extend(a_2)
    a.extend(a_3)
    a.extend(a_4)
    recounted = Counter(a)
    print(recounted)

    lst = pd.Series(a)
    print("Sumarização dos dados")
    print(lst.describe())
    n, bins, patches = plt.hist(x=a, bins=5, color='#0504aa',
                                alpha=0.7, rwidth=0.85,)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Valor')
    xticks = [(bins[idx + 1] + value) / 2 for idx, value in enumerate(bins[:-1])]
    plt.xticks(xticks,labels = ["0","1","2","3","4"])
    plt.ylabel('Frequencia')
    plt.title('Histograma')
    plt.show()