## Formatos e conectividade
padronização de formatos, conectividade, drivers, regras de rede, landing para receber, software agentes , etc..; 
Breve introdução dos formatos csv, parquet, delta tables, quando usar vantagens e desvantagens, qual é mais rapido, qual é menor, códigos de conversão entre formatos; Com ou sem schema – schemaless schemaonread ou write, mudança de schema


# Formatos
> delta, avro, iceberg
A escoha dos formatos sao importantes para garantir a padronização dos dados analíticos e a interoperabilidade com os componentes da arquitetura (engine, lakehouse, orquestrador, ferramenta de análise, frameworks de ml)

Escolha de um tipo de arquitetura e formato de arquivo para MDS

Formatos (Delta Lake, Iceberg, Hudi) that are suitable for building a lakehouse.

> tabelas em iceberg com mais de 1TB

Predominante Delta e Iceberg (Dremio - open lakehouse)
Delta, Iceberg são compativeis e comparáveis?

- ACID - transações, correncia no object storage - garantia
- Multitransação grandes pontos de um beneficio de um lakehouse


## schema on read e schema on write

## mostrar um estudo comparando a performance (leitura e escrita) e espaço de armanzenamento de diferentes formatos

## destacar o funcionamento do parquet como padrão para dados analiticos


## Iceberg

https://www.thoughtworks.com/en-es/radar/platforms/apache-iceberg

Apache Iceberg falls in the same category as Delta Lake and Apache Hudi.
- Formato de arquivo para implantação de lakehouse
- Mais possibilidade de customizações/otimizações do que delta (tabelas gigantes acima de 10 TB)
- Criado pensando em abstrações que permitem outras engines podem se conectar, camada extra de abstrações  
- Expressões com SQL (SELECT, INSERT, UPDATE, MERGE tudo que um banco relacional tem)
- Evolução de Schema (adaptação a mudamças de schema e não falha o pipeline) 
- Hidden Partitioning (não precisa dizer o que precisa particionar) entende o que fazer auto
- Timetravel e rollback
- Lakehouses são imutaveis, novas versões dos dados
- dois tipos de arquivos (delete files/puffin files) qualquer tipo de arquivo não apenas parquet - parquet, orc, avro (melhor em streaming) - tabelas grandes para query (ORC), default (parquet)- atende casos de uso específicos no mesmo lakehouse format - escolhe o tipo par cada tabela "file format agnostic"


## Delta Lake
Tecno qye funciona bem em com delta
![Alt text](image-7.png)
- Sugestão de criar particionamento quando a tabela estiver acima de 1TB
- Criado pensam na integração com o spark, 
- Cada formato tem um conjunto de tecnologias que se casam ou preferenciais: Kafka, StarRocks (DW Open Source), Apache Doris (DW Open Source), Apache Impala 
- Não precisa ter um DW ou um lakehouse pode usar um engine de query moderno como trino e consultar o dado direto no data lake Pinot + Trino + Delta/Iceberg
- Expressões com SQL (SELECT, INSERT, UPDATE, MERGE tudo que um banco relacional tem)
- Trabalha apenas com parquet

- Hidden Partitioning (não precisa dizer o que precisa particionar)
muita dirsidade de linguafes e
O spark consegue conversar bem com todos os formatos, mais é mais alinhado com o Delta (mesma fabricante) 

> recomendações
Quanto mais arquivos mais lento a leitura - arquivos no tamanho certo (pequenos demais - muito list ou grandes demais - acessando mesmo o local sempre paralelismo) - cada arquivo tem que ser aberto listadop o 
que demora. O custo maior está no list, abertura leitura e fechamento
- pra resolver compartação de arquivos
- atividades de  manutenção arquovos oordenados



### comparação
https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison
https://medium.com/@bernardo.costa/comparativo-de-hudi-ice-berg-e-delta-lake-para-plataformas-modernas-de-dados-b0077c82d2df
https://www.databricks.com/blog/delta-uniform-universal-format-lakehouse-interoperability

# particionamento em storage distribuido


# Comparativo
- gcs vs adls vs minio

# tendencias
> o que vêm mudando, o que vem se estabelecedo como padrão

