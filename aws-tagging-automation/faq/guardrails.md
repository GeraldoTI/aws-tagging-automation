# Guardrails Implementados


Guardrails Implementados
Validação de Tags em Tempo de Criação
Descrição: Verifica se as tags obrigatórias estão presentes antes da criação do recurso.
Como Funciona: Uma função Lambda é acionada para validar as tags.

Orçamento e Limite de Gastos
Descrição: Monitora os custos e alerta quando um limite é atingido.
Como Funciona: O AWS Budgets é utilizado para configurar alertas de custo.

Auditoria de Recursos Tagueados
Descrição: Verifica se todos os recursos estão tagueados corretamente.
Como Funciona: Uma função Lambda é agendada para verificar as tags periodicamente.

Regras de Compliance
Descrição: Garante que os recursos estejam em conformidade com as políticas.
Como Funciona: O AWS Config verifica as configurações dos recursos.

Controle de Acesso e Permissões
Descrição: Limita o acesso a operações críticas.
Como Funciona: Políticas de IAM são aplicadas para definir permissões.

Uso de Recursos Provisórios
Descrição: Identifica e remove recursos não utilizados.
Como Funciona: Scripts são executados para limpar recursos não utilizados.

Gerenciamento de Risco de Segurança
Descrição: Protege recursos expostos.
Como Funciona: Ferramentas como o AWS Inspector são utilizadas para verificar a segurança.