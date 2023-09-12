
## 02 - Idenpendência de componentes
A independência entre os componentes, principalmente entre a camada de storage e as engines de processamento (separação entre armazenamento e computação) é um princípio que traz benefícios como redução de custos, escalabilidade e flexibilidade para mudanças. Esse princício está presente nas stack de dados modernas e vem sendo o grande diferencial em comparação a modelos antigos baseados em data warehouse tradicionais.

Um exemplo são as arquiteturas de Lakehouse e data warehouses modernos como Azure Synapse, BigQuery, Databricks onde o storage é desacoplado da computação. Na prática o engine de processamento roda em clusters diferentes, dessa forma a arquiterura fica escalável e suporta muito mais usuários concorrentes ou volumes de dados maiores, se adptando ao caso de uso e tipo de demanda.

Além disso ter elementos independentes permitem:
- ser dimensionados de forma independente em momentos distintos
- ser substituídos conforme a convenência
- evoluir a medida que novas tecnologias surjam
- que os problemas sejam isolados
- que a arquitetura seja mais simples de ser entendida
- ter baixo acoplamento entre os componentes
- espalhar a arquitetura e pequenos componentes mais gerenciaveis

>As escolhas dos componentes que serão usados, precisam buscar o equilíbrio entre atender ao ciclo de vida dos dados como um todo com soluções com propósito amplo, ou soluções buscar soluções bem específicas, que atendam domínios de problemas únicos. Construir a arquitetura com flexibilidade de adaptação é o que permite equilibrar essa balança. Exemplo:....

