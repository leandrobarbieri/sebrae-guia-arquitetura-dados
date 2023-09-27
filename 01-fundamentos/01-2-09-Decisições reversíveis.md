# P09 - Decisições reversíveis
> "_As escolhas podem ser revisadas e desfeitas, se que comprometa a continuidade do funcionamento, arquitetura deve ser capaz de absorver mudanças._"

Ao chegar a uma arquitetura viável, é importante que ela seja vista sempre como algo mutável, algo que está em constante evolução. 

Como as mudanças são previsíveis e a evolução das staks de dados é constante e até recomendável devido evolução técnica dos componentes, toda decisão arquitetural deve buscar a flexibilidade e poder ser revertida sempre que for necessário. A viabilidade disso é normalmente influenciada pelo grau de acoplamento entre os componentes. Esse é um princípio da engenharia de software que é muito importante nesse contexto de arquitetura de dados. 

#### Exemplo
Durante a aplicação de uma nova versão de um produto, ou testes de uma nova ferramenta, ser capaz de fazer pequenas mudanças e garantir que são reversíveis, permite que atualizações tecnológicas ou updates sejam feitos com mais regularidade em caso de falha não afetem os clientes.
