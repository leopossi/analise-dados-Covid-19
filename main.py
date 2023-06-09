import pandas as pd
import io
import requests

url="https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SGL/2022/uf=AC/lote=1/part-00000-2c6b95ee-a526-44ae-b48f-a3975bbae6fb.c000.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')), sep=';')

print(c)

print(c.dtypes)

print(s.decode('utf-8'))

#eu vai apadar tudo - Tatá#