# Conceitos
Para alinhar os conceitos que serão usados ao longo do guia, vamos relacionar os termos e tecnologias mais comuns da área de engenharia de dados e detalhar o significado, objetivo e como ele se relaciona com as fases do ciclo de vida.

Conceito/Tecnologias | Descrição | Fase
-------------------- | --------- | -----
Data Warehouse | É um repositorio centralizado de dados criado para servir de fonte de dados para o desenvolvimento de relatórios e dashboards. Ainda é muito usado pelas empresas como estrutura de dados analítica de dados estruturados. Pode ser encontrado on-premise, ou em nuvem, em formato dedicado ou serverlles | Modelagem e Entrega
Modern Data Warehouse | São bancos de dados relacionais que possuem uma arquitetura distribuída, implementados com o conceito de separação da camada de storage da camada de processamento, capazes de escalar e executar consultas em SQL  | ----
Big Data |  ---- | -----
Column-store vs Row-store | ----- | ---
OLAP/Cubos | Online Analytical Processing são bancos de dados otimizados para análise de dados, possuem estruturas de dados colunares e são responsáveis por abrigar a camada semântica do modelo de dados. Também conhecidos como cubos, essas estruturas são montadas pensando na maneira como o analista utiliza os dados para criar relatórios e gráficos | Entrega
Bancos de dados de streaming | Banco de dados projetado especificamente para processar um fluxo constante de dados em tempo real. Ao contrário dos bancos de dados tradicionais, que armazenam dados em lotes antes do processamento, um banco de dados de streaming processam os dados assim que são gerados, permitindo insights e análises em tempo real. Casos de uso mais comuns são aqueles que exigem baixa latência como: recomendação de anúncios, detecção de fraudes, monitoramento de dispositivos, aplicações de entrega ou carros por aplicativo. Em conjunto com esse tipo de banco são usadas ferramentas especializadas de ETL em streaming e análise de streaming. | ------
Business intelligence | aplicações, infraestrutura e ferramentas que permitem estruturar explorar dos dados | -----
ACID | --- | Modelagem e Entrega
Data Lake | ---- | ----
Lakehouse | Padrão de arquitetura de dados que traz conceitos de ACID para datalakes baseados em object storage | Ingestão, Transformação, Modelagem
Virtualização de dados | ---- | ----
Governança de dados | ------ | -------
Computação distribuída | A escalabilidade e elasticidade de uma arquitetura são princípios desejáveis e podem ser obtidas de forma vertical aumentado recursos como cpu, memória e disco ou de forma distribuída/horizontal da inclusão de novos nós que atuam de forma orquestrada. O problema da escalabilidade vertical são os limites rígidos impostos pó próprio hardware e a continuidade em caso de falhas. Já arquitetura distribuída são virtualmente infinitamente escalaveis ao mesmo tempo mais confiáveis por um ou vários nós podem ser perdidos se afetar o processo. Basicamente um nós central distribui a tarefa para os worknodes eles executam e retornam ao no central ia resultados. Atualmente as soluções de data warehouse modernas MPP, object storages, spark funcionam dessa forma | ------
Data Mesh | --- | Ingestão, Transformação, Modelagem
Ingestão | ---- | ----
ETL, ELT/EtLT | --- | Ingestão
Metric Store | --- | Transformação, Modelagem
Domínio e Serviço | Domínio é a área de assunto que pode ter um ou vários serviços. Um serviço é um conjunto de dados específico associado a uma tarefa. Por exemplo, você pode ter um serviço de avaliação de atendimentos tarefa é monitorar a satisfação e outro serviço de processamento de cadastros de atendimentos onde o trabalho de processar os atendimewntos. Um domínio pode conter vários serviços. Por exemplo, você pode ter um domínio de atendimento com serviços: avaliação e castrastro e faturamento. Cada serviço tem tarefas específicas que apoiam o domínio de atendimentos. | Entrega
NoSQL | São bancos Not Only SQL, armazenam dados semi-estruturados como documentos json ou chave-valor que possuem flexibilidade no schema | -----
Modelagem dimensional | ----- | ------
Linhagem de dados | ----- | ------
Pull/Push Pull Request | ----- | ----
Schema-on-write e Schema-on-read | ----- | ----
Área de Stage | é uma área de armazenamento transitório, também referenciado com o landing zone, usado como area de storage durante o processo te ETL | ----
Granularidade | --- | --



