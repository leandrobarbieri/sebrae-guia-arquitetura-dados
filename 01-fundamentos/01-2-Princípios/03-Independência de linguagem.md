# P03 - Independência de linguagem
> _Os profissionais devem ser capazes de exercer as atividades nos projetos de dados usando as liguagens que possuem maior proeficiência_

As linguagens de programação, de consulta ou de prompt são os meios pelos quais os profissionais exercem sua proeficiencia para realizar as tarefas e implementar os pipelines, as transformações, o deploy das soluções, as análises e até o storytelling na entrega. 

A plataforma que não cria barreiras para a utilização das principais linguagens se beneficiam, pois direcionam o foco do profissional ao código das regras de negócio das etapas do pipeline. Tecnologias como virtualização de dados criam essa camada de abstração de linguagens. A virtualização de dados padroza a forma de interagir com tecnologias diferentes usando uma mesma linguagem. Exemplo com uma solução como Microsoft Polybase o analista de dados pode usar SQL-ANSI para consultar uma base NoSQL no Mongo DB, ou com Python, ele pode fazer webscrapping em um página Web ao mesmo tempo que se conecta ao um banco relacional ou a um arquivo parquet.

Cada profissional possui suas habilidades, e cada linguagem tem suas características. Na área de dados em geral as linguagens mais comuns são sql, python/r e bash.

#### Exemplos
O **SQL** é considerado a liguagem franca da área de dados. Essa linguagem passou pelo teste do tempo, surgiu na década de 70 e até hoje é amplamente usada. Trata-se de uma liguagem madura, muito conhecida e que ganhou ainda mais relevancia quando foi adotada por soluções de data warehouse e lakehouse modernos como SparkSQL, BigQuery, Snowflake. Um dos fatores do sucesso está na forma declarativa, que abstrai o algorítimo de execução da consulta e que facilita muito a explicabilidade dos comandos.

O **python** é uma linguagem com um conjunto amplo de bibliotecas de manipulação de dados (numpy, pandas, polars) de visualização de dados (matplotlib, seaborn, plotly, etc) e machine learning (sklear, tensorflow, pytorch), gera um código limpo devido sua sintax bem construída. Muitas das principais soluções de código aberto que se destacam na área de dados suportam python, ou tem APIs em python (Apache Airflow, Kafka, Dremio, MinIO, PySpark, Superset, etc). Essa é a linguagem que faz a ponte entre as áreas de Engenharia de Dados e Ciência de Dados. 

A linguagem de script **Bash**, permite trabalhar com a linha de commando linux. Assim como python, as principais soluções da área de dados possuem CLI que permitem automatizar tarefas e aumentar a produtividade, principalmente nas fases de implantação. Está muito associada às atividades de manutenção e sustentação da plataforma de dados.

Esse princípio deve ser sempre considerado sob a perpectiva da eficiencia da liguagem. O principal benefício é a produtividade e a possiblidade de absorver mudanças ao longo do tempo, seja pela evolução do próprio mercado, seja porque novas bilbiotecas surguiram em outras linguagens.


