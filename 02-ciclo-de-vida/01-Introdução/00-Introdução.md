# Introdução do ciclo de vida
As fases do ciclo de vida refletem o esforço para obter os dados das diversas fontes para criar um pipeline de dados capaz de adicionar valor e qualidade, transformando dados brutos em conjuntos de dados enriquecidos, modelados e prontos para serem consumidos.

É semelhante a produção de um produto qualquer que transforma materia prima em produto acabado. Os dados são a matéria prima e os conjuntos de dados analíticos e modelos de machine learning são os produtos acabados.

Uma analogia com o ciclo de vida de um produto de consumo.

![analogia](../media/analogia.png)


O ciclo de vida dos dados deve ser desenvolvido considerando os diversos perfis de consumo. Cada fase define um objetivo específico e atribui sentido para os componentes e as relações de dependência, entradas, saídas, limites, responsabilidades, tecnologias utilizadas.

Vamos trazer detalhes sobre quais artefatos serão gerados, tipos de tecnologias utilizadas, entradas, saídas e recomendações do que deve ser feito em cada fase. 

Podemos considerar o ciclo padrão com 4 fases principais: Ingestão, Transformação, Modelagem e Entrega. E 2 fases externas, a exploração, que antecede o ciclo e a análise/modelagem estatística, que utiliza dados entregues.
  

## Padrão Medallion
Antes de começarmos o detalhamento de cada fase do ciclo de vida, vamos conhecer o padrão "medallion". Ele vem se tornando uma espécie método para organização, limpeza e padronização de dados em Lakehouses. A sua lógica de separação em camadas, que adiciona qualidade a medida que o dado é movido entre as elas no object storage faz dele um reflexo do ciclo de vida dos dados, desde a exploração inicial até o consumo. 

A ideia de camada bronze, prata e ouro remete ao incremento de qualidade e valor adicionado para o negócio. 

As camadas deste método adicionam qualidade através de validações, checagens, padronizações, enriquecimento com regras de negócio. Além disso, criam as fronteiras de segurança necessárias para entrega dos dados a públicos específicos, de acordo com o caso de uso.

  
![Alt text](../media/image-11.png)


### Bronze
Essa é a camada da dados brutos, é o ponto de entrada dos dados que vêm das fontes originais, sempre de um para um, cada tabela da fonte terá uma tabela na bronze (mesma quantidade de linhas e colunas). Todo tipo de dado deve ser possível armazenar aqui, seja ele estruturado, semi-estruturado, não estruturado. Não são feitas transformações e o formato original é mantido. Essa camada tem o objetivo de receber os dados ingeridos os mais rápido possível para liberar a fonte de dados original do fluxo de dados de consumo. Essa camada pode receber metadados como nome da fonte de dados, data/hora. método de usado na ingestão, etc. Essa camada deve ser usada explusivamente para ingestão dos dados, os dados nunca devem ser ingidos na Silver ou na Gold e os usuários nunca devem ter acesso a essa camada, se precisarem de dados brutos, crie um clone na camada gold para entrega.

O principal benefício é fazer com que todos as cargas de trabalho após a ingestão aconteçam de forma mais rápida e não afetem as fontes de dados originais

![alt text](image.png)


### Silver
Essa é uma camada de validação, se preocupa em criar tabelas que representam as entidades de domínios. Enquanto da bronze podemos ter várias tabelas de produtos, vindo de vários sistemas diferentes, na Silver teremos uma tabela que continua representando o produto, porém no contexto geral, represemta produto independente da origem. Nessa fase as primeiras checagens de qualidade são feitas. Os dados são refinados, transformações como deduplicação, limpeza de valores nulos, ofuscação, padronização de formato, entre outras. Nesta camada a preocupação principal deve estar em deixar o dado consistente e completo. Regras de negócio que modificam as representação dos dados não devem ser incluídas aqui, na Silver temos uma visão operacional e não de negócio. Nesse momento os dados estão prontos para serem usados em contextos específicos, muitas vezes cientistas de dados buscarão na Silver realizar a validação de hipóteses em dados que ainda não estão modelados. Evite entregar o acesso aos usuários diretamente nessa camada, se for necessário crie clones na camada gold para que mudanças nessa camada possam ser feitas sem afetar o que foi desenvolvido.

Sempre implementar a Silver no processo, independente de será alterada ou não na gold

### Gold
Aqui os dados estão sendo preparados para consumo. Geralmente é onde acontece a modelagem. Nessa camada os dados são modificados para atender casos de uso específicos. Entre ações que ocorrem nesta camada estão, agregações, dê-paras com dados externos, expressões com cálculos, joins, unions, e vários outras operações que modificam e preparam para responder questões de negócio. Pode haver mais de uma camada gold por exemplo, otimizada para ciêntistas de dados, ou a camada gold pode estar fora do datalake e ser entregue através de um data warehouse. A função dessa camada é servir como local de entrega, combinando de diferentes formas as entidades de domímio criadas na Silver. As mesmas tabelas da Silver podem ser combinada de N formas na Gold para satisfazer diferentes demandas do negócio. Por exemplo, podemos entregar uma modelagem Star Schema ou criar tabelões desnormalizados e agregadas para satisfazer as demandas.

### Canadas adicionais
Não há problema em ter camadas adicionais, isso sempre vai depender do projeto, pode haver situações que uma camada adicional, raw ou landing por exemplo, precisa ser criada para receber os dados para depois ingerir na bronze, ou quando alguns sistemas não conseguem ler o formato padronizado na bronze. Também pode haver necessidade de uma camada para dados sensíveis ou para um caso de uso muito específico. O importante é manter a filosofia do padrão, separar as reponsabilidades e adicionar qualidade aos dados a cada camada de transformação.

Separar em diferentes camadas otimiza o processamento de dados e permite atender diferentes casos de uso, onde cada camada esteja alinhada com as necessidades de um perfil de usuário. 

Em resumo a bronze e á área de dados brutos, a silver de dados de domínio e a gold de negócio.

### Checklist de transformação de dados
Antes de mover os dados entre as camadas veja:
- Qual é o volume de dados que será movido?
- Qual é a complexidade das transformações?
- Qual é a frenquência?

Fazer essas perguntas te ajudará a selecionar as melhores alternativas de ferramentas e abodagens. Por exemplo, para mover um grande volume de daos sem fazer transformações complexas, podemos usar conectores nativos de um orquestrador, para mover os dados e aplicar regras de negócio ou realizar transformações, podemos usar um engine de processamento.

### Perfil dos profissionais e áreas de conhecimento

Cada fase deste ciclo envolve diferentes habilidades e profissionais com conhecimentos em todos os componentes da arquitetura são difíceis de encontrar, cada pessoa envolvida pode ter mais proeficiencia em uma parte do ciclo de vida dos dados ou conhecer uma tecnologia específica. O mais importante é identificar os tipos de atividades e os tipos de profissionais dentro da mesma função e equilibrar o time e cobrir todos os gaps de conhecimento.

Podemos dividir a área de dados em 2 grandes grupos e em cada grupo identificar o tipo de profissional.


Área de Conhecimento | Tipo 1 | Tipo 2 | Tipo 3
---------- | ------ | ------ | -------
Engenharia de dados | Perfil mais técnico, responsável por manter, gerenciar e evoluir a plataforma usando produtos gerenciados em ecosistemas de clouds públicas. Ele implanta o lakehouse/data warehouse, desenvolve os pipelines de ingestão de dados, serve os analistas de dados com conjuntos de dados tratados | Perfil de engenheiros que constrõem soluções customizadas, escalavés, conhece muito infraestrutura como código (terraform), orquestração de containers e devops. Esse tipo se dedica a aprimorar e automatizar aplicações baseadas em dados, trabalha em conjunto com os engenheiros de software para que as aplicações já nascam orientada a dados e que a qualidade seja uma preocupação desde do desenvolvimento. | Perfil de engenharia de dados voltado para desenvolver e implatar infraestrutura pra rodar modelos de ML em produção. Conhece práticas de Devops e o ciclo de vida de modelos (experimentação, treinamento, avaliação, implantação, re-treino) e frameworks de ML. Também conhecido com engenheiro de machine learning.
Cientista de Dados/Analista de Dados | Perfil de mais focado em realizar analise e validar hipóteses. Busca sempre identificar oportunidades nos dados, mais orientado ao negócio, entende o que está acontecendo através de análises descritivas, prescritivas. Faz a modelagem semântica e aplica regas de negócio para enriquecer os dados | Perfil mais orientado ao desenvolvimento. Possui forte conhecimento em programação, utiliza dados em um estado mais bruto, sem muitas transformações que afetem o estado original. Busca validar hipóteses, trabalha com modelos estatísticos e frameworks de machine learning supervisionados de classificação, clusters e recomendações. | Profissional com conhecimentos avançados de estatística e modelos não supervisionados como de NLP, visão computacional. Conhecem algorítimos avançados de redes neurais e deep learning.

<br>
Olhando de fora, podemos ver a plataforma de dados como hub que conecta os diversos tipos de fontes, aos desenvolvedores e consumidores de dados (egenheiros, analistas de negócio, analistas de BI, cientistas de dados). É através da colaboração entre eles que o ciclo de vida dos dados acontece e o valor é obtido através do uso de dados.

![Alt text](../media/produtor-consumidor.png)



# Pipelines de dados
Os pipelines de dados representam todo esse processo de transformação de dados em informação. Eles combinam os elementos da arquitetura de dados (storages, engines, bibliocas) e processos para mover e transformar os dados entre as fases so ciclo de vida. Um pipeline de dados é o sequenciamento lógico das etapas de transformação, respeitando suas dependências e restrições. 

O termo pipeline também é usado na área de tecnologia em diferentes contextos. Por exemplo:

### Pipeline Devops:  
Esse tipo de pipeline está relacionado com o processo de desenvolvimento de software e busca a através da automação do processod e compilação, teste, implantação garantir a qualidade do software e a entrega em produção de forma mais tranquila e controlada.

### Pipeline Machine Learning
Já um pipeline de machine learning está mais relacionado com o pipeline de dados, mas vai além. As primeiras fases são iguais (coleta, limpeza, preparação e transformação de dados brutos) com o objetivo de obter um formato adequado para treinar um modelo estatístico. Além disso, ele também automatiza o treinamento do modelo a validação e a implantação do modelo em produção como produto acessível por uma API, por exemplo. 


## Como cada profissional atua no desenvolvimento do pipeline
Função | Atividades | Tecnologias envolvidas
------ | ---------- | -----------------------
Engenheiro de dado | Perfil mais técnico, focado no processo de ingestão de dados (extract e load) e desenvolvimento do pipeline | SQL, Python, Data Warehouse, Data Lake, Spark, Containers, etc..
Analista de Dados | Consumidor indireto do pipeline, produz análises com ferramentas de  BI avançada e faz a modelagem OLAP para atender requisitos de negócio | SQL, modelagem de dados, storytelling, estatística, conhecimento da área de negócio
Analista de Negócio | Apoia na fase de exploração de dados e modelagem semântica. Consome os relatório e dashboards com dados gerados pelo pipeline. Fazer querys ad-hoc e produz dashboards customizados | Conhecimento da área de negócio e ferramentas de visualização de dados
Cientista de dados/ML | Utiliza os dados brutos gerados nas primeiras fases do pipeline para validar hipóteses e gerar modelos preditivos que podem ser utilizados como parte do eriquecimento dos dados no pipeline. | Python, SQL, R, Estatística, Framework de Machine Learning


## Orquestração
A orquestração é o processo de execução das fazes do pipeline e envolve o acionamento, agendamento e monitoramento das várias tecnologias envolvidas no processo. Existem plataformas específicas para execução destes pipelines, todas elas se caracterizam por terem uma vasta lista de conectores. Um coisa importante buscar manter a separação das responsabilidades ao usar uma plataforma de orquestração. Apesar de muitas vezes ela ser capaz de fazer a ingestão e processamento de dados, ela deve ser usada apenas para acionar e controlar a execução.

### Exemplo: 
A solução de orquestração inicia a execução no dia e horário agendado. Na primeira etapa ela fica escutando uma pasta do datalake esperando a aplicação enviar dados novos, quando detecta a presença de um arquivo na pasta "landing" ela passa para a etapa que executa um código PySpark que roda no cluster Spark que lê os dados e fazer o processamento e salva de volta em outra pasta do datalake. Quando termina o orquestrador aciona a próxima etapa que executa um procedure em um banco SQL que cria uma tabela virtual que abstrai o arquivo salvo na etapa anterior, se a tabela for criada com sucesso o orquestrador aciona uma nota procedure que lê os dados da tabela virtual e insere os dados em um data warehouse. Quando essas etapas estiverem prontas o orquestrador fazer uma requisição para o endpoint do serviça na nuvem responsável por disparar o atualização do modelo semântico comos novos dados. Quando tudo tiver pronto envia uma mensgem para o teams informando que o processo acadou. Veja, o orquestrador acionou, um datalake, um cluste spark, um data warehouse, uma api, um webhook, mas não processou um dado sequer.

