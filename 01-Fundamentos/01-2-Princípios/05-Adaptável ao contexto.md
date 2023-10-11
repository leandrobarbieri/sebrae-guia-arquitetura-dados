
## P05 - Adaptável ao contexto de uso
>_A arquitetura de ver flexível para se adequar às naturezas de casos de uso e tipos de usuários com níveis de conhecimento e necessidades diferentes_

A arquitetura da plataforma de dados deve ser adaptável e flexível para atender diferentes casos de uso de projetos de dados. Atender os workloads de analistas de negócio, analistas de dados,  cientista de dados e engenheiros de dados através de ferramentas específicas e tipos de dados com níveis de transformações diferentes, disponíveis em estado bruto, tratados, modelados. 

Deve haver compatibildade com frameworks de ML, linguagens de consulta ou ferramentas de BI, e todas devem consumir o mesmo repositório de dados compartilhado.


#### Exemplos
Os dados quando estão armazenados em camadas diferentes, com níveis de tratamento diferentes, no estado bruto, tratado ou modelado, isso permite por exemplo que um analista de negócio utilize os dados modelados, o analista de BI use os dados tratados e os cientistas de dados usem os dados brutos. O mesmo dataset pode ser usado em scritps Python, SQL ou em ferramentas de BI.