# P06 - Multicloud
Esse princípio busca estabelecer como objetivo a escolha de componentes que não dependem de um provedor de nuvem específico, amplia as possibilidades atuais e futuras de migração, atualização e evolução da plataforma em uma estratégia de longo prazo. É importante ter um provedor de referência e se beneficiar das integrações entre seus produtos, mas não podemos deixar de considerar a escolha de componentes específicos que criam o lock-in de fornecedor. 

A abordagem de desenvolver soluções de dados usando os serviços nativos de uma cloud preferida é muito comum mas cria uma série de desafios de longo prazo:

Desafio | Descrição
------- | ---------
Multiplas versões de código | Necessidade de manter multiplas repositórios de código para uma mesma aplicação para conseguir rodar em serviços nativos de uma cloud
Multiplos builds de infraestrutura | Diferentes versões de scripts de builds para gerenciar a infraestrutura da cloud específica
Multiplas habilidades | necessidade de ter multiplas competências para conseguir suportar serviços em clouds específicas

Para alcançar uma arquitetura multicloud busque sempre usar: formatos de dados abertos, storages e engines de processamento que existem em todas as clouds, e desenvolva os projetos de dados usando padrões estabelecidos como data warehouses, lakehouses.

Crie a infraestrutura como código usando abstrações com ferramentas como o terraform, solução de código de aberto para deploy de infraestrutura na nuvem, compatível com vários provedores.

Como os provedores de nuvem ofereceram uma interface por linha de comando para automação de tarefas e gestão da infraestrutura, é possível orquestrar o deploy de servicos de forma automatizada, a questão que surge nesse contexto multicloud, é que vários comandos diferentes implementados por cada provedor de nuvem, surge a necessidade de uma abstração capaz de traduzir o comando criada em cada comando específico de cada nuvem.


## Exemplo
Um bom exemplo é o apache airflow, uma solução open-source para orquestração de pipelines. Essa solução pode ser usada como ferramenta de ELT/ETL, como orquestrador de dados ou de machine learning e pode ser implantada tanto on-premise, hibrida ou gerenciada como produtos das principais clouds. No Google ela se chama "Google Composer", na Microsoft está como feature do Data Factory e na AWS é o produto  Managed Workflows para Apache Airflow. Ou seja, um pipeline criado em Airflow, poderia rodar nas principais clouds sem muitos ajustes. 

Cloud | Ferramenta Orquestração/ETL | Versão Airflow Gerenciado
----- | ---------- | --------------
Google | Cloud Data Fusion | [Composer](https://cloud.google.com/composer/docs/concepts/overview?hl=pt-br)
Microsoft | Data Factory | [Data Factory Managed Airflow](https://learn.microsoft.com/pt-br/azure/data-factory/concept-managed-airflow)
AWS | AWS Glue | [Data Factory Managed Airflow](https://docs.aws.amazon.com/pt_br/mwaa/latest/userguide/what-is-mwaa.html)


O Databricks é outra ferramenta multicloud que permite rodar uma plataoforma de dados completa nas principais clouds públicas.

https://www.databricks.com/blog/multi-cloud-architecture-portable-data-and-ai-processing-financial-services


## Benefícios
Uma arquitetura moderna e multi-cloud traz os benefícios de ser capaz de atender mudanças geográficas (caso decidam descontinuar algum datacenter em uma determinada região), geopolítica e regulatória (caso alguma restrição legal obrigue a mudar para outra região) e de mercado caso haja mudança de preço no catálogo de serviços. 

Pensar em uma plataforma multicloud direciona as ações no sentido de ter uma arquitetura mais aberta, formatos abertos, portáveis, com APIs comuns a várias engines de processamento. Essa independencia de cloud aumenta a qualidade dos produtos e o valor pois diminui a necessidade de refatorar código em casos de mudanças futuras.

Outro benefício é que ao trabalhar o contexto multicloud faz com que tenhamos que criar a infraestrutura como código (IaC) o que permite criar pipelines de CI/CD que trazem eficiência e permitem maior controle sobre as mudanças. 


> Falar sobre como isso ajuda a criar um plano de disaster recovery
