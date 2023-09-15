
# 04 - Independência de formatos de dados
O uso de formatos abertos facilita o acesso aos dados a partir de multiplas ferramentas e permite atender casos de uso diferentes. Buscar padrões de mercado como json, csv, txt, parquet (delta, hudi, iceberg) com um ecosistema de ferramentas de analise de dados, bibliotecas de linguagens de programação, engines de processamento e frameworks de machine learning dá a liberdade suficiente para todos usarem os dados independentemente do perfil. 

### Exemplo
Utilizar diversos tipos de fomatos abre espaço para os tipos são estruturados. Por exemplo, o dado é armazenado em um object storage (que aceita qualquer formato) de um lakehouse, depois é transformado, enriquecido e usado em varios contextos diferentes, desde vídeos, imagens a texto semi-estruturado.

### Benefícios
Utilizar formatos abertos simplifica a infraestrutura de tipos de conectores necessários para obter os dados, também amplia as possibilidades de como usar sem criar uma dependência de um fabricante. O mesmo dado em parquet que o analista de dados faz a query criando suas regras de negócio pode ser o dados que o cientista de dados usa para treinar seu modelo usando um framework de ml.  

 



Ideias interessantes
https://www.youtube.com/watch?v=yCQTOHDOfJw&t=13s