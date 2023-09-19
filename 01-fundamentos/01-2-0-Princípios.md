# Princípios para uma boa arquitetura

Atualmente a diversidade de tipos fontes de dados, a disponibilidade de informações e o volume disponíveis são um grande desafio mas também uma grande oportunidade. Os benefícios uma arquitetura capaz de se adaptar rapidamente às necessidades, alinhada aos padrões de mercado, nos dará uma boa referência de caminho a seguir.

Projetar uma arquitetura de dados envolve identificar os elementos necessários, as interfaces, as entradas e as saídas de cada fase do ciclo de vida.

As decisões e as escolhas devem ser sempre reversíveis, isso dá um bom indicativo de uma arquitetura robusta, capaz de se adaptar com o tempo. Não depender de um fabricante, modelo ou produto é altamente desejável e está no centro do conceito de plataforma de dados moderna. Mesmo que hoje algumas tecnologias sejam consideradas estado da arte, no futuro não muito distante isso pode mudar, além disso, com o aumento da maturidade da empresa novos casos de uso podem demandar evolução ou substituição de componentes.

Estabelecer os princípios nos ajuda a entender o que faz mais sentido para o contexto atual e futuro da empresa, pensar em termos que estabelecem as características mais importantes facilitam o processo de decisão e as escolhas passam a ser mais direcionadas a propósito e menos a preferencias pessoais.

Os princípios são apenas aspectos desejáveis, não impõe restrições, tratam sempre de recomendações que na prática, quando bem implementados se tornam os direnciais das soluções gerenciadas por plataformas como databricks, azure, gcp, aws.

Vamos a seguir discutir os 10 princípios que para o Sebrae devem ser considerados para a implementação de uma arquitetura de dados.

Cód | Nome | Conceito principal
--- | ---- | ------------------
P01 | Separação das responsabilidades | Cada componente com um papel bem definido e especializado (sem sobreposições de funcionalidades)
P02 | Independência de componentes | Componentes podem ser substituídos, escalados ou desativados de forma isolada sem comprometer o todo
P03 | Independência de linguagem | Os profissionais deve ser capazes de exercer as atividades as liguagens que têm maior proeficiência
P04 | Independência de formatos de dados | Os dados devem estar em formatos abertos, comuns às diversas tecnologias de processamento e consumo
P05 | Adaptável ao contexto | A arquitetura de ver flexível para se adequar às naturezas de casos de uso diferentes
P06 | Multicloud | A empresa deve ser capaz de realizar a implantação da arquitetura e diferentes clouds públicas
P07 | Escalabilidade | Os componentes devem ser capazes de se adaptar a demanda de conexões, processamento e volumes de dados, aumentando ou diminuindo recursos
P08 | Descentralização | As decisões de governaça podem ser hibridas/federadas e o consumo dos dados descentralizados (self-service com governança federada)
P09 | Decisições reversíveis | As escolhas podem ser revisadas e desfeitas sem afetar o todo. Arquitetura preraparada para mudança
P10 | Simplicidade | Os componentes devem ser fáceis de usar, devem facilitar ou atomatizar a execução de tarefas comuns


## Próximos passos

- [01-2-01-Separação das responsabilidades](https://github.com/leandrobarbieri/sebrae-guia-arquitetura-dados/blob/main/01-2-01-Separa%C3%A7%C3%A3o%20das%20responsabilidades.md)
- [01-2-02-Independência de componentes](https://github.com/leandrobarbieri/sebrae-guia-arquitetura-dados/blob/main/01-fundamentos/01-2-02-Independência%20de%20componentes.md)
- [01-2-04-Independência de formatos de dados](https://github.com/leandrobarbieri/sebrae-guia-arquitetura-dados/blob/main/01-fundamentos/01-2-04-Independência%20de%20formatos%20de%20dados.md)
- [01-2-05-Adaptável ao contexto](https://github.com/leandrobarbieri/sebrae-guia-arquitetura-dados/blob/main/01-fundamentos/01-2-05-Adaptável%20ao%20contexto.md)
- [01-2-06-Multicloud](https://github.com/leandrobarbieri/sebrae-guia-arquitetura-dados/blob/main/01-fundamentos/01-2-06-Multicloud.md)
- [01-2-07-Escalabilidade](https://github.com/leandrobarbieri/sebrae-guia-arquitetura-dados/blob/main/01-fundamentos/01-2-07-Escalabilidade.md)
- [01-2-08-Descentralização](https://github.com/leandrobarbieri/sebrae-guia-arquitetura-dados/blob/main/01-fundamentos/01-2-08-Descentralização.md)
- [01-2-09-Decisições reversíveis](https://github.com/leandrobarbieri/sebrae-guia-arquitetura-dados/blob/main/01-fundamentos/01-2-09-Decisições%20reversíveis.md)
- [01-2-10-Simplicidade](https://github.com/leandrobarbieri/sebrae-guia-arquitetura-dados/blob/main/01-fundamentos/01-2-10-Simplicidade.md)
	
