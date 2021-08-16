import scipy.stats as st
import numpy as np


if __name__ == '__main__':

    data = [-0.04, -0.19, 0.14, -0.09, -0.14, 0.19, 0.04 , 0.09]
    mean, sigma = np.mean(data), np.std(data)
    print("Media = %s e Desvio = %s" %(mean,sigma))
    c1,c2 = st.t.interval(alpha=0.90, df=len(data)-1,
                            loc=np.mean(data), scale=st.sem(data))
    print(c1,c2)
