# o que é
> Abordar aqui as relações de dependência, entradas, saídas, limites, responsabilidades, tipos de tecnologias



# porque
> benefícios de ter um pipeline com ingestão de dados eficiente (isolamento, concorrência, etc..)

# Como?
> como uma ingestão é feita, tipos de conexões (api, drivers, agentes, etc), oquestração, formatos


# tipos e estratégias

> Ingestão: Diferenças ETL e ELT ou EtLT, Full, Incremental, padronização de formatos, conectividade, drivers, regras de rede, landing zone, agentes, etc..; Formatos csv, parquet, delta tables, quando usar vantagens e desvantagens, qual é mais rapido, qual é menor, códigos de conversão entre formatos; Com ou sem schema – schemaless schemaonread ou write, mudança de schema

> ETL reverso
Reverse ETL vs CDP

Another somewhat-in-the-weeds, but fun to watch part of the landscape has been the tension between Reverse ETL (again, the process of taking data out of the warehouse and putting it back into SaaS and other applications) and Customer Data Platforms (products that aggregate customer data from multiple sources, run analytics on them like segmentation, and enable actions like marketing campaigns). 


## exemplos
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

# pull push

# batch vs streaming
> diferenças, tipos de tecnologias, quando usar e quando não usar
Unificado


# cdc

# Contratos
> descrever a importância de ter um contrato entre os pipelines e as fontes geradoras (frequência de geração e consumo, escopo, forma, volume esperado) para evitar modificações que quebram os pipelines


# observabilidade
> o que é, exemplos e benfícios. Porque nessa fase

# Object storages vantagens e desvantagens
Features mais importantes, porque usar como storage de dados analíticos
Melores praticas para organizar as pastas em buckets/containers

# Conclusão
> como as saídas cumpreem o objetivo da fase e os princípios do cap. anterior, 


# Links
https://youtube.com/watch?v=kJcd6xVK2lY&feature=share



