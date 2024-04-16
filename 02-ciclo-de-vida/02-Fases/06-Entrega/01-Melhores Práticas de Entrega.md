
# Recomendações do guia
Código | Recomendação | Descrição
------ | ------------ | ---------
R01-Entrega | A empresa deve ter uma infraestrutura de dados sólida e madura antes de focar em iniciativas de ML | A produtividade de cientistas de dados depende da disponibilidade de dados, da qualidade, da capacidade de lidar com volumes grandes, da infraestrutura de orquestração de pipelines para produtizar os modelos estatísticos. Tudo isso depende de infraestrutura previamente estabelecida.
R02-Entrega | Exponha apenas os dados gerados pelas fontes originais | Caso haja sobreposição de fontes de dados, identifique a aplicação responsável pelo dado original, não gere sobreposições.
R03-Entrega | Evite criar dê-para na fase de entrega para contornar deficiências na modelagem | Qualquer dê-para que não possa ser feito usando os dados das fontes oficiais deve ser feito na camada de modelagem. Ao utilizar em um painel, dê transparência. Em geral, evite pois dê-para são fontes de dúvidas pois são difíceis de ser validados na fontes de dados originais.
R04-Entrega | Todos os dados expostos como produto devem ter um proprietário identificado | Saber quem é a pessoal que responde pela qualidade de um conjunto de dados adiciona valor, confiabilidade e contexto para quem consome.
R05-Entrega | Controle de acesso em níveis (workspace, tabela, coluna, linha) | Os dados devem ser expostos com diferentes níveis de acordo com a necessidade. Teve ser possível ter um controle mult-tenant de acesso.
R06-Modelagem | os consumidores nunca podem ter permissões para inserir ou alterar os dados | Os consumidores pode usar os dados alterados mas devem exportá-los para outros contexto. No caso de ETL reverso, onde uma aplicação consome dados analíticos como entreda, as mudanças estão fora do escopo da arquitetura.
R07-Entrega | Substitua os dados confidenciais por tokens e aplique máscaramento em tempo de execução [dynamic data masking](https://oreil.ly/sZ371)
R08-Entrega | Organize os ativos de dados um catálogo unificado orientado a domínios e permita que seja possível rastrear a linhagem dos dados até a origem, dando visibilidade de onde os dados estão vindo, quais outros conjuntos de dados foram usados para criá-lo, quem o criou e quando, quais transformações foram executadas. | Isso traz transparência, auxilia na descoberta e democratização dos dados e auxilia na solução de problemas e análise de impacto de mudanças.
R09-Entrega | Como gerenciar os acessos e compartilhamento de dados em um modelo descentralizado/federado? | Centralizar o controle de acesso: Mesmo que os dados estejam em arquiteturas separadas, em um modelo federado, busque usar padrões de armazenamento abertos de forma que seja possível criar catálogos com controle de acceso centralizado mantendo uma governança unificada.
R10-Entrega | Fornecer dados semanticamente consistentes para que os consumidores possam entender facilmente e combinar corretamente diferentes conjuntos de dados. Além disso, todos os dados devem ser facilmente descobertos e acessíveis aos consumidores por meio de um catálogo central com metadados e linhagem de dados devidamente selecionados.
R11-Entrega | Busque sempre criar experiências de autoatendimento para solicitação de acessos aos produtos de dados
R11-Entrega | Como ter controle de acesso completo a nível de objeto, tabela (linhas, colunas), views, procedures, funções, etc? | Usar na camada de entrega uma solução baseada na arquitetura de data warehouse moderno, com dados persistidos ou virtualizados. Dependendo da plataforma, Lakehouses podem não ter o nível de controle de acesso necessário para essa camada de entrega.


# Boas práticas

Adaptar o tipo de entrega a necessidade: Muitas vezes o que os analistas precisam são os dados e não mais um dashbord

Construção de dashboards: Não criar paineis com filtros implicitos. É importante sempre estar claro todos os filtros que estão dando contexto a um painel. Utilize textos para complementar as análises gráficas

Prototipação:  Uma técnica que pode ajudar é sempre prototipar no excel antes de criar dashboards. Com isso terá a real dimesão do que será necessário. E muitas vezes verá que não precisa de um dashboard, e sim apenas um tabela dinâmica ou apenas os microdados

Descoberta: todos os dados devem ser facilmente descobertos e acessíveis aos consumidores por meio de um catálogo central com metadados e linhagem de dados devidamente selecionados.


