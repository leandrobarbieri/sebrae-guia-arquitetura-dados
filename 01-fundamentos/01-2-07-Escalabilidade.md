# P07 - Escalabilidade
> _"Os componentes devem ser capazes de se adaptar a demanda de conexões, processamento e volumes de dados, aumentando ou diminuindo a quantidade de recursos alocados."_

Os componentes devem ter escalabilidade tanto para adaptar-se ao aumento de demanda quando para reduzir o uso dos recursos para gerar oportunidades de redução de custos quando possível. No mundo ideal a arquitetura deve ser elástica e se adaptar automaticamente à demanda, inclusive, quando possível desligando os recursos quando não estão sendo usados. Falhas ou pouca atenção a esse princício pode resultar em custos elevados para a sustentação da arquitetura.

A arquitetura deve permitir que a capacidade seja ajustada à demanda mantendo a performance mesmo que em casos de uso específicos o projeto de dados demande muitas conexões, volume de consultas ou quantidade de dados. 

Essa característica de elasticidade é o atributo que define sistemas que são capazes de fazer escalabilidade automática tanto para mais, quanto para menos. Essa característica é muito importante para garantir performance sem intervenção manual, aumentando assim robustez da solução. O objetivo é sempre a busca pela eficiência, atender a demanda com menor custo. 


#### Benefícios
Se a arquitetura não tem essa capacidade de escalonar ou de reduzir de acordo com a demanda, erros no dimensiomento de capacidade podem gerar custos excessivos em recursos subutilizados, ou quando escassos causar problemas de performance. Adotar componentes auto-escaláveis permite que apenas a quantidade necessária será provisionada, otimizando o uso dos recursos ao mesmo tempo que mantém a performance.