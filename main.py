import pandas as pd
import io
import requests
from bs4 import BeautifulSoup

r = requests.get("https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-leve-2022")
soup = BeautifulSoup(r.content, "html.parser")
#print(soup)

#soup.find_all(class_="resource-item")

for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])



link = "https://opendatasus.saude.gov.br/dataset/notificacoes-de-sindrome-gripal-leve-2022"
f = requests.get(link)
print(f.text)

url="https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SGL/2022/uf=AC/lote=1/part-00000-d5288981-2f4b-47dc-9406-6c9854cfe0d2.c000.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')), sep=';')

print(c)

print(c.dtypes)  