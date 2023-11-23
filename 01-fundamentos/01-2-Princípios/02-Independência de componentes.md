## P02 - Idenpendência de componentes
> "_Os componentes podem ser substituídos, escalonados ou desativados de forma isolada sem comprometer o funcionamento da plataforma._"

A independência entre os componentes, principalmente entre a camada de storage e as engines de processamento (separação entre armazenamento e computação) é um princípio que traz benefícios como redução de custos, escalabilidade e flexibilidade para mudanças. Esse princício está presente nas stack de dados modernas e vem sendo o grande diferencial em comparação a modelos antigos baseados em data warehouse tradicionais.

Além da independência entre o storage e as engines de processamento presente nos data warehouses/lakehouses, temos a idenpendência entre tecnologias de armazenamento de dados OLAP, que criam a camanda semântica para diferentes ferramentas de análise de BI que consomem. 

![Camadas](/01-Fundamentos/media/image-1.png)

#### Exemplo
Nas arquiteturas de Lakehouse e Data Warehouses modernos, como Azure Synapse, BigQuery, Databricks, o storage é desacoplado da computação. Na prática o engine de processamento roda em clusters diferentes, dessa forma a arquiterura fica escalável e suporta muito mais usuários concorrentes ou volumes de dados maiores, se adatando ao caso de uso e tipo de demanda. Esse é um exemplo de como o o desacoplamento traz versatilidade. 

Outro exemplo é quando a camada OLAP (semântica) está definida de forma independente das ferramentas de visualização. Quando uma métricas é usada a mesma representação e significado é aplicado em todas as visualizações, independentemente da ferramenta de BI usada.

#### Benefícios

1. **Dimensionamento de forma independente em momentos distintos**: Ao fazer um treinamento de um modelo de machine learning que demanda muito processamento pra calcular as matrizes, você pode aumentar a quantidade de nós de processamento e manter a mesma quantidade e recursos no storage, ou ao executar um pipeline de dados para fazer uma ingestão massiva em batch, você pode aumentar os recursos do object storage enquanto mantém o cluster de processamento com os mesmos recursos já que a ingestão demandará menos transformações.

2. **Ser substituídos conforme a convenência**: Em uma determinada situação, a empresa decide mudar a ferramenta de orquestração, se os dados estão armazenados fora da ferramenta, se o processamento é feito por uma engine independente e os scripts com as regras de negócio estão versionados em um repositório, a troca de um orquestrador pode ser feita sem comprometer a arquitetura.

3. **Evoluir a medida que novas tecnologias surgem:** É semelhante ao exemplo acima. A substituição, ou as atualizações podem ser feitas sem compromenter ou afetar outros componentes, pois estão isolados e com interfaces bem definidas.

4. **Problemas ficam isolados**: Se por exemplo, o data warehouse está com um problema de performace, os usuários que consomem o modelo semântico (cubo olap) não são afetados.

5. **A arquitetura seja mais simples de ser entendida**: Apenas as partes que interessam a cada perfil são disponibilizadas, por exemplo. O usuário de negócio não precisa ter que lidar com o formato, o espaço em disco, pipeline de transformação.

6. **Permite "espalhar" a arquitetura em pequenos componentes mais gerenciaveis**: Se acontecer um problema em um componete com muitas features como um banco de dados relacional tradicional, a causa pode ser storage, processamento, formato, índice, controle de acesso, códigos (trigger, procedures, views). São muitas frentes de trabalho para identificar e corrigir. Agora se der problema em uma DAG do orquestrador você sabe exatamente qual componente falhou, pois são independes.
