# O que é
> Abordar aqui asrelações de dependência, entradas, saídas, limites, responsabilidades, tipos de tecnologias


O que é um storage de dados analíticos, formatos de arquivos, object storages, armazenamento distribuido, etc

# Porque
Benefícios de se usar tecnologias de storage dedicados a análise de dados

# tipos 
> blob, object, etc

# Formatos
> delta, avro
A escoha dos formatos sao importantes para garantir a padronização dos dados analíticos e a interoperabilidade com os componentes da arquitetura (engine, lakehouse, orquestrador, ferramenta de análise, frameworks de ml)

ormats (Delta Lake, Apache Iceberg, Apache Hudi) that are suitable for building a lakehouse.

### comparação
https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison
https://medium.com/@bernardo.costa/comparativo-de-hudi-ice-berg-e-delta-lake-para-plataformas-modernas-de-dados-b0077c82d2df
https://www.databricks.com/blog/delta-uniform-universal-format-lakehouse-interoperability

# particionamento

# tendencias
> o que vêm mudando, o que vem se estabelecedo como padrão

# Comparativo
- gcs vs adls vs minio


# Features

Feature | Tipo 1 | Tipo 2 
-------| -------- | -----------
blob | x | x 
object | - | x 

# virtualização de dados e conceito de serverless
> descrever os benefícios como não precisar mover os dados, principalmente em uma arquitetura mesh baseada em domínios, centralizar o acesso aos dados em um unico ponto (oquestrador não precisa ter acesso a todas as fontes, apenas a maquina que virtualiza) 

# Recomendações

## não armazenar dados semi-estruturados em base relacionalç