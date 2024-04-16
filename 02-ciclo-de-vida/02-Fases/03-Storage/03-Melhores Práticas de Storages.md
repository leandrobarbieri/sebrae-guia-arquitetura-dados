# Lista de recomendações de melhores práticas para storages

Código | Questão | Recomendação | Princípio
------ | --------- | --------- | ---------
R01-Storage | Como armazenar de forma correta dados em bases de relacionais? | Não armazenar dados semi-estruturados em base relacional e garantir que todas as tabelas com dados analíticos estejam armazenados como column-store | P6
R02-Storage | Como garantir que os dados possam ser acessados por diversos compomentes de processamento e análise de dados? | os dados não devem estar em formato proprietario, exclusivo do produto do storage (devem estar em formato aberto, comum a maioria das ferramentas). 
R03-Storage | Como gerenciar o storage para não perder a governança? | Use valores exclusivos nos dados para criar hierarquias de pastas. Particione os dados com base em critérios como data, região ou tipo. Isso facilita a recuperação e o processamento seletivo dos dados. Dê nomes descritivos às pastas para que sua função seja clara. Evite abreviações confusas ou códigos não intuitivos. Estabeleça padrões de nomenclatura para consistência. Por exemplo, use “ano-mês-dia” para pastas de dados diários. Defina permissões adequadas para pastas e arquivos. Garanta que apenas usuários autorizados tenham acesso. Mantenha documentação sobre a estrutura das pastas. Descreva o conteúdo de cada pasta e sua finalidade. Monitore o uso das pastas regularmente. Remova dados obsoletos ou desnecessários para evitar acúmulo. 
R04-Storage | Qual tipo de storage usar? | Usar object storage com padrões abertos que garantam performance e facilidade para o compartilhamento com segurança. | P10-Simplicidade, P08-Descentralização, P09-Multicloud
R05-Storage | Como libdar com a segurança de dados sensíveis? | Logo na camada Bronze/Raw, os dados seinsíveis devem ser encriptados ou mascarados. Utize mascaramento sempre que tiver a previsão usar os dados sem mascaramento por algum grupo de usuários com permissão.
R06-Storage | Como evitar mover grandes quantidades de dados entre unidades e parceiros? | Use os recursos de data sharing para "montar" os conjuntos de dados externos ou internos que já serão compartilhados. Isso aumenta a confiabilidade, reduz a redundância e traz qualidade. | P06-Multicloud, P08-Descentralização,  P10-Simplicidade
R07-Storage | Como controlar o aumento do espaço de armazenamento do object storage? | Utilizar políticas para remoção automática de versões de arquivos mais antigos ou que já tem várias versões armazenadas |
R08-Storage | Como reduzir o custo de storage? | Utilize os recursos das ferramentas de gestão de ciclo de vida dos object storages para criar políticas automatizadas para armazenar dados antigos ou pouco acessados em categorias de persistências com discos com melhor custo benefício.


### Dicas de como gerenciar o storage para não perder a governança?
- Use valores exclusivos nos dados para criar hierarquias de pastas. 
- Particione os dados com base em critérios como data, região ou tipo. Isso facilita a recuperação e o processamento seletivo dos dados. 
- Dê nomes descritivos às pastas para que sua função seja clara. Evite abreviações confusas ou códigos não intuitivos. 
- Estabeleça padrões de nomenclatura para consistência. Por exemplo, use “ano-mês-dia” para pastas de dados diários. Defina permissões adequadas para pastas e arquivos. Garanta que apenas usuários autorizados tenham acesso. 
- Mantenha documentação sobre a estrutura das pastas. Descreva o conteúdo de cada pasta e sua finalidade. 
- Monitore o uso das pastas regularmente. Remova dados obsoletos ou desnecessários para evitar acúmulo. 


# Anotações
- usar parquet na bronze por ser mais generalista e delta ou iceberg na silver e gold
- colocar pk e foreign key no começo da tabela
- não armazenar dados semi-estruturados em base relacionalç
- antes de armazenar fazer a compressao do arquivo para reduzir o tamanho e economizar

ex func de compressao para testar o melhor formato 

> def salvando_arquivo_comprimido_json(dataframe):
    compressoes = ["none", "bzip2", "gzip", "lz4", "snappy", "deflate"]
    caminho_padrao = "/FileStore/tables/PNSB_json_"

    for tipo_compressao in compressoes:
        dataframe.write \
            .option("compression", tipo_compressao) \
            .mode("overwrite").format("json") \
            .save(caminho_padrao + tipo_compressao)
        
        display(dbutils.fs.ls(caminho_padrao + tipo_compressao))

salvando_arquivo_comprimido_json(df)
