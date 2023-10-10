## P01 - Separação das responsabilidades
>"_Cada componente possui um papel bem definido e especializado (sem sobreposições de funcionalidades)._"

Assim como na engenharia de software, a separação de responsabilidades em arquiteturas de dados traz benefícios como:

1. **Clareza no entendimento** de como o processo funciona, pois cada componente tem suas entradas e saídas bem definidas.
2. **Simplificação da manutenção** pois as configurações possuem um escopo reduzido e mais bem definido.
3. **Aumento da confiabilidade**, pois as soluções são mais especializadas.
4. **Modularização**, que permite a substituição de um componente sem afetar a solução como um todo, afetando apenas uma parte.

Esses benefícios são fundamentais para o desenvolvimento de sistemas robustos e escaláveis. A separação de responsabilidades ajuda a evitar a complexidade desnecessária e facilita a compreensão, toda a arquitetura mais e fácil de manter.

Em bancos de dados tradicionais, não há uma separação clara entre os componentes que armazenam os dados e aqueles que os processam. Isso significa que, quando precisamos escalar os recursos do banco apenas para processar, temos que escalar a instância inteira. Se precisássemos reduzir os recursos para o processamento e aumentar apenas o armazenamento dos dados, não seria possível nessa arquitetura, pois um componente depende do outro e são escalados em conjunto.

Além disso, quando não há separação entre engine e storage, a única forma de acessar os dados é passando pelo engine exclusivo de processamento do banco. Em uma arquitetura moderna, o engine de processamento fica responsável apenas por processar e o storage apenas por persistir e acessar. Dessa forma, você pode usar diferentes engines, pode inclusive desativar a engine e continuar com o storage ativado. Com isso, surge a possibilidade de usar diversas ferramentas para processar os mesmos dados, pois os dados existem de forma independente do engine de banco de dados.

Esse é um exemplo de separação de responsabilidades relacionada à tecnologia. Esse princípio também está associado ao ciclo de vida dos dados. Cada fase possui seu escopo, responsabilidades, objetivos, entradas e saídas. Essas fronteiras que separam as responsabilidades das fases simplificam o entendimento e nos ajudam a identificar o que cada fase representa e precisa fazer para ser concluída.

A clara separação de responsabilidades entre os elementos cria uma fronteira entre as fases do ciclo de vida dos dados, facilitando o monitoramento e a governança. Essa separação também nos permite criar uma matriz de responsabilidades, com grupos de atribuições e controles de acesso, evitando conflitos e "bolas divididas". Essas fronteiras bem definidas abrem espaço e preparam a arquitetura para o uso de padrões de gestão, como ISO (9000, 27001), e frameworks como ITIL por exemplo.