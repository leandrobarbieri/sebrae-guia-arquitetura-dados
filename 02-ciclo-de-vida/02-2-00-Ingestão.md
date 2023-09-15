#### o que é
> Abordar aqui as relações de dependência, entradas, saídas, limites, responsabilidades, tipos de tecnologias

#### porque
> benefícios de ter um pipeline com ingestão de dados eficiente (isolamento, concorrência, etc..)

#### Como?
> como uma ingestão é feita, tipos de conexões (api, drivers, agentes, etc), oquestração, formatos


# Ingestão

## Diferenças ETL e ELT ou EtLT

## ETL reverso
Processo de usar os dados do DW de volta nas aplicações com dados consolidados e multiplas fontes com uma visão cross-process que ajudam a enriquecer as aplicações com dados complementares.

## batch vs streaming
> diferenças, tipos de tecnologias, quando usar e quando não usar
Unificado

## Estratégias de atualização
Full, Incremental, pull, push
## Com usar cdc para estrategias incrementais


## Formatos e conectividade
padronização de formatos, conectividade, drivers, regras de rede, landing para receber, software agentes , etc..; 
Breve introdução dos formatos csv, parquet, delta tables, quando usar vantagens e desvantagens, qual é mais rapido, qual é menor, códigos de conversão entre formatos; Com ou sem schema – schemaless schemaonread ou write, mudança de schema


## exemplos de códigos de ingestão
> criar uma tabela
https://docs.delta.io/latest/delta-batch.html#write-to-a-table&language-sql

```
SQL APPEND
INSERT INTO default.people10m SELECT * FROM morePeople

SQL OVERWRITE
INSERT OVERWRITE TABLE default.people10m SELECT * FROM morePeople

Python
df.write \
  .format("delta") \
  .mode("overwrite") \
  .option("replaceWhere", "birthDate >= '2017-01-01' AND birthDate <= '2017-01-31'") \
  .save("/tmp/delta/people10m")
```

Você sabe o que é Upsert? Upsert é uma operação de banco de dados que tenta inserir um registro e, caso o registro exista, o registro é atualizado, caso não exista, o registro é inserido como um novo registro.





