# Lista de recomendações de melhores práticas de modelagem

Código | Recomendação | Descrição | Princípios
------ | ------------ | --------- | ----------
R01-Modelagem | Os dados da camada de modelagem devem estar organizados com base nos domínios da informação e não mais pelos contextos das fontes de dados. | Como os dados estão sendo preparados para atenderem as necessidades do negócio, fontes de dados de sistemas diferentes podem ser agrupadas em um domínio único. | P05
R02-Modelagem | A modelagem deve esconder a maior parte da complexidade das fondes de dados originais | Toda a camanda semântica deve ser orientada ao consumo. Remover a normalização, simplicicar nomenclatura de atributos, mudar granularidade, criar métricas calculadas, etc.
R03-Modelagem | Os dados armazenados na camada de modelagem (gold) devem estar no mesmo storage e formatos de arquivos que as camadas anteriores.
R04-Modelagem | A camada de modelagem deve ser otimizada para consumo | As tecnologias de MDW, com particionamento, processamento distribuído, storages com discos rápidos (hot)
R05-Modelagem | Os recursos computacionais desta camada devem ser para escalar de forma independente dos recursos de storage, para acomodar o comumo massivo.
R06-Modelagem | Views materializadas podem ser criadas para simplificar o otimizar o consumo | Views ajudam a diminuir a complexidade e quando materializadas podem trazer performance. Usar apenas quando há a possibilidade de analisar a linhagem dos dados.
R07-Modelagem | Entenda como funciona o mecanismo de otimização de querys. Use as boas práticas como particionamento e compactação para extrair o melhor da tecnologia do banco dados, isso vai te ajudar a escrever querys mais eficientes e economizar tempo e dinheiro
R08-Modelagem | Faça o pré-processamento de algumas tabelas mais usadas em joins para otimizar as querys
R09-Modelagem | Crie tabelas desnormalizadas para consumo. Substituir join por tabelões podem ser muito mais performático para acesso ao dados para consumo.
R10-Modelagem | Desacoplar a camada semântica das ferramentas de BI (metric store) | Uso de ferramendas de BI diferentes com a mesma metrica, propagação de mudanças, melhor consistencia, confinça que todos estão usando a mesma logica dos indicadores, concistencia entre ferramentas de BI
