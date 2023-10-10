## P08 - Descentralização
>_As decisões de governaça podem ser hibridas/federadas e o consumo dos dados descentralizado, ao mesmo tempo que a governança se mantém centralizada._

A arquitetura deve ser descentralizada a ponto de poder crescer de forma independente, sem perder a possibilidade de compartilhamento das camadas de storage, controle de acesso e catálogo. 

Essa abordagem federada pode trazer agilidade nas tomadas de decisões pois cada participante por ter sua própria stack de dados, facilitando assim a adoção e a evolução de cada unidade em ritmos diferentes. 

Outra perspecetiva da descentralização é a do consumo. A arquitetira deve permitir a análise de dados descentralizada, com o incentivo ao self-service BI. Mas ao mesmo tempo é necessário mater o desenvolvimento dos datasets endossados pela empresa, evitando ao máximo a proliferação de dados fisicamente duplicados.

#### Exemplo
Uma unidade pode construir uma stack de dados usando um conjunto de tecnologias abertas, enquanto outra unidade usa outro conjunto de tecnologias, mas mantém os mesmos princípios, garantindo que seja possível que essas diferntes plataformas compartilharem a mesma infraestrutura, por exemplo, usando o mesmo catálogo e storage distribuído, ao mesmo tempo que diferentes ferramentas de processamento, orquestração e análise são usadas para implementar o ciclo de vida dos dados. A descentralização da arquitetura não implica necessariamente em falta de governança desde que a plataforma tenha padrão abertos. Criar uma arquitetura

Deve-se manter governança centralizada.

#### Benefícios
A descentralização pode trazer agilidade nas escolhas, flexibilidade para cada unidade escolher como quer evoluir sua arquitetura e redução de custos, quando permite evoluir de acordo com o momento e o nível de maturidade atual da unidade.