Código | Questão | Recomendação | Princípio
------ | --------- | --------- | ---------
R01-Storage | Como armazenar de forma correta dados em bases de relacionais? | Não armazenar dados semi-estruturados em base relacional e garantir que todas as tabelas com dados analíticos estejam armazenados como column-store | P6
R02-Storage | Como garantir que os dados possam ser acessados por diversos compomentes de processamento e análise de dados? | os dados não devem estar em formato proprietario, exclusivo do produto do storage (devem estar em formato aberto, comum a maioria das ferramentas). 

- usar parquet na bronze por ser mais generalista e delta ou iceberg na silver e gold

- colocar pk e foreign key no começo da tabela

- não armazenar dados semi-estruturados em base relacionalç

- antes de armazenar fazer a compressao do arquivo para reduzir o tamanho e economizar

ex func de compressao para testar o melhor formato 

> def salvando_arquivo_comprimido_json(dataframe):
    compressoes = ["none", "bzip2", "gzip", "lz4", "snappy", "deflate"]
    caminho_padrao = "/FileStore/tables/PNSB_json_"

    for tipo_compressao in compressoes:
        dataframe.write \
            .option("compression", tipo_compressao) \
            .mode("overwrite").format("json") \
            .save(caminho_padrao + tipo_compressao)
        
        display(dbutils.fs.ls(caminho_padrao + tipo_compressao))

salvando_arquivo_comprimido_json(df)
