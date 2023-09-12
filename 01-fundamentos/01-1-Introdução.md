# Introdução
Aqueles que acompanharam as tendências e transformações na área de dados podem ter a impressão de que novas ferramentas e padrões de arquitetura estão surgindo a cada instante. Novos formatos de armazenamento de dados, tecnologias de object storages, engines de processamento dados distribuídos como o spark, soluções especializadas de transformação como dbt, arquiteturas de data warehouses moderno como bigquery, azure synapse, Lakehouse no databricks, padrões como data mesh, ferramentas de virtualização de dados, práticas de Dataops, novos frameworks de machine learning, etc. São tantas inovações para as stacks de dados modernas que corremos o risco de perder o foco do propósito de uma arquitetura de dados que deveria ser: "enriquecer dados brutos, transformar, modelar e criar conjuntos de dados com qualidade e disponíveis para que as pessoas entender a dinâmica do negócio e identificar os padrões estatísticos que validam suas hipóteses." 

O fato é que a área de tecnologia com um todo vêm passando por transformação e a área de dados não poderia ser diferente. Essa rápida mudança ocasionada principalmente pelo aumento do volume de dados disponíveis fez com que novas tecnologias surgissem para lidar com desafios antes eram economicamente ou tecnicamente inviáveis. Soluções de bigdata e machine learning mudaram o panorama das arquiteturas das plataformas de dados e também redefiniram o escopo de atuação dos profissionais. Hoje, as equipes de dados são mais especializadas e lidam com desafios muito mais complexos. O que antes era atribuição de analistas de BI como por exemplo: criar pipelines, fazer transformações, modelagem e entrega, vemos como parte de funções de engenheiros de dados, engenheiros de machine learning, arquitetos de dados, analistas de dados, cientistas de dados, entre outros. Essa evolução é recente e está diretamente associada ao aumento da complexidade dos desafios dos projetos de dados, além disso, também é influenciada pelos bons resultados obtidos por empresas orietadas a dados.

Esse ecosistema de soluções que constumamos chamar de plataforma de dados modernas é que viabiliza esse novo cenário. Mas o que faz uma plataforma ser considerada moderna? Essa é uma questão que o guia vai buscar explorar através de conceitos, exemplos e recomendações. Vamos discutir os aspectos que permitem que uma plataforma seja considerada "moderna", como por exemplo: estar preparadas para múltiplos casos de uso, ser distribuída, ser capaz de se adequar a demanda de volume de dados e processamento, ter camadas independentes para que possa evoluir e se adaptar, entre outros vários princípios. 

Parte do sucesso de empresas orientadas a dados e que usam IA em suas aplicações como uber, ifood, nubank, picpay entre outras, está no fato de terem sido capazes de aplicar na prática a convergência entre 3 fatores: disponibilidade de dados, capacidade de processamento e evolução dos frameworks de machine learning. A IA sem volume de dados suficiente ou muitos dados mas sem algorítmos modernos não levariam ao mesmo resultado.

O primeiro passo para estabelecer uma arquitetura de dados adequada ao contexto da empresa é a definição clara de critérios e princípios que sustentem as escolhas arquiteturais, isso servirá de base para justificar a necessidade de cada componente e para alinhar a expectativas sobre o que é importante e porquê. Para termos uma ideia o landscape de soluções relacinadas à área de dados continua crescendo, por isso é tão importante estabelecer princípios para não se perder.

![Alt text](..\anexo\data-landscape-2023.png)
https://mattturck.com/landscape/mad2023.pdf

Mas apesar da grande quantidade de opções, quando pensamos em plataformas de dados em clouds públicas, vemos a convergência de alguns padrões e tipos de tecnologias como object storages, engines de processamento de dados distribuído, virtualização de dados, lakehouses. Não significa que existe uma única forma de fazer, ou uma plataforma definitiva, completa, que resolva todo os cenários, existe a necessidade de identificar as melhores opções com melhor custo benefício que melhor se adaptam a realidade da empresa e que quando for necessário seja possível mudar.


# Objetivos Guia

O guia busca a trazer um detalhahmento das melhores práticas estabelecidas em arquiteturas de dados modernas, apresentar estratégias de implantação e recomendações de tecnologias agnósticas, sempre com o propósito de encontrar o que melhor se adequa ao modelo federado do Sebrae, com independência das unidades mas com governança centralizada.

O guia também tem o objetivo de servir como meio para disseminar conhecimento entre os times envolvidos em atividades de engenharia de dados e servir de inspiração ou referência para dar os primeiros passos na direção de criar, evoluir ou justificar decisões de arquitetura em plataformas de dados. Este documento não tem o objetivo de estabelecer regras, ou servir como única referência, ele busca ser um material de apoio que traz uma visão de momento, do que poderia ser um bom caminho para estabelecer uma arquitetura, robusta, adaptável, escalável, reversível e simples.

# Estrutura do Guia
O guia é composto com quatro partes principais. *Parte I* busca delinear os objetivos, conceitos e princípios de arquitetura de dados como separação de responsabilidades, independência de formatos e linguagem, múltiplos casos de uso, análise descentralizada, simplicidade e escalabilidade. *Parte II* irá apresentar o ciclo de vida dos dados como espinha dorsal para ancorar e dar sentido para os componentes da aruitetura. Serão abordadas as relações de dependência, entradas, saídas, limites, responsabilidades, tecnologias e ao final um estudo de caso com o ciclo completo. Na *Parte III* vamos falar de arquitetura e propor diagramas que exemplificam como os componentes se relacionam. Serão discutidos os métodos para estruturação e storage "medallion", são apresentados os benefícios e vantagens das arquiteturas de data warehouse, data lake, lakehouse e data mesh. Além disso serão apresentados comparativos e recomendações de quando usar. Na *Parte V* vamos falar sobre tópicos relacionados a governaça e como  boas práticas de segurança, metadados e catálogo, versionamento de código em projetos de dados, gerenciamento de riscos elevam a maturidade e adicionam valor a plataforma de dados. 


>Referências:
https://www.lxahub.com/stories/key-takeaways-from-the-2023-ml-ai-data-landscape-report
https://airbyte.com/blog/data-engineering-past-present-and-future





