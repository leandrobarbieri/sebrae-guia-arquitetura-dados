## P01 - Separação das responsabilidades
Assim como na engenharia de software, a separação de responsabilidades em arquiteturas de dados traz muitos benefícios como: clareza no entendimento de como o processo funciona pois cada componente tem suas entradas e saídas bem definidas, simplifica a manutenção, aumenta confiabilidade pois os componentes têm escopo mais reduzido e são mais especializados, além permitir a substituição de um componente sem afetar a solução como um todo, apenas naquele escopo reduzido.

Por exemplo, engines de processamento de bancos relacionais tradicionais não separam claramente os componente que armazena os dados daquele que os processa, se tiver que escalar o banco precisa escalar a instância com um todo, se precisassemos reduzir os recursos para o processamento e aumentar apenas para o armazenamento do dados, não seria possível nessa arquitetura, um componente depende do outro e são escalados em conjunto. Em uma arquitetura moderna, com engine de processamento responsável apenas por processar e storage apenas por ler e escrever, você pode desativar um componente e continuar com o outro, você pode trocar ou usar outras ferramentas para processar os mesmos dados.

Esse é um exemplo seperação de responsabilidades relacionados a tecnologia. Esse princípio também está associado ao ciclo de vida dos dados. Cada fase possui seu escopo, uma responsabilidade, seus objetivos suas entradas e saídas, suas tarefas. Essas fronteiras simplificam o entendimento, e nos ajuda a identificar o que cada fase representa.

A clara separação de responsabilidades entre os elementos cria uma fronteira entre as fases do ciclo de vida dos dados de forma que também facilida o monitoramento e governança; 

É importante que tenha uma matriz de responsabilidades, com todas a decisões bem maepadas, evitando conflitos e "bolas divididas". Essa separação vai preparar a  arquitetura para alguns padroes de gestão, ISO (9000, 27001), alguns frameworks ITIL por exemplo e também já deixar construidos os pontos de controles para adequação a legislação LGPD, GDPR.

Sem responsabilidades divididas o resultado por ser catastrofico...
