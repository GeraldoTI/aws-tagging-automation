Projeto de Tagueamento Automatizado na AWS
Objetivo
Este projeto demonstra como provisionar uma aplicação na AWS com um orçamento de US$ 10.000, garantindo que todos os recursos estejam devidamente tagueados para controle financeiro.

Estrutura do Projeto
architecture/: Diagrama da arquitetura.
lambda/tagging/lambda_function.py: Função Lambda para tagueamento.
lambda/buildspec.yml: Configuração de build para a Lambda.
templates/template.yaml: Modelo CloudFormation para provisionamento dos recursos.
templates/pipeline.yaml: Definição do pipeline de CI/CD.
Passo a Passo para Implementação
1. Configuração da Função Lambda
Objetivo: Criar uma função Lambda que aplica tags nos recursos.
Implementação:
Faça o upload do código da função em lambda/tagging/lambda_function.py.
Configure o IAM Role necessário com permissões para modificar tags.
2. Provisionamento dos Recursos
Objetivo: Usar o AWS CloudFormation para provisionar instâncias EC2 e RDS.
Implementação:
Execute o modelo CloudFormation localizado em templates/template.yaml.
3. Configuração do Pipeline de CI/CD
Objetivo: Automatizar o processo de build e deploy.
Implementação:
Utilize o arquivo templates/pipeline.yaml para definir o pipeline no AWS CodePipeline.
4. Monitoramento de Custos
Objetivo: Monitorar os custos utilizando AWS Budgets e Cost Explorer.
Implementação:
Configure orçamentos no AWS Budgets para alertar quando os custos se aproximarem de US$ 10.000.
Tipos de Guardrails Utilizados
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
Automação do Processo
Automação Total: O projeto visa automatizar todo o processo de provisionamento, tagueamento, monitoramento de custos e compliance.
Relatórios: Utilize AWS Cost Explorer para extrair relatórios sobre gastos e monitorar se as tags estão sendo aplicadas corretamente.