# Projeto de Tagueamento Automatizado na AWS

## Objetivo
O objetivo deste projeto é automatizar o provisionamento de recursos na AWS, garantindo que todos os recursos estejam corretamente **tagueados** para permitir o controle financeiro detalhado e a governança eficaz. Com um orçamento anual de **US$ 10.000**, o projeto implementa **guardrails** (limitações de segurança) que asseguram conformidade com as melhores práticas de segurança e governança, utilizando uma abordagem automatizada de monitoramento e gestão.

## Guardrails Implementados

### 1. **Validação de Tags em Tempo de Criação**
**Descrição**: Este guardrail impede a criação de recursos sem as tags obrigatórias, garantindo que toda a infraestrutura esteja em conformidade desde o início.  
**Como Funciona**: Uma função **AWS Lambda** é acionada via **AWS CloudFormation** ou **AWS Service Catalog** no momento em que os recursos estão sendo provisionados. Essa função valida se as tags exigidas, como "Ambiente", "Centro de Custo", "Proprietário" e "Projeto", foram corretamente atribuídas. Caso qualquer uma esteja faltando, a criação do recurso é bloqueada. Esse mecanismo evita a criação de recursos não rastreados, garantindo maior visibilidade e controle sobre o uso da infraestrutura.

### 2. **Orçamento e Limite de Gastos**
**Descrição**: Este guardrail define um controle proativo sobre o orçamento, alertando antes que os limites sejam ultrapassados e mantendo os custos dentro do orçamento anual de **US$ 10.000**.  
**Como Funciona**: Utilizando o **AWS Budgets**, são configurados alertas que monitoram os gastos em tempo real. Limites financeiros, como 80% e 90% do orçamento, são definidos para disparar notificações via **SNS** (Simple Notification Service) para as equipes responsáveis. Esse mecanismo permite ajustes ou ações corretivas antes que o orçamento seja excedido, ajudando na prevenção de gastos excessivos.

### 3. **Auditoria de Recursos Tagueados**
**Descrição**: Este guardrail assegura a conformidade contínua com as políticas de tagueamento.  
**Como Funciona**: Uma função **Lambda** é programada para executar auditorias periódicas utilizando o **AWS Config**, garantindo que os recursos mantenham as tags obrigatórias ao longo de seu ciclo de vida. Recursos que não estejam em conformidade são sinalizados, e relatórios são gerados automaticamente para alertar a equipe sobre a necessidade de correção.

### 4. **Regras de Compliance**
**Descrição**: Assegura que todos os recursos provisionados estejam de acordo com as políticas de segurança e governança da organização.  
**Como Funciona**: O **AWS Config** é configurado para monitorar as configurações dos recursos e verificar conformidade com as regras pré-estabelecidas de compliance, como controle de permissões, criptografia de dados em repouso, e configurações de rede. Quando um recurso não está em conformidade, o AWS Config gera alertas e pode acionar remediação automática via **AWS Systems Manager** ou notificações para os administradores.

### 5. **Controle de Acesso e Permissões**
**Descrição**: Garante que somente usuários autorizados possam realizar ações críticas, mitigando riscos de acesso não autorizado.  
**Como Funciona**: O **AWS Identity and Access Management (IAM)** é utilizado para criar políticas detalhadas de controle de acesso, atribuindo permissões granulares com base em funções específicas (RBAC - Role-Based Access Control). Isso inclui a restrição de permissões de leitura, escrita e exclusão de recursos, permitindo um controle rigoroso sobre quem pode modificar a infraestrutura e executar ações sensíveis.

### 6. **Gerenciamento de Recursos Provisórios**
**Descrição**: Identifica e elimina recursos subutilizados ou não utilizados, promovendo eficiência financeira e garantindo que o orçamento anual de **US$ 10.000** seja respeitado.  
**Como Funciona**: Scripts automáticos, agendados via **AWS Lambda** ou **AWS Systems Manager**, fazem a varredura periódica dos recursos, analisando o uso de instâncias EC2, volumes EBS e outros componentes. Recursos inativos são sinalizados para revisão e potenciais ações de desligamento ou exclusão são sugeridas, promovendo a eliminação de desperdício e o alinhamento com as metas de otimização de custos.

### 7. **Gerenciamento de Risco de Segurança**
**Descrição**: Protege a infraestrutura de vulnerabilidades ao identificar e corrigir falhas de segurança conhecidas.  
**Como Funciona**: O **AWS Inspector** realiza varreduras contínuas em instâncias EC2 e containers, identificando vulnerabilidades de segurança, como patches não aplicados e configurações incorretas. Relatórios detalhados são gerados com recomendações de correção, permitindo a remediação rápida e garantindo que a infraestrutura esteja em conformidade com as melhores práticas de segurança.

## Conclusão
Este projeto de **tagueamento automatizado** na AWS promove um alto nível de eficiência operacional, ao mesmo tempo em que garante uma governança robusta e conformidade contínua através de **guardrails** claramente definidos. A automação do processo de provisionamento e a validação de tags asseguram o controle financeiro preciso e alinhado às políticas organizacionais, enquanto as auditorias regulares e os sistemas de monitoramento garantem a conformidade com as diretrizes de segurança. Com a implementação de **guardrails** eficazes, a infraestrutura se mantém protegida, gerenciável e otimizada para reduzir riscos e maximizar a eficiência financeira, tudo dentro do orçamento anual de **US$ 10.000**.

https://aws.amazon.com/pt/blogs/architecture/lets-architect-cost-optimizing-aws-workloads/