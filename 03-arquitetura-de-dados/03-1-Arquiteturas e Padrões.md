# Arquitetura de dados e padrões
Existem tipos de abstrações de arquiteturas que trazem conceitos antigos, novos ou repaginados que utilizam os componentes tecnolócicos disponíveis para entregar valor através da tranformação, armazenamento e entrega de dados para a empresa. Porém, mais importante do que seguir o padrão que está mais em evidência no momento, é considerar sempre o propósito, os tipos de casos de uso dos dados (analise de dados, machine learning, etl reverso, querys ad-hoc), a forma que serão mantidos e atualizados (cargas full, cargas incrementais, ingestão de streaming), o custo que será gerado entre outros fatores. Escolhas de arquiteturas mais simples, com menos camadas no data lake, com processos de ingestão em batch, com uso de engines de querys "serverless" (query como serviço, não precisa de instanciar um cluster para consultar dados) podem fazer mais sentido inicialmente. Ou se as cargas de trabalho e casos de uso são muito diversificados, talvez faça mais sentido buscar opções mais flexíveis com Lakehouses. 

## Data Lakes
Uma das arquiteturas mais populares nos ultimos anos da area de engenharia de dados, ganhou destaque por trazer a liberdade de trabalhar com dados semi-estruturado e permitir armazenamento em escala a qualquer tipo de objeto de dados ao mesmo tempo ser de fácil integração com engines de processamento diversas. Porém, apesar do hipe, essa tecnologia apresentou vários desafios de governança, controle de transações, catálogos de metadados para descoberta. Mas o maior problema foi que essa arquitetura foi concebida para ser somente leitura e enfrenta dificuldade de atender requisitos de leis como LGPD que obriga a empresa a deletar dados de um usário específico.

## Data Lakehouses (papper)
Essa é uma arquitetura que traz aspectos dos data warehouses como operações em dados estruturados com controle de transações, isolamento, consistência, atualizações em nível de linha e os benefícios e flexibilidade de um data lake para trabalhar com dados semi-estruturados e não estruturados, muito comum em projetos de ciência de dados.

Os problemas experimentados pelos data lakes foram abordados pela empresa Databricks que criou o conceito e a solução Lakehouse. O Lakehouse aplica uma camada de abstração, através de tecnologias como Delta Lake, Hudi, Iceberg, quem adicionam aos dados armazenados em object storages muitas das funcionalidades presentes em bancos relacionais transações atômicas, consistencia, isolamento e durabilidade (ACID). O padrão Lakehouse traz a possibilidade de usar object storages (opão de armazenamento mais barata) para persistir os dados com o formato "parquet" com suporte a atualizações incrementais e rollbacks, como se fosse uma tabela em um banco relacional. Ele consegue isso através do versionamento dos arquivos e geração de metadados. Toda essa complexidade para fazer fica abstraída para o engenheiro de dados. Essa padrão busca a convergencia entre Data Warehouses e Data Lakes. 

De fato é a arquitetura que se tornou predominante nas stacks de plataformas de dados modernas e os data warehouse modernos e os Lakehouse terão diferenças cada vez menores e convergentes nas plataformas Databricks, Azure, Google, Snowflake

A perpectiva de avançar na realização de análises preditivas através da modelagem estatística faz com que os Lakehouses ganhem ainda mais importância pois trazem a possibilidade de trabalhar com dados não-estruturados em conjunto com dados tabulares. Além disso os formatos de armazenamento abertos facilitam muito a integração com os principais frameworks de machine learning.

## Data warehouses modernos (MDW)
Os MDW são projetados para fazer a centralização, organização e padronização de grandes volumas de dados de uma empresa. Até pouco tempo atrás eram baseados em bancos de dados relacionais, com dados armazenados em blocos de linhas. Mas com o surgimentos das soluções em clouds que utilizam formatos abertos, armazenamento de dados colunas e processamento distribuído MPP (massive parellel processing) os data warehouses são bem diferentes.

Os MDW em nuvem representam uma evolução significativa das alternativas on-premise pois trazem uma arquitetura distribuida que permite adaptar a infraestrutura de acordo com a demanda (escalabilidade), provisionando ou desabilitando nós dos clusters. Atualmente suportam processamento em escala de petabytes, armazenam dados semi-estruturados e se integram com tecnologias de processamento como Spark. 

Uma limitação que existe em um MDW é que ele não consegue apoiar efetivamente cargas de trabalho que envolvam dados **não estruturados** como imagens, vídeos, audios. O que em muitos casos é fonte de dados para treinamento de modelos de machine learning. Neste contexto os Lakehouses são uma opção mais adequada.

Em DW tradicionais essa infra de dados teria que ser previamente dimensionada para atender a demanda atual e futura. Exemplos de soluções que se destacam atualmente estão Azure Synapse Dedicated pool, BigQuery, Snowflake, Amazon Redshift. Além dessa flexibilidade os MDW trazem na prática a ideia de separação da camada de processamento da estrurura de armazenamento, que em geral está sustentada por object storages.

Essa separação entre as camadas de armazenamento e processamento está fazendo com que seja cada vez mais tênue os parâmetros que diferenciam os data warehouses modernos dos lakehouses. Hoje ambos estão convergindo para uso de formatos abertos e processamento distribuido apoiados em object storages. Esses padrões poderão em algum momento se fundir em algo único.



### Arquiteturas MPP

<!-- Descrever como essa arquitetura entrega processamento distribuído

![Alt text](image-4.png)

Possio um nó principal e compute notes
Divide entre os compute note
Temos que fazer a forma de distribuição correta para aproveitar os benefícios do paralelismo

Tipos de distribuição entre os nós

Round-robin: distribuição aleatória entre as partições, definida por tabela. Para carga costuma ser mais o método mais rápido. Método de distribuição recomendado para carga de tabelas stage

Hash-distributed: passa uma coluna que será usada para realizar a distribuição de forma determinística atribuindo cada linha a uma distribuição. Recomendado para querys em tabelas fato. Alta performance na leitura
É importante escolher uma coluna de forma certa para a distribuição não ficar desbalanceada. As colunas usadas precisam conseguir identificar de forma bem granular (identificação única)

Replicated: uma cópia completa em cada nó. Funciona bem para dimensões pois são pequenas. 


Partições dentro das distribuições

São divisões dentro da própria distribuição. Só faz sentido começar a particionar quando tipos mais de 100 milhões de registros em uma tabela.
Criada em geral em colunas de data
Performance nas querys pois facilita a busca e filtragem dos dados


Recomendações
![Alt text](image-5.png) -->

## Comparativo

Característica | Data Warehouse | Data Lake | Lakehouse 
---- | ---- | ----- | ---- |
Tipo de dado | Estruturado apenas | Todos | Todos |
Formato | proprietário | csv, parquet, delta | parquet, delta, hudi, iceberg |
Usuários | analistas de dados | cientistas de dados | analistas e cientistas de dados |
Caso de uso | Análise descritiva | Análise e modelagem estatística | Análise e modelagem estatística |
Consumo | ---- | ----- | ---- |


## Quando usar MDW ou LH?
É dificil escolher, a infraestrutura de dados que armazena os dados de ambos estão padronizadas na mesma tecnologia, geralmente parquet (delta, hudi, iceberg)

Então a escolha tem que ser baseada em outros critérios, pois os usuários da plaforma podem anternar entre o uso de um MDW e um LH, ou armazenar dados que vem de um no outro.




Cenário | Escolha
------- | --------
Funcionalidades |Para direcionar a escolha, se você vai trabalhar com os dados usando um linguagem de programação como Python/R em notebooks em projetos de ciência de dados escolha Lakehouse, mas se precisa de funcionalidades de um banco relacional, como views, procedures e os dados possuem um schema mais estável escolha Data Warehouse.
Tipos de dados | Se você vai usar apenas dados estruturados escolha Data Warehouse, mas se no projeto de dados serão analisados dados em csv, json, parquet ou dados como texto ou imagem, vá com Lakehouse

O importante é a arquitetura permitir migrar de um para o outro de uma forma tranquila para atender os cenários dos projetos de dados


## Plataformas de Dados
Essa nova geração de soluções de dados que trazem uma plataforma integrada com soluções de orquestração de pipelines, processamento distribuido, object storage, Lakehouse, virtualização, ambiente de desenvolvimento para ciência de dados e BI, sendo oferecida como PaaS nas principais clouds implusiona e traz agilidade para empresas de todos os tamanhos conseguirem extrair valor dos seus dados. Essas plataformas se caracterizam por serem altamente modularizadas, o que permite criar arquiteturas mais simples ou mais complexas dependendo da realidade da empresa. 

Se pesarmos em níveis complexidade poderiamos ter por exemplo:

Nível | Componentes
----- | -----------
Nível 1: Basico | Fontes de dados -> Ferramenta de ETL -> Datawarouse/Lakehouse -> Ferramentas de BI
Nível 2: Médio | Fontes de dados -> Orquestradores -> Ferramentas de ETL -> Datawarehouse/Lakehouse -> Ferramentas de BI
Nível 3: Avançado | Fontes de dados -> Orquestradores -> Bancos de dados de streaming -> Ferramentas de ETL/streaming -> Bancos Datawarehouse/Lakehouse -> Ferramentas de BI > Plataforma de ML e deploy de modelos > Versionamento e CI/CD.

REDSHIFT
BIGQUERY
SYNAPSE

snowflake roda em  todos bom pra evoluirmos multcloud


## Data Mesh
Este novo padrão de arquitetura surgiu como resposta as arquiteturas centralizadasd e data lakes e data warehouses, invertendo o lógica e descentralizando o armazenamento e responsabilidade através do conceito de domínios de dados orientados a maneira que os dados são consumidos.

Os conceitos principais da arquitetura data mesh são:

- Domínios descentralizados

- Dados como produto

- Infraestrutura como plataforma self-service

- Governança federada



#### dominios
Domínio é uma representação de um assunto no mundo real ele representa um conjunto de serviços relacionados que podem ou não fazerem parte de outro domínio mas em outro contexto.  

Exemplo domínio atendimento 
Atendimento - produção/registro  
Domínio processo 
Atendimento - operação/execução 
Venda 

Domínio financeiro 
Venda  

Melhor forma de identificação dos domínios e funções é conversa com especialista no negócio  


# Outros Exmplos de Padrões de Arquitetura

Existe outras variações de padrões de arquitetura como "Data Fabric", "Data Vault"