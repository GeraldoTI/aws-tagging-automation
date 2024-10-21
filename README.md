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


## Automação da Extração de Relatórios Financeiros
A automação deste projeto não se limita apenas ao provisionamento e tagueamento de recursos; ela também facilita a extração de relatórios financeiros. Após a implementação do pipeline, os seguintes processos garantem que as informações financeiras sejam coletadas de maneira eficiente:

1. **AWS Cost Explorer**: 
   - O AWS Cost Explorer é integrado para fornecer relatórios detalhados sobre os gastos. Ele analisa os dados de uso e custo, permitindo que você visualize onde os recursos estão sendo alocados.
   - Relatórios podem ser programados para serem gerados em intervalos regulares, como semanal ou mensalmente.

2. **AWS Budgets**:
   - Os orçamentos configurados no AWS Budgets monitoram os gastos em tempo real e enviam alertas quando os custos se aproximam do limite estabelecido.
   - Isso não só ajuda a evitar surpresas no final do mês, mas também permite que você tome decisões informadas sobre a alocação de recursos.

3. **Relatórios Automatizados**:
   - Scripts ou funções Lambda podem ser criados para extrair automaticamente relatórios financeiros a partir do Cost Explorer e enviá-los por e-mail ou armazená-los em um bucket S3.
   - Isso garante que as partes interessadas tenham acesso rápido e fácil às informações financeiras relevantes, permitindo uma análise mais eficaz e tempestiva.

4. **Integração com ferramentas de BI**:
   - Os dados extraídos podem ser integrados a ferramentas de Business Intelligence (BI) como Tableau ou Power BI para análises mais aprofundadas, visualizações interativas e dashboards personalizados.

Esses processos de automação não apenas aumentam a eficiência, mas também melhoram a transparência e o controle sobre os custos operacionais na AWS.

Referencia.

https://aws.amazon.com/pt/blogs/architecture/lets-architect-cost-optimizing-aws-workloads/