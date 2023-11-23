# Conceitos
Para alinhar os conceitos que serão usados ao longo do guia, vamos relacionar os termos e tecnologias mais comuns da área de engenharia de dados e detalhar o significado, objetivo e como ele se relaciona com as fases do ciclo de vida.

Conceito/Tecnologias | Descrição | Fase
-------------------- | --------- | -----
ACID | --- | Modelagem e Entrega
Data Warehouse | É um repositorio centralizado de dados criado para servir de fonte de dados para o desenvolvimento de relatórios e dashboards. Ainda é muito usado pelas empresas como estrutura de dados analítica. Pode ser encontrado on-premise, ou em nuvem, em formato dedicado ou serverlles | Modelagem e Entrega
OLAP | Online analytics processing. São bancos de dados otimizados para análise de dados, possuem estruturas de dados colunares e são responsáveis por abrigar a camada semântica do modelo de dados. | Entrega
Lakehouse | Padrão de arquitetura de dados que traz conceitos de ACID para datalakes baseados em object storage | Ingestão, Transformação, Modelagem
Data Mesh | --- | Ingestão, Transformação, Modelagem
Metric Store | --- | Transformação, Modelagem
Domínio e Serviço | Domínio é a área de assunto que pode ter um ou vários serviços. Um serviço é um conjunto de dados específico associado a uma tarefa. Por exemplo, você pode ter um serviço de avaliação de atendimentos tarefa é monitorar a satisfação e outro serviço de processamento de cadastros de atendimentos onde o trabalho de processar os atendimewntos. Um domínio pode conter vários serviços. Por exemplo, você pode ter um domínio de atendimento com serviços: avaliação e castrastro e faturamento. Cada serviço tem tarefas específicas que apoiam o domínio de atendimentos. | Entrega



