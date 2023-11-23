# Fase: Exploração de dados
Essa é a primeira fase do ciclo de vida, nesse momento são sendo avaliadas as possibilidades de obtenção dos dados, será avaliado o que é necessário e o que está disponível. É uma fase que requer conhecimento técnico e de negócio. É realizada por engenheiros de dados em conjunto com analistas de negócio.

Durante a exploração são feitas análises descritivas, distribuição das variáveis numéricas, avaliação dos tipos de atributos categóricos. Questões como contas de acesso, disponibilidade de drivers e conectores e diferentes tipos de tecnologias podem aumentar o grau de complexidade dessa fase. Nesse contexto ferramentas virtualização de dados podem ajudar a padrinizar a linguagem e abstrair os formatos das fontes de dados de origem.


### SQL, Python ou Bash?
Ao iniciar a exploração, qual linguem utilizar? Dependendo do momento e do desafio técnico nessa fase, pode ser mais indicada uma linguagem específica. Cada caso de uso vai ajudar a determinar. Por exemplo: podemos recomendar SQL para realizar transformações e modelagem; Python  para realizar a extração dos dados de formatos e de fontes diferentes, ou para fazer requisições a APIs de aplicações e lidar com dados em json; podemos usar bash para automatizar tarefas de implantação, interagir com o sistema de arquivos ou S.O e realizar configurações de ambiente.

Profissionais que dominam todas os componentes da arquitetura são difíceis de encontrar, cada pessoa envolvida pode ter mais proeficiencia em uma parte do ciclo de vida dos dados. O mais importante é identificar os tipos de atividades e os tipos de profissionais dentro da mesma função e equilibrar o time e cobrir todos os gaps de conhecimento.

Área de Conhecimento | Tipo 1 | Tipo 2 | Tipo 3
---------- | ------ | ------ | -------
Engenharia | Perfil mais técnico que mantém, gerencia e evolui a plataforma usando produtos gerenciados em ecosistemas de clouds públicas para criar data warehouse, pipelines de ingestão de dados servir analistas de dados, analistas de BI e machine learning | Perfil de engenheiros que constrõem soluções customizadas, escalavés, conhece muito infraestrutura como código, orquestração de containers. Se dedica a aprimorar e automatizar aplicações baseadas em dados. | Perfil de engenharia de dados voltado para desenvolver e implatar infraestrutura pra rodar modelos de ML em produção. Conhece práticas de Devops e o ciclo de vida de modelos (experimentação, treinamento, avaliação, implantação, re-treino) e frameworks de ML.
Cientista de Dados/Analista de Dados | Perfil de analise, busca identificar oportunidade nos dados, mais focado no negócio e orientado a entender o que está acontecendo através de análises descritivas, prescritiva. Faz a modelagem semântica e aplica regas de negócio para enriquecer os dados | Perfil mais orientado ao desenvolvimento com forte conhecimento em programação, utiliza dados em um estado mais bruto, sem muitas transformações que afetem o estado original. Busca validar hipóteses, trabalha com modelos estatísticos de frameworks de ML mais tradicionais supervisionados. Orientados a previsões e recomendações. | Profissional com conhecimentos avançados de estatística e modelos não supervisionados como de NLP, visão computacional que usam redes neurais.

A plataforma de dados pode ser vista com o hub que conecta os produtores (sistemas, dispositivos) aos consumidores de dados (engenheiros, analistas, cientistas) e viabilizar o ciclo de vida.

![Alt text](../../media/produtor-consumidor.png)


> O que?
> Abordar aqui asrelações de dependência, entradas, saídas, limites, responsabilidades, tipos de tecnologias

> Porque?
> descrever aqui as motivações de existir essa fase de exploração e porque é imporante;  importancia de identificar as fontes originas, não gerar duplicidade, os dados que realmente serão usados,  as caracteristicas deles para prever a tipagem e validações necessárias, os formatos etc,.

> Como?
> Entradas e saídas dessa fase; Exemplos com exemplo de codigo para leitura de tipos diferentes, fontes diferentes, conversão de formatos; Webscapping, api, csv, json, delta

Considerações importantes...
Entender a cadencia
Volumetri 
Tabelas
Tipos de fontes de dados
