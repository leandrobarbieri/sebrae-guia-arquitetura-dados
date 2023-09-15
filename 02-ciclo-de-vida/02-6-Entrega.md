# o que
> Abordar aqui asrelações de dependência, entradas, saídas, limites, responsabilidades, tipos de tecnologias


> qual é o propósito da fase de entrega. A importancia dos metadados e descoberta. Delinear entradas, saídas limites e fronteiras

Nem só de dashboard vide a análise de dados, o analista de dados pode e deve ir muito além de criar gráficos, ele deve contar histórias, contextualizar, identificar correlações, fazer análise de impacto. 

Pode utilizar modelos treinandos ou treinar seu próprios modelos. É importante a arquitetura estar preparada para se integrar com soluções de gestão de modelos como mlflow que gerencia os experimentos e registro dos modelos de forma que o analista possa usar como parte dos scritps sql, usando um conjunto de colunas para submentar a inferencia de um modelo.



# como
camada gold, dw ou cubo? como e porque cada uma das opções
, catalogo, segurança, machine learning, BI, self-service, storytelling, etc

Caso de uso | Siver | Gold | DW | Cubo | Painel | Obs
------------| ----- | ---- | -- | ---- | ------ | ---
Investigação de hipótese e correlação | x | x | x | - | - | -
Desenvolvimento de modelo estatísco | x | x | x | - | - | Dados nas camadas integração frameworks de ml
Análise ad-hoc | - | - | x | x | - | Dados modelados ideal para consulta SQL e ferramentas de viz
Acompanhamento de indicadores | - | - | - | - | x | -


# Boas práticas
Dados brutos ou modelados, com catálogo e segurança, dados sensíveis separados, alternativas para consumo direto do data lake ou através de data warehouse dependendo do caso de uso. Ambiente para publicação e monitoramento de modelos estatísticos de ML

3-Entrega: Painéis de BI com modelos OLAP criados para cada painel

3-Entrega: Dados modelados que podem ser usados por diferentes tipos de tecnologias de análise ou ML

3-Entrega: Dados brutos ou modelados, com catálogo e segurança, dados sensíveis separados, alternativas para consumo direto do data lake ou através de data warehouse dependendo do caso de uso. Ambiente para publicação e monitoramento de modelos estatísticos de ML

# para analise
Nem só de dashbord vive um empresa 
não criar paineis com filtros implicitos
prototipar no excel antes de criar dashboards
principios gestapo


# para ml
Cientista de dados deve pegar da camada limpa de Gold 




Logical consumption layer
The consumption layer is responsible for providing scalable tools to gain insights from the vast amount of data in the marketing CDP.

Analytics layer – Enables consumption by all user personas through several purpose-built analytics tools that support analysis methods, including ad-hoc SQL queries, batch analytics, business intelligence (BI) dashboards and ML-based insights. Components in this layer should support schema-on-read, data partitioning, and a variety of formats.
Data collaboration layer – Consists of data clean rooms where organizations can aggregate customer data from different marketing channels or lines of business, and combine it with first-party data to gain insights while enforcing security, anonymization, and compliance controls.
Activation layer – This layer integrates customer profiles with the organization. It can also integrate with third-party SaaS providers in the advertising and marketing industry, and is capable of enriching data sets for consumption.

https://aws.amazon.com/pt/blogs/architecture/overview-and-architecture-building-customer-data-platform-on-aws/


# Recomendações do guia
Código | Recomendação | Descrição
------ | ------------ | ---------
R01-ENT | A empresa deve ter uma infraestrutura de dados sólida e madura antes de focar em iniciativas de ML | A produtividade de cientistas de dados depende da disponibilidade de dados, da qualidade, da capacidade de lidar com volumes grandes, da infraestrutura de orquestração de pipelines para produtizar os modelos estatísticos. Tudo isso depende de infraestrutura previamente estabelecida.

