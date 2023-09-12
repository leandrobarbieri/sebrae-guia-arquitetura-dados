# O que?
> o que acontece nessa fase, entradas e saídas, objetivos. Delinear entradas, saídas limites e fronteiras

Um ponto crítico para ter uma arquitetura de dados moderna é saber dazer a modelagem


# Porque
> Importancia de separar a transfornação da modelagem (a primeira cria um produto com dados tratados mas sem regras de negócio, essa com regras e dados modificados para atender casos de uso)

# Como
> tipos de tratamentos e transformações. Modelagem: relacionamentos, joins, semântica, dimensões, fatos, etc

# Exemplos
> das operações acima, de modelagem multidimensional e OLAP. Melhores práticas para modelos oplap (tabular)

sc typ2 delta 
https://docs.delta.io/latest/delta-update.html#id2





Logical processing layer
This layer is responsible for transforming data into a consumable state by applying business rules for data validation, identity resolution, segmentation, normalization, profile aggregation, and machine learning (ML) processing. This layer comprises custom application logic. The compute resources for this layer are designed to scale independently from storage to handle large data volumes; support schema-on-read, support partitioned data and diverse data formats; and orchestrate event-based data processing pipelines.