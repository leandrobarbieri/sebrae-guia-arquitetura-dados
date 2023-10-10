Código | Questão | Recomendação | Princípio
------ | --------- | --------- | ---------
R01-Storage | Como armazenar de forma correta dados em bases de relacionais? | Não armazenar dados semi-estruturados em base relacional e garantir que todas as tabelas com dados analíticos estejam armazenados como column-store | P6
R02-Storage | Como garantir que os dados possam ser acessados por diversos compomentes de processamento e análise de dados? | os dados não devem estar em formato proprietario, exclusivo do produto do storage (devem estar em formato aberto, comum a maioria das ferramentas). 

- usar parquet na bronze por ser mais generalista e delta ou iceberg na silver e gold

- colocar pk e foreign key no começo da tabela