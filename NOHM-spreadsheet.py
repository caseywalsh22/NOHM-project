#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
#import plotly.express as px
import matplotlib.pyplot as plt

mydf = pd.read_excel (r'C:\Users\Greenbaum\Downloads\1H fits Sahana.xlsx')

mydf['Normalize'] = pd.to_numeric(mydf.Normalize[3:19], downcast="float")

df_norm = mydf['Normalize']

df_Gz = mydf['Gz (G/cm)']
df_Gz[3:19]

myplot = plt.plot(df_norm, df_Gz)


# In[ ]:





# In[ ]:




