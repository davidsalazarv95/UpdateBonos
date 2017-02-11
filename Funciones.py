
# coding: utf-8

# In[2]:

def quitar(x):
    y = x[2:len(x)]
    w = y.replace('.', '')
    return float(w.replace(',', '.'))


# In[3]:

def scrap_bonds():
    import csv
    from urllib.request import urlopen 
    from bs4 import BeautifulSoup
    html = urlopen("http://www.tesouro.fazenda.gov.br/web/stn/tesouro-direto-precos-e-taxas-dos-titulos") 
    bsObj = BeautifulSoup(html, "lxml")
    table = bsObj.findAll("table",{"class":"tabelaPrecoseTaxas sanfonado"})
    bond = []
    price = []
    i = 0
    for row in table[0].findAll("tr"):
        g = 0
        for col in row.find_all('td'):
            if g == 0:
                bond.append(col.string.strip())
            elif g == 3:
                price.append(col.string.strip())
            g += 1    
    bond.pop(0)
    bond.pop(11)
    bond.pop(20)
    bond.pop(23)
    import pandas as pd
    columns = {'Bond': bond, 'Price': price}
    df = pd.DataFrame(columns)
    df['Price'] = df['Price'].map(quitar)
    return df


# In[4]:

def update_date():
    from urllib.request import urlopen 
    from bs4 import BeautifulSoup
    html = urlopen("http://www.tesouro.fazenda.gov.br/web/stn/tesouro-direto-precos-e-taxas-dos-titulos") 
    bsObj = BeautifulSoup(html, "lxml")
    update = bsObj.findAll("div",{"class":"portlet-body"})[13]
    fecha = update.findAll("b")[-1].contents
    return fecha[0]


# In[5]:

def coger_todo():
    df = scrap_bonds()
    fecha = update_date()
    return df, fecha

