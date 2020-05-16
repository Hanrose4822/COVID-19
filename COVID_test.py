#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import glob


# In[89]:


pliki = glob.glob(r'D:\csse_covid_19_daily_reports\*.csv')


# In[90]:


tab = pd.DataFrame(columns=['Last_Update', 'Confirmed', 'Deaths', 'Recovered'])


# In[91]:


for plik in pliki:
    dane = pd.read_csv(plik)
    
    try:
        rows = dane[dane['Country_Region'] == 'Poland'][['Last_Update', 'Confirmed', 'Deaths', 'Recovered']]
    except:
        rows = dane[dane['Country/Region'] == 'Poland'][['Last Update', 'Confirmed', 'Deaths', 'Recovered']]
        rows.columns = ['Last_Update', 'Confirmed', 'Deaths', 'Recovered']
    
    tab = pd.concat([tab, rows], ignore_index=True)
    


# In[92]:


tab[['Confirmed', 'Deaths', 'Recovered']] = tab[['Confirmed', 'Deaths', 'Recovered']].astype(int)
tab['Last_Update'] = pd.to_datetime(tab['Last_Update'])


# In[93]:


tab.sort_values('Last_Update', inplace=True)


# In[95]:


tab.to_csv('D:\COVID-19\Wykres.csv', index=False, date_format='%Y-%m-%d')

