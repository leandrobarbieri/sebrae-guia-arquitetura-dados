Conceituação dos tipos de tecnologias: Requisitos e restrições das soluções e licenças das tecnologias que devem ser observados no processo de aquisição.

Ferramentas e Tecnologias Recomendadas: Sugestões de ferramentas e tecnologias que podem auxiliar na implementação da arquitetura de dados, como sistemas de gerenciamento de bancos de dados, ferramentas de integração de dados, entre outras.

As escolhas são sempre baseadas no contexto da empresa e no nível de maturidade analitica.


# sistemas distribuido
A escalabilidade e elasticidade de uma arquitetura são princípios desejáveis e podem ser obtidas de forma vertical aumentado recursos como cpu, memória e disco ou de forma distribuída/horizontal da inclusão de novos nós que atuam de forma orquestrada. O problema da escalabilidade vertical são os limites rígidos impostos pó próprio hardware e a continuidade em caso de falhas. Já arquitetura distribuída são virtualmente infinitamente escalaveis ao mesmo tempo mais confiáveis por um ou vários nós podem ser perdidos se afetar o processo. Basicamente um nós central distribui a tarefa para os worknodes eles executam e retornam ao no central ia resultados. Atualmente as soluções de data warehouse modernas MPP, object storages, spark funcionam dessa forma  



Tipos de tecnologias | Objetivo/Função | Fase do ciclo de vida | Exemplos de produtos
---------------------| --------------- | --------------------- | ---------------------
Orquestração de pipelines | --------------- | --------------------- | ---------------------
Object Storage | --------------- | --------------------- | ---------------------
Formatos de armazenamento | --------------- | --------------------- | ---------------------
ETL e Transformação | --------------- | --------------------- | ---------------------
Governança de dados e catálogo | --------------- | --------------------- | ---------------------
Data lake, Lakehouse e Data Warehouse | --------------- | --------------------- | ---------------------
Qualidade de dados e observabilidade |--------------- | --------------------- | ---------------------
Processamento de dados | --------------- | --------------------- | ---------------------
Bancos OLAP |  --------------- | --------------------- | ---------------------
Liguagens e frameworks | --------------- | --------------------- | ---------------------
BI e Visualizalização de dados | --------------- | --------------------- | ---------------------
Frameworks de ML
