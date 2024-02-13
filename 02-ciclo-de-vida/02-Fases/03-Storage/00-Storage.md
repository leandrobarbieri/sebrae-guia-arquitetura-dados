# Fase: Storage
Os storages de dados desempenham um papel central no ciclo de vida de engenharia de dados. Ele é a fundação da arquitetura de uma plataforma, é nele que os dados serão persistidos, transformados e servidos. Os componentes de processamento, as linguagens de consulta, as ferramentas de virtualização de dados irão interagir com o storage o tempo todo para ler e escrever durante no ciclo de vida.

![Alt text](../../media/fase-storage.png)

<br>

# Tipos de Storages de Dados
Os storages de dados podem ser entendidos quanto aos sistemas de storage em si ou quanto às suas abstrações que facilitam a aplicação prática da tecnologia.

No final do dia os engenheiros de dados não acessam diretamente os sistemas de arquivos do storage, as abstrações e os recursos que auxiliam realizar as operações de leitura e escrita de forma mais eficiente.

Sob sistemas de arquivos distribuídos como HDFS, Object Storages ou bancos relacionais MPP são criados os data lakes, lakehouses e os modern data warehouses com os recursos adionais como controles de acesso, políticas de retenção, catalogação, indexação, etc.

Atualemente datalakes ou um lakehouses se baseam em object storages distribuídos (hdfs, amazon s3, azure blob storage) que utilizam  tecnologias abertas e padrões de serialização, formatos de arquivos (parquet, delta, hudi, iceberg) e tipos de compactação abertos. 

Essa abertura, permite que plataformas diferentes compartilhem dados com segurança sem que haja necessidade de configurações de firewall, vpn, vlan e todas as questões de segurança e infraestrutura entre domínios. Arquiteturas de dados modernas hoje são capazes fazer querys diretamente e datasets externos como se fossem parte do storage sem ter necessidade de copiar os dados graças e essa padronização e abertura.


![Alt text](../../media/sistemas-storages.png)


# Object storages
Hoje os principais storages para dados analíticos são os object storages, entre os mais usados estão o Amazon S3, Azure Blob Storage, Google Cloud Storage. Todos eles tem o benefício de serem baratos e muito flexíveis pois antedem vários tipos de caso de e são capazes de armazenar qualquer tipo de arquivo, e ao mesmo tempo serem integrados com tecnologias de Lakehouse. 

Além disso, funcionam de forma distribuída e escalável, características essas encontradas nas tecnologias de plataformas de dados modernas como spark, e data warehouses modernos baseados em serviço na cloud.

Um object storage funciona como se fosse um sistema de arquivos, que podemos armazenar qualquer tipo de objeto (txt, csv, json, imagens, vídeos, audio). Uma característica específica é a de não ter um árvore de diretório de arquivos centralizada, cada objeto mantém seus próprios metadados e isso faz com que não haja limitação para a quantidade de arquivos que podem ser gerenciados por um object storage. Outra característica importante é que os objetos armazenados são imutáveis, não podem ser modificados, apenas inseridos, substituídos ou removidos. Tudo isso aliado ao fato de serem distribuídos e escaláveis verticalmente e horizontalmente, faz dos object storages uma solução que entraga a capacidade de ler e escrever grandes volumes de dados de forma muito eficiente.

Nas arquiteruras modermas temos a separação entre o processamento e o armazenamento dos dados, nesse contexto os object storages entregam a flexibilidade que as diversas tecnologias para processar os dados precisam. Hoje os object storages vêm provando que são ideais para as cargas de trabalho com volume e varidade. Ou seja, eles são capazes de acomodar a demanda de armazenamento de tecnologias de big data que processam dados em escala de petabytes com um ótima performance de escrita e leitura em processamentos em batch.

Existe uma questão quanto a cargas de trabalho que envolvem atualizações frequentes. Object storages em geral não são bons com operações em arquivos pequenos. Eles trabalham melhor com arquivos grandes e baixas taxas de operações por segundo.

Mas existem formatos e tecnologias que surgiram para lidar com essas questões de atualização em object storages e estão resolvendo bem essas limitações. Veremos com mais detalhes quando entrarmos no assunto formatos em object storages.


## Organização em buckets/containers
Apesar de parecer que os arquivos em um object storage possuem uma estrutura de diretórios, na verdade não existe. Todos os metadados incluisive o caminho completo do arquivo está contido nele mesmo, dessa forma não existe dependências que limitam o volume de arquivos que podem existir, aliado a isso, o fato de terem uma arquitetura distribuída, os object storage são virtualmente ilimitados.

Um fator muito importante para ter um object store funcional é a padronização das camadas (exemplo: bronze/raw, silver/enriched, gold/curated) e a nomenclatura das "pastas' para organizar o data lake e não correr o risco de perder o controle sobre onde os dados estão armazenados.

## Hierarquia Lógica:
Para manter o data lake organizado, crie uma hierarquia lógica de pastas que reflita a estrutura dos dados. Organize as pastas por domínio, projeto, fonte de dados ou qualquer outra categoria relevante. Evite pastas com muitos arquivos soltos.

Veja uma relação de camadas e as sugestões de padrões de nomenclatura:

Camanda | Característica | Exemplo
------- | -------------- | -------
Landing/Transient | Essa camada é usada em processos de ingestão do tipo push, que recebe os dados em formato nativo (qualquer formato) e de imediato são movidos para bronze. Nessa camada as pastas devem ter os nomes das fontes de dados originais. | ./landing/sas;<br> ./landing/leme;<br>./lading/bizagi;
Bronze/Raw | Nessa camada os dados estão com o schema original, mas com um formato padrinizado e organizado por nome das fontes e as datas (ano, mês/ dia) da data de processamento. | ./bronze/sas/ano=2024/mes=jan/dia=20240131
Silver/Trusted | Nessa camada os dados estão padronizados com um formato único por tipo mas ainda são classificados pela fonte | ./silver/sas/delta/ano=2024/mes=jan/dia=20240131; silver/sas/parquet/ano=2024/mes=jan/dia=20240131; 
Gold/Refined | Após limpeza e padronização os dados devem estar organizados para consumo e depedendo do projeto os conjuntos de dados devem ter nomes relacionados às áreas de negócio | ./gold/atendimento/uf=es/ano=2024/mes=jan/dia=20240131

![Alt text](../../media/hierarquia-objectstorage-diagrama.png)



## Tipos de disco para storages
Os dados em um object storage podem ser armazenados em tipos de disco diferentes. Dependendo da frequencia de acesso e do tipo de uso podemos escolher entre tipos "hot" ou "cold" para armazenar os dados de forma eficaz e com maior custo benefício.

o tipo hot storage é usado em camadas do data lake que são acessadas com mais frequencia, ele é baseado em discos SSD, mais eficientes e mais caros. Essa opção possui baixa latência, mais facilidade para escalar e leitura e escrita otimizada. Já o tipo cold é mais barato, é baseado em dicos HDD e é recomdado para manter dados históricos.

Use o tipo hot nas camadas de transformação e entrega e cold para backup ou armazenamento de longo prazo para dados históricos que precisam ser mantidos por alguma questão de compliance

<br>

# Data Sharing
É um recurso que nos permitir incorporar fontes de dados de storages remotos ou internos como parte do lakehouse. Isso traz simplicidade e evita a replicação de dados sem controle dentro da empresa e abre a possibildade de compartilhamento entre unidades independentes ou empresas parceiras.

O fato de não ter mover grandes quantidade de dados e conseguir incorporar nas querys tabelas externas com segurança e performance, faz com que a feature data sharing seja ideal para o modelo federado do Sebrae, onde cada unidade pode atuar de forma independente, com arquiteturas distintas e mesmo assim compartilhar seus produtos de dados como recurso que pode ser gerenciado e governado por um repositório central unificado. Além disso simplifica os pipelines de atualização dos dados pois evita a necessidade de sincronização dos pipelines externos e internos.

<br>

## Formatos de arquivos
Os arquivos de dados podem existir em formatos abertos, conhecidos e tradicionais como csv, json, xml, parquet ou proprietários como .mdf do SQL Server e .dbf o Oracle. Cada formato possui suas característivas vantegens e desevantagens. Alguns são mais estruturados como é o caso do parquet, outros são semi-estrutrados como o csv. Essa diversidade faz seja necessário avaliar cada caso de uso.

### Schema-on-Read e Schema-on-Write
A definição do schema do arquivo, ou seja, a estrutura da tabela e os tipos das colunas pode fazer parte dos metadados do arquivo ou ser parte da query que faz a leitura dos dados. Essa diferenciação faz com que as consultas tenham que inferir os tipos para conseguir analisar os dados. Exemplo: os dados são armazenados sem schema e ao ler um arquivo csv os tipos dos campos precisam ser inferidos ou definidos explicitamente, o que não acontece com arquivos parquet, pois já faz parte da estrutura os metadados com os tipos e ao serem lidos não precisam de explicitar o schema da tabela. Já no processo aquivos schema-on-write, o arquivo ganha a definição de campos e tipos no momento que são salvos no storage.


# Formatos
A escoha dos formatos mais adequados para a sua arquitetura influenciam a forma como o pipeline será desenvolvido e as tecnologias que serão usadas tanto para processamento quanto para consumo dos dados. O mais importante é padronizar o uso de um formato cada caso de uso e camada do Lakehouse. Hoje os mais usados em arquiteturas de Lakehouse são  (Delta Lake, Iceberg, Hudi)

Os formatos Delta, Iceberg e Hudi trazem além do formato otimizado para análise de dados, uma série de features que adicionam as características ACID de bancos de dados tradicionais aos data lakes dessa forma criando os recursos necessário para implantação de um Lakehouse.

O formato parquet desempenha um papel central neste conjunto de formatos para Lakehouses. É com base nele que são criadas as abstrações que entregam as características ACID que existem nos Lakehouses que usam DELTA, HUDI, ICEBERG como formato.



## Comparação de formatos em Lakehouses
Vamos fazer uma comparação dos formatos Delta Lake, Apache Hubi e Iceberg, por serem as principais tecnologias com formatos para arquiteturas baseadas em Lakehouse. Na verdade esses produtos não são apenas formatos, eles adionam as capacidades de um data warehouse aos data lakes.

Obs: buscando unificar e criar interoperabilidade entre estes formatos (princípio de todos estes projetos) foram criados:

- Uniform: https://learn.microsoft.com/pt-br/azure/databricks/delta/uniform
- OneTable: https://www.onetable.dev/

<br>

### Principais funcionalidades

Funcionalidade | DELTA | ICEBERG | HUDI 
-------------- | ----- | ------- | ----
Open source iniciado pelo Databrics https://delta.io/ | Open source iniciado pelo Netflix https://iceberg.apache.org/ | Open source iniciado pelo Uber https://hudi.apache.org/
Suporte a transações ACID | Sim | Sim | Sim
Copy-On-Write: Ao inserir dados cria uma cópia grantindo consistêcia, isolamento e imutabilidade  | Sim | Sim | Sim
Merge-On-Write: As inserções são aplicadas ou mescladas com os dados originais evitando reescrita completa | Não | Não | Sim
Time travel: consultar versões anteriores de um registro |  Sim | Sim | Sim
Primary Keys: chaves primárias nas tabelas gerenciadas | Não | Não | Sim
Estatísticas: analisa estatísticas das tabelas para obter performance | Sim | Sim | Sim
Deduplicação: inserir dados repetidos sem gerar duplicidades | Somente com comando Merge | Somente com comando Merge | Sim, nativo em todo tipo de escrita
Limpeza: versão anteriores dos dados históricos são automaticamente removidos | Operação manual "VACUM" | Operação manual "expireSnapshots" | Automático
Schema Evolution: adapta o schema das tabelas para acomodar as mudanças ao longo do tempo | Sim | Sim | Sim
Validação de qualidade dos dados: permite fazer checagem na qualidade dos dados ? | Sim, NOT NULL, CHECK | Não | Sim
Snapshot: permite salvar uma versão da tabela e restaurar | Sim | Não | Sim

<br>

### Integrações com outros componentes 

Integrações    | DELTA | ICEBERG | HUDI 
-------------- | ----- | ------- | ----
Apache Spark | Sim | Sim | Sim
AWS Redshift | Sim | Não | Sim
Google BigQuery | Não | Sim | Sim 
Google DataProc | Sim | Sim | Sim
Azure Synapse | Sim | Não | Sim
Databricks | Sim | Sim | Sim
Snowflake | Sim | Sim | Não
Presto | Somente leitura | Leitura e Escrita | Somente leitura
DBT | Sim | Não | Sim
Kafka | Sim | Não | Sim
ClickHouse | Sim | Não | Sim



## Iceberg

https://www.thoughtworks.com/en-es/radar/platforms/apache-iceberg

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