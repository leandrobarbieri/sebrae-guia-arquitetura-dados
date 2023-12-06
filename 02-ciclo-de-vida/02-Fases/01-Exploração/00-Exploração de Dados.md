# Fase: Exploração de dados
Essa é a primeira fase do ciclo de vida, é a fase que antecede a construção do pipeline de dados, nesse momento são sendo avaliadas as possibilidades de obtenção dos dados, as fontes disponíveis e os dados necessários.

É uma fase muito importante pois busca identificar as fontes originas dos dados disponíveis que são realmente necessários. Se preocupa principalmente em mapear os dados e não gerar duplicidade no processo de ingestão e a cadência que são gerados e que podem ser lidos.
 
Essa uma fase que requer conhecimento técnico em múltiplas tecnologias de bancos de dados além de conhecimento de regras de negócio. A execução dessa etapa do ciclo é realizada por engenheiros de dados em conjunto com analistas de negócio e se caracteriza pela entrega de uma análise de viabilidade, que vai explicitar as características dos dados como formatos, volumes e variedade.

Durante a exploração, faça analises descritivas, avalie as distribuições das variáveis numéricas, veja os tipos de atributos categóricos e o nível de qualidade dos dados na fonte. Para lidar com questões como diferentes contas de acesso a base de dados ou API, disponibilidade de drivers e conectores e diferentes tipos de tecnologias de armazenamento de dados, utilize ferramentas de virtualização de dados para simplificar o ambiente. A virtualização de dados podem ajudar a padronizar a linguagem utilizada para obter os dados, além de abstrair os diferentes formatos das fontes de dados de origem.


### SQL, Python, R ou Bash?
Ao iniciar a fase de exploração surge a questão, qual liguagem utilizar? Dependendo do momento e do desafio técnico nessa fase, pode ser mais indicada uma linguagem específica. Cada caso de uso vai ajudar a determinar. Por exemplo: podemos recomendar SQL para realizar transformações e modelagem; Python  para realizar a extração dos dados de formatos e de fontes diferentes, ou para fazer requisições a APIs de aplicações e lidar com dados em json; podemos usar bash para automatizar tarefas de implantação, interagir com o sistema de arquivos ou S.O e realizar configurações de ambiente.


### Entradas
Relações de dependência externas como regras de firewall, drivers de conexão, usuários, senhas tokens

### Saídas
Scritps com querys que descrevem os dados explorados, notebooks com análises de distribuição das variáveis numéricas e categóricas, gráficos das pricipais entidades, análise de percentual de valores nulos, avaliação dos outliers.

### Limites
 Essa fase se limita a validar a disponibilidade das fontes e gerar uma lista de entidades e atributos disponíveis. Não são feitas manipulações, cargas ou qualquer movimentação de dados.
 
### Responsabilidades
 Engenheiros de dados em cojunto com analistas de negócio e desenvolvedores de software.
  
### Tipos de tecnologias
SQL clients, Jupyter notebooks ou VSCode.


### Continuar ...

> trazer exemplos de codigo para leitura de tipos diferentes, fontes diferentes, conversão de formatos; Webscapping, api, csv, json, delta

