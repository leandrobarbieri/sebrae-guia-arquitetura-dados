# o que é
> Abordar aqui asrelações de dependência, entradas, saídas, limites, responsabilidades, tipos de tecnologias

> O que acontece nessa fase, qual o objetivo da fase. Delinear entradas, saídas limites e fronteiras

# porque
> ter uma camada de transformação específica. Qualidade dos dados, multiplos casos de uso (dados tratados mas não alterados com regras de negócio são ótimos para DS)

# Como?
> Como padronizar formatos diferentes e aplicar regras de validação, duplicidade e inconsistencias
Como lidar com mudança de schema; tipagem, limpeza, padronização, validação, ofuscação, qualidade, performance

# Tecnologias de qualidade de dados
dbt

## Processamento distribuído
, quando é necessário, como funciona, quais são os limites


## Linguagens de processamento
Definir qual engine vai interagir como o lakehouse, 
de dados SQL, Python, SparkSQL, quando usar, qual é mais indicada para cada perfil de usuário, ou fase no ciclo de vida

Tabela indicativo de linguagem/ tipo de tecnologia de transformação para cada perfil

Linguagem | Analista | Cientista | Engenheiro
-------| -------- | --------- | -----------
SQL | x | x | x
Python | - | x | x
R | - | x | x
PySpark | - | x | x
SparkSQL | x | x | -
Bash | - | - | -


## Exemplos códigos comuns
Listar os comandos mais comuns e as transformações básicas em cada linguagem

Código | SQL | Pandas | PySpark 
------- | --- | ------ | -------
Projeção de atributos de uma tabela | SELECT col1 FROM Tab | df["col1] | df.select(col(col1))
Selecionar todos os atributos da tabela | SELECT * FROM Tab | display(df) | df.show()
