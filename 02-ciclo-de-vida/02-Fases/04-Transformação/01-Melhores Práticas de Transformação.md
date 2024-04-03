
# Lista de recomendações de melhores práticas de transformação

Código | Recomendação | Descrição | Princípios
------ | ------------ | --------- | ----------
R01-Transformações | Não devem ser incluídas regras de negócio na fase de transformação. Essa fase deve se concentrar em entregar valor através da validação, checagem, otimização e preparação dos dados. | Gerar datsets validados e com alta qualidade mas sem alterações de regras de negócio, os mantém com um propósito geram, servindo para múltiplos contextos e casos de uso onde a inclusão de regras de negócio poderiam limitar.
R02-Transformação | Os dados devem ser ter padrões de representação consistentes entre os conjuntos de dados. | Por exemplo, todas as tabelas que usar campos como: endereço, um telefone, representação de gênero, número de cpf/cnpj, um código de contrata, etc. devem armazená-los transformados da mesma forma.
R03-Transformação | As tecnologias usadas para o processamento devem ser escaláveis para conseguir lidar operações complexas de transformação ou limpeza.
R04-Transformação | Problemas com a qualidade dos dados devem sempre ser endereçados para serem corrigidos no sistema de origem
R05-Transformação | Dever ser estabelecido limites para a qualidade dos dados, quando é detectada que a qualidade está abaixo desses limites, deve haver uma análise por parte do proprietários dos dados se aceitam ou não a inclusão de dados com baixa qualidade.
R06-Transformação | Evite realizar operações full scan (select *) | Esse tipo de leitura faz o scan da tabela inteira, retornando todas as linhas e todas as colunas isso é ineficiente, não aproveita as features de particionamento e caso esteja sendo processado em um serviço de cloud terá custos extras desnecessários.
R07-Transformação | Use CTEs (common table expression) ao invés de subquerys ou tabelas temporárias
R08-Transformação |  Não armazenar dados semi-estruturados em base relacional
R09-Transformação | Como regra geral, para acesso a dados sempre selecione as colunas necessárias e aplique filtros ao rodar uma consulta.
R10-Tranformação | Quanto uma tabela em um Lakehouse é muito grande use sempre estratégias de particionamento para reduzir a quantidade arquivos que são carregados e persistidos. 