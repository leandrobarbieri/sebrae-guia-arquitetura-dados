# Introdução
> _Momento da área de engenharia de dados, a mudança de paradigma do que é bigdata hoje e que será amanhã; a importância crescente em tomar decisões baseadas em dados; a necessidade de direcionamento para acompanhar o ritmo das mudanças._

O guia se busca a trazer um detalhahmento das melhores práticas estabelecidas, estratégias de implantação e recomendações técnicas agnósticas e multicloud, sempre com o propósito de encontrar o que melhor se adequa ao modelo federado, com a independência das unidades mas com governança centralizada.


### mostrar a evolução do landscape (imgs)
> Historico e landscape 
https://airbyte.com/blog/data-engineering-past-present-and-future

Atualmente a diversidade de fontes de dados, a disponibilidade de informações e o volume disponíveis são um grande desafio mas também uma grande oportunidade, os benefícios uma arquitetura capaz de se adaptar às necessidades de anáslise de dados, alinhada aos padrões de mercado irão dar a solidez necessária para extrair valor 

Projetar uma arquitetura de dados envolve definir os elementos necessário, as interfaces, as entradas e saídas para fazer com que o dados sejam transformados em informação em um ciclo de vida.

As decisões e as escolhas devem ser reversíveis, não depender de um fabricante, modelo ou produto. A robustez da arqutetura também está associada a capacidade de se adaptar, tecnologias que hoje são estado da arte logo podem estar defasadas, ou a maturidade de dados no futuro pode levar a casos de uso não mapeados que demandarão a evolução e mudanças.


# Objetivos Guia

Delinear os objetivos do guia, conceitos e princípios de arquitetura e engenharia.

> _Objetivos e Escopo do Guia: Uma declaração clara dos objetivos do guia e quais tópicos ele abordara. Definir o público-alvo e os usuários esperados também é útil._
- Alinhar os conceitos entre os colaboradores envolvidos
- Disseminar o conhecimento
- Estabelecer princípios que direcionam as abordagens para evolução de plataformas de dados
- Etc...

"Incluir aqui a nossa definição de arquitetura de dados"

O que faz uma arquitetura ser considerada boa?
-

# Estrutura do Guia
O guia é composto com quatro partes principais

### Parte I
Descrever os fundamentos necessários para endender os conceitos e princípios envolvidos no ciclo de vida dos dados. Descrever o que é  arquitetura e os padrões de mercado. O capitulo 1 e 2, traz uma uma visão geral da área de engenharia, do ciclo de vida dos dados e os princípios importantes para o Sebrae.

### Parte II
A parte II detalha cada fase do ciclo de vida com a descrição do propósito, as entradas e saídas e as fronteiras. Também serão apresentados exemplo do que fazer e comparativos de abordagens e tipos de tecnologia.

### Parte III
Na parte III são apresentados métodos para estruturação e storage "medallion", são apresentados os benefícios e vantagens das arquiteturas de data warehouse, data lake, lakehouse e data mesh. Além disso serão apresentados comparativos e recomendações de quando usar.

### Parte V
Nesta V parte vamos falar sobre tópicos relacionados a governaça e como  boas práticas de segurança, metadados e catálogo, versionmento de código em projetos de dados, gerenciamento de riscos. 


# Objetivos
Descrever os componentes mais comuns e as melhores práticas associadas de forma que seja possível compartilhar com na organização recomendações para a construção de uma arquitetura de dados moderna, além de ser um meio de disseminar o conhecimento entre os times envolvidos em atividades de engenharia de dados.

Entre os componentes mais comuns que serão explorados com mais detalhes estão: object storages, sistemas de orquestração, engines de processamento, controle de versão, entre outros. Além disso, a liderança em projetos de arquitetura de dados é um fator importante de sucesso. Profissionais com uma liderança forte, aliada a capacidade técnica são difícies de encontrar mais sçao valiosos para a formação de uma equipe. É importante que a liderança compartilhe as decisões sobre a arquitetura e que não crie viéses baseados em escolhas individuais, a equipe deve ter a liberdade chegar ao concenso nas decisões. Essa dinâmica colaborativa de compartilhadas evita que seja escolhida uma plataforma única, proprietária e que os demais sejam forçados a se adaptarem a ela.

Ao chegar a uma arquitetura viável, é importante que ela seja vista sempre como algo mutável, em constante evolução. Ter uma visão clara de onde está e planejar constantemente a arquitetura deve ser um objetivo permanente.

O guia irá levar no caminho de uma definição da arquitetura atual mas também de como definir os princípios para o planejamento da evolução com uma visão de futuro

