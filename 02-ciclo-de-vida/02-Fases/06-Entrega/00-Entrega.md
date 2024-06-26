# Fase: Entrega
Essa é a fase final do pipeline de dados, é o momento em que o dado está "pronto" para análise. O mais importante aqui é que os produtos de dados atendam às diferentes necessidades dos usuários e tenham como principal característica a qualidade. Além disso, devemos garantir que o que é entregue seja reutilizável e atenda a vários casos de uso e que a empresa pode confiar.

Produzir dados como produto de alta qualidade é o objetivo principal de qualquer plataforma de dados, portanto essa fase é o final dessa processo de transformação de dados em produto. 

A ideia é que as equipes data engineering apliquem o pensamento do produto aos dados selecionados: os ativos de dados são seus produtos, e o cientista de dados, engenheiros de ML e BI ou quaisquer outras equipes de negócios que consomem dados são seus clientes. Esses clientes devem ser capazes de descobrir, abordar e criar valor a partir desses dados-como-produtos por meio de uma experiência de autoatendimento sem a intervenção das equipes de dados especializadas.

Publique produtos de dados semanticamente consistentes em toda a empresa
Um data lake geralmente contém dados de diferentes sistemas de origem. Às vezes, esses sistemas nomeiam o mesmo conceito de maneira diferente (como cliente x account) ou significam conceitos diferentes pelo mesmo identificador. Para que os usuários de negócios combinem facilmente esses conjuntos de dados de maneira significativa, os dados devem ser homogêneos em todas as fontes para serem semanticamente consistentes. Além disso, para que alguns dados sejam valiosos para análise, as regras internas de negócios devem ser aplicadas corretamente, como o reconhecimento de receita. Para garantir que todos os usuários estejam usando os dados interpretados corretamente,


Nem só de dashboard vide a análise de dados, o analista de dados pode e deve ir muito além de criar gráficos, ele deve contar histórias, contextualizar, identificar correlações, fazer análise de impacto. 

Pode utilizar modelos treinandos ou treinar seu próprios modelos. É importante a arquitetura estar preparada para se integrar com soluções de gestão de modelos como mlflow que gerencia os experimentos e registro dos modelos de forma que o analista possa usar como parte dos scritps sql, usando um conjunto de colunas para submentar a inferencia de um modelo.


# Virtualização de dados e conceito de serverless

A virtualização traz benefícios como não precisar mover os dados, principalmente em uma arquitetura mesh baseada em domínios, centralizar o acesso aos dados em um unico ponto (oquestrador não precisa ter acesso a todas as fontes, apenas a maquina que virtualiza). Esse componente se apresenta como uma ótima solução para empresas que armazenam dados em vários tipos de bancos de dados. Apesar de ser uma solução que facilita o acesso e consumo, ela não resolve o problema do isolamente e concorrência. As querys realizadas por esse tipo de tecnologia são processadas pelo sistema de origem, muitas vezes impactanto a fonte cada vez que as querys são executadas.

#### Benefícios
- Integração de bases de dados: as mesmas querys em SQL são executadas  em Oracle, MongoDB, S3 Object storages.

- Virtualiza a origem: permitindo o acesso indireto à fonte sem ter que configurar drivers, conectores, regras no client.

- Simplifica as consultas: Padroniza a linguagem de consulta, independentemente da fonte as querys são SQLm padrão

- Redução de replicação: Acesso aos mesmos dados sem necessidade de importar/duplicar para a engine de processamento

Storage unificado de dados agrupados por domínios

![Alt text](../../media/image-2.png)



# Tipos de entrega

Podemos classificar os tipos de entrega para os usuários de acordo com o grau de flexibilidade. Entregas em que os dados estão mais preparados, onde foram manipulados para obter a visão específica atender um caso de uso específo são classificadas como menos flexível porém mais prontos para consumo (menor esforço e necessidade de manipulação). Já os produtos que são entregues com alto grau de flexibilidade, podem ser usados com um propósito mais geral, podem atender a mais casos de uso (análise descritiva, prescritiva, preditiva) porém demandam mais esforço e preparação para resolver o problema. É como a **analogia** de um foodtruck versus um restaurante. No foodtruck os ingredientes (dados) estão pré-processados, e são contidos nas poucas possibilidades de preparação pré-planejadas. Já em um restaurante os ingredientes estão em seu estado mais bruto, há disponibilidade de realizar combinações não planejadas, que podem vir de um pedido de um cliente.


![Alt text](../../media/tipos-de-entrega.png)


# Importância de um catálogo de dados

- Descoberta de onde os dados estão e  quais os assuntos
- Fonte rica de metadados que auxiliam a definição de contexto


# Casos de Uso

Caso de uso | Siver | Gold | DW | Cubo | Painel/Infográfico | Obs
------------| ----- | ---- | -- | ---- | ------ | ---
Investigação de hipótese e correlação | ✔️ | ✔️ | ✔️ | ✔️ | - | Esse caso de uso exige flexibilidade e as necessidades e possibilidades de exploração não estão previamente estabelecidas
Desenvolvimento de modelo estatísco | ✔️ | ✔️ | - | - | - | Os modelos estatísticos utilizam dados brutos, e a manipulação envolve transforma-los e números
Análise ad-hoc | - | - | ✔️ | ✔️ | - | Dados modelados ideal para consultas SQL e storytelling com ferramentas de vizualização
Acompanhamento de indicadores | - | - | - | - | ✔️ | São dados previamente mapeados e com os padrões de análise amplamente conhecidos e estáveis. Geralmente não mudam com frequência


# Storytelling


# Resumo

Pergunda | Exploração | Ingestão | Storage | Transformação | Modelagem | Entrega
---------- | -------- | ------- | ------------- | --------- | ------- | --------
O que acontece em cada fase? | Identifica as fontes, entende o significado | Move os dados das fonte de origem para o storage analítico | Armazena os dados (ler e escrever arquivos) | Adiciona qualidade e padronização para as tabelas | Cria regras de negócio e as entidades de domínio de acordo com a necessidade de análise | - 
Qual tipo de tec. usar? | Drivers, conectores, APIs, libs, SDKs | Ferramentas de orquestração | - | - | - | -
Qual perfil de profissional? | - | - | - | - | - | -
Entradas | - | - | - | - | - | -
Saídas | - | - | - | - | - | -