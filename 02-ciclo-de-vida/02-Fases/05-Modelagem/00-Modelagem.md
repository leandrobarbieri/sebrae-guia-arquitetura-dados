# Fase: Modelagem
Essa é uma camada onde a lógica de negócio da empresa é aplicada aos datasets. Nessa fase os dados são mais orientados aos domínios e não matém total relação com a fonte de dados original. Junções entre várias tabelas, concatenação entre atributos, colunas calculadas, agregações, segmentaçõs, novos atributos derivados e muitos outros tipos de processamentos que podem mudar significativamente os dados originais nessa camada.

O objetivo principal agora é preparar os dados para consumo, principalmente por analistas de dados e analistas de negócio. Cientistas de dados também clientes desta camada, mas em geral seus projetos se beneficiam mais de camadas anteriores (bronze, silve) pois os dados estão mais próximos do estado bruto o que possíbilita diferentes combinações e validações de hipóteses não mapeadas. 

## Entradas
Deixam os dados prontos para consumo das ferramentas de visualização

É a etapa que prepara o dado para ser servido de acordo com as necessidades específicas do negócio. 
				
Diferente da transformação, a modelagem adiciona regras de negócio, semantica para os campos, desnormalização, joins, dê-para, agregações. A modelagem é voltada para simplificação  do schema para a entrega para o negócio
				
Exemplo: nessa fase são feitos joins com entidades externas podem adicionar features: join de uma localização com as coordenadas, um de-para de uma unidade da empresa uma área de atuação, etc..



## Escopo
Fronteira entre a camada de qualidade e camada semântica
Filtra qualquer tipo de dados que não precisa ser exposto para análise
A transformação ocorrida na fase anterior não depende de contexto de utilizaçaõ dos dados as transformações buscam trazer integridade e limpeza
Qualidade dos dados
Deduplicação
Parse de atributos
Padronização de formatos
Monitoramento de falhas e incrementos

A fase de modelagem já dependente de caso de uso, altera a essencia do dado de certa forma limita o uso mas enriquece com:
Agregações
Joins / Unions
Dê-para
Métricas e indicadores



# técnicas e modelagem
- dimensional
- slowly change dimension


## Saídas
A simplificação obtida através da modelagem nessa fase do ciclo de vida, transforma os conjuntos de dados tratados em produtos, prontos para o usuário final consumir através de ferramentas de análise de dados. O objetivo dessa fase foi alcançado quando não há necessidade de conhecer os aspactos das fontes de dados originais para conseguir fazer análise dos dados.





# Exemplos
> das operações acima, de modelagem multidimensional e OLAP. Melhores práticas para modelos oplap (tabular)

sc typ2 delta 
https://docs.delta.io/latest/delta-update.html#id2


# camada semantica
Conceito de desacoplamento da camada semantica empresa Transform comprada pelo dbt 
dbt Semantic Layer, Enabling Greater Consistency Across Analytics Tools

![Alt text](image.png)
https://github.com/dbt-labs/metricflow

https://www.getdbt.com/blog/dbt-acquisition-transform

https://www.prnewswire.com/news-releases/dbt-labs-launches-the-dbt-semantic-layer-enabling-greater-consistency-across-analytics-tools-301652226.html

>What Transform introduced to all of us was the incredible potential of semantic capabilities that are decoupled from a single business intelligence tool – or, “headless semantic layer”. In this world, metrics and entities are no longer locked into a single BI tool, they can be accessed by all downstream tools. 



# Recomendações





Código | Recomendação | Descrição | Princípios
------ | ------------ | --------- | ----------
R01-Modelagem | Os dados da camada de modelagem devem estar organizados com base nos domínios da informação e não mais pelos contextos das fontes de dados. | Como os dados estão sendo preparados para atenderem as necessidades do negócio, fontes de dados de sistemas diferentes podem ser agrupadas em um domínio único. | P05
R02-Modelagem | A modelagem deve esconder a maior parte da complexidade das fondes de dados originais | Toda a camanda semântica deve ser orientada ao consumo. Remover a normalização, simplicicar nomenclatura de atributos, mudar granularidade, criar métricas calculadas, etc.
R03-Modelagem | Os dados armazenados na camada de modelagem (gold) devem estar no mesmo storage e formatos de arquivos que as camadas anteriores.
R04-Modelagem | A camada de modelagem deve ser otimizada para consumo | As tecnologias de MDW, com particionamento, processamento distribuído, storages com discos rápidos (hot)
R05-Modelagem | Os recursos computacionais desta camada devem ser para escalar de forma independente dos recursos de storage, para acomodar o comumo massivo.
R06-Modelagem | Views materializadas podem ser criadas para simplificar o otimizar o consumo | Views ajudam a diminuir a complexidade e quando materializadas podem trazer performance. Usar apenas quando há a possibilidade de analisar a linhagem dos dados.


> RX | Desacoplar a camada semântica das ferramentas de BI (metric store) | Uso de ferramendas de BI diferentes com a mesma metrica, propagação de mudanças, melhor consistencia, confinça que todos estão usando a mesma logica dos indicadores, concistencia entre ferramentas de BI
