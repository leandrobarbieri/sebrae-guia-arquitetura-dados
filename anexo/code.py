import pandas as pd
dados1 = {"estado": ["SP", "RJ", "ES"] * 3, 
          "ano": [2000, 2000, 2000, 2010, 2010, 2010, 2020, 2020, 2020],
          "populacao": [50_000, 30_000, 20_000, 55_000, 33_000, 22_000, 60_000, 40_000, 30_000]}

# transforma um dicionario em um dataframe
df1 = pd.DataFrame(dados1)
df1.head()
