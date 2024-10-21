# Projeto de Tagueamento Automatizado na AWS

## Objetivo
Este projeto tem como objetivo automatizar o provisionamento de recursos na AWS com um orçamento de US$ 10.000, garantindo que todos os recursos estejam devidamente tagueados para controle financeiro. A implementação de **guardrails** é essencial para garantir a conformidade e a segurança da infraestrutura.

## Guardrails Implementados

### 1. **Validação de Tags em Tempo de Criação**
**Descrição**: Este guardrail garante que todas as tags obrigatórias estejam presentes antes da criação de qualquer recurso na AWS.  
**Como Funciona**: Uma função Lambda é acionada durante o processo de criação de um recurso. Essa função verifica se as tags necessárias foram fornecidas e rejeita a criação se alguma delas estiver faltando. Isso ajuda a evitar a criação de recursos descontrolados e não rastreados.

### 2. **Orçamento e Limite de Gastos**
**Descrição**: Este guardrail define orçamentos que monitoram os gastos em tempo real e alertam os usuários quando um limite específico é atingido.  
**Como Funciona**: Utilizando o AWS Budgets, configuramos alertas que notificam os responsáveis sobre o uso financeiro, permitindo intervenções proativas antes que o orçamento seja excedido.

### 3. **Auditoria de Recursos Tagueados**
**Descrição**: Garante que todos os recursos provisionados estejam em conformidade com as políticas de tagueamento.  
**Como Funciona**: Uma função Lambda é programada para realizar auditorias periódicas, verificando se as tags exigidas estão aplicadas a todos os recursos. Isso assegura a conformidade contínua com as diretrizes de governança.

### 4. **Regras de Compliance**
**Descrição**: Este guardrail assegura que todos os recursos estejam alinhados com as políticas de segurança e governança definidas pela organização.  
**Como Funciona**: O AWS Config é utilizado para monitorar as configurações dos recursos e emitir alertas quando as regras de compliance não são atendidas, facilitando a manutenção da integridade da infraestrutura.

### 5. **Controle de Acesso e Permissões**
**Descrição**: Garante que apenas usuários autorizados possam executar ações críticas na infraestrutura.  
**Como Funciona**: Políticas de IAM (Identity and Access Management) são implementadas para restringir o acesso, definindo permissões granulares que ajudam a proteger recursos sensíveis.

### 6. **Uso de Recursos Provisórios**
**Descrição**: Ajuda a identificar e remover recursos não utilizados, evitando desperdício.  
**Como Funciona**: Scripts automatizados verificam periodicamente o uso dos recursos e sugerem ações para descontinuar aqueles que não estão em uso, contribuindo para uma gestão financeira mais eficiente.

### 7. **Gerenciamento de Risco de Segurança**
**Descrição**: Protege recursos expostos a vulnerabilidades conhecidas.  
**Como Funciona**: O AWS Inspector realiza varreduras regulares para identificar falhas de segurança e fornece relatórios que ajudam na remediação rápida.

## Conclusão
Este projeto de tagueamento automatizado na AWS não apenas promove a eficiência operacional, mas também estabelece um conjunto robusto de guardrails que garantem conformidade e segurança. A automação do processo de provisionamento e tagueamento, juntamente com práticas de monitoramento financeiro, garante que a infraestrutura esteja alinhada com as melhores práticas de governança. Ao seguir este guia, você estará bem equipado para gerenciar recursos na nuvem de forma eficaz e segura.


https://aws.amazon.com/pt/blogs/architecture/lets-architect-cost-optimizing-aws-workloads/