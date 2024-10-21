# Projeto de Tagueamento Automatizado na AWS

## Objetivo
Este projeto demonstra como provisionar uma aplicação na AWS com um orçamento de US$ 10.000, garantindo que todos os recursos estejam devidamente tagueados para controle financeiro.

## Estrutura do Projeto
- `architecture/`: Diagrama da arquitetura.
- `lambda/tagging/lambda_function.py`: Função Lambda para tagueamento.
- `lambda/buildspec.yml`: Configuração de build para a Lambda.
- `templates/template.yaml`: Modelo CloudFormation para provisionamento dos recursos.
- `templates/pipeline.yaml`: Definição do pipeline de CI/CD.

## Passo a Passo para Implementação
1. **Configuração da Função Lambda**
   - Objetivo: Criar uma função Lambda que aplica tags nos recursos.
   - Implementação: Faça o upload do código da função em `lambda/tagging/lambda_function.py`.

2. **Provisionamento dos Recursos**
   - Objetivo: Usar o AWS CloudFormation para provisionar instâncias EC2 e RDS.
   - Implementação: Execute o modelo CloudFormation localizado em `templates/template.yaml`.

3. **Configuração do Pipeline de CI/CD**
   - Objetivo: Automatizar o processo de build e deploy.
   - Implementação: Utilize o arquivo `templates/pipeline.yaml` para definir o pipeline no AWS CodePipeline.

4. **Monitoramento de Custos**
   - Objetivo: Monitorar os custos utilizando AWS Budgets e Cost Explorer.
   - Implementação: Configure orçamentos no AWS Budgets para alertar quando os custos se aproximarem de US$ 10.000.

## Pipeline de Tagueamento Automatizado
Este pipeline utiliza o AWS CodePipeline para automatizar o processo de tagueamento de recursos na AWS. O pipeline é composto pelas seguintes etapas:

1. **Source**: Captura alterações no repositório de código.
2. **Build**: Compila o código da função Lambda e prepara para implantação.
3. **Deploy**: Implanta a função Lambda e suas permissões necessárias.
4. **Tagging**: Executa a função Lambda que aplica tags aos recursos.

## Tipos de Guardrails Utilizados
- Validação de Tags em Tempo de Criação
- Orçamento e Limite de Gastos
- Auditoria de Recursos Tagueados
- Regras de Compliance
- Controle de Acesso e Permissões
- Uso de Recursos Provisórios
- Gerenciamento de Risco de Segurança
