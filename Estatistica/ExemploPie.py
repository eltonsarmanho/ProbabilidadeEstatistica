# library
import matplotlib.pyplot as plt
import pandas as pd
# create data: an array of values

data = pd.read_csv("../Dados/inep_saeb_merge_fatorial_2017.csv",delimiter='\t')
data[data['ID_UF']==15];
data.groupby('IN_BIBLIOTECA').size().\
    plot(kind='pie', autopct='%.2f')
# Create a pieplot
#plt.pie(df)
plt.show()