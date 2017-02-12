
# coding: utf-8

# # Table of Contents
#  <p>

# In[19]:

from funciones_tesouro import *
df, fecha = coger_todo()
print("Los datos fueron actualizados en: " + fecha)


# In[20]:

df


# In[8]:

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('PruebaPython-8a97b6c1f08a.json', scope)

gc = gspread.authorize(credentials)


# In[17]:

sh1 = gc.open('Tesouro')
worksheet = sh1.get_worksheet(0)


# In[26]:

cell_list = worksheet.range('A1:A26')
i = 0
for cell in cell_list:
    cell.value = df.iloc[i, 0]
    i += 1
cell_list2 = worksheet.range('B1:B26')


# In[27]:

i = 0
for cell in cell_list2:
    cell.value = df.iloc[i, 1]
    i += 1


# In[29]:

worksheet.update_cells(cell_list)
worksheet.update_cells(cell_list2)


# In[39]:

worksheet.update_cell(1, 3, "Los datos fueron actualizados en: " +  fecha)


# In[35]:

fecha


# In[ ]:



