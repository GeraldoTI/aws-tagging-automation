# **Projeto de Tagueamento Automatizado na AWS**

## **Objetivo**
Este projeto demonstra como provisionar uma aplicação na AWS com um orçamento de US$ 10.000, garantindo que todos os recursos estejam devidamente tagueados para controle financeiro.

## **Estrutura do Projeto**
- **architecture/**: Diagrama da arquitetura.
- **lambda/tagging/lambda_function.py**: Função Lambda para tagueamento.
- **lambda/buildspec.yml**: Configuração de build para a Lambda.
- **templates/template.yaml**: Modelo CloudFormation para provisionamento dos recursos.
- **templates/pipeline.yaml**: Definição do pipeline de CI/CD.

## **Passo a Passo para Implementação**

### **1. Configuração da Função Lambda**
- **Objetivo**: Criar uma função Lambda que aplica tags nos recursos.
- **Implementação**:
  - Faça o upload do código da função em `lambda/tagging/lambda_function.py`. O código deve incluir a lógica para aplicar tags com base nos parâmetros passados durante a criação do recurso.
  - Configure o IAM Role necessário com permissões para modificar tags. Isso envolve conceder permissões específicas, como `ec2:CreateTags` e `rds:AddTagsToResource`, para garantir que a função Lambda possa operar corretamente.

### **2. Provisionamento dos Recursos**
- **Objetivo**: Usar o AWS CloudFormation para provisionar instâncias EC2 e RDS.
- **Implementação**:
  - Execute o modelo CloudFormation localizado em `templates/template.yaml`. Este modelo define os recursos a serem provisionados, incluindo instâncias EC2, bancos de dados RDS e outros recursos associados, garantindo que todos sejam tagueados conforme as diretrizes de tagueamento.

### **3. Configuração do Pipeline de CI/CD**
- **Objetivo**: Automatizar o processo de build e deploy.
- **Implementação**:
  - Utilize o arquivo `templates/pipeline.yaml` para definir o pipeline no AWS CodePipeline. O pipeline deve incluir as seguintes etapas:
    - **Source**: Integrar o repositório Git onde o código está armazenado.
    - **Build**: Utilizar o arquivo `lambda/buildspec.yml` para definir o processo de build da função Lambda. Este arquivo deve conter comandos para instalar dependências e empacotar a função.
    - **Deploy**: Implementar o modelo CloudFormation e a função Lambda no ambiente AWS.

### **4. Monitoramento de Custos**
- **Objetivo**: Monitorar os custos utilizando AWS Budgets e Cost Explorer.
- **Implementação**:
  - Configure orçamentos no AWS Budgets para alertar quando os custos se aproximarem de US$ 10.000. Isso permite que você receba notificações quando os gastos atingirem limites críticos, ajudando a evitar surpresas financeiras.

## **Tipos de Guardrails Utilizados**

### **1. Validação de Tags em Tempo de Criação**
- **Descrição**: Este guardrail assegura que todas as tags obrigatórias estejam presentes antes da criação de qualquer recurso na AWS. Isso é fundamental para garantir que todos os recursos sejam adequadamente categorizados para fins de gerenciamento e controle de custos.
- **Como Funciona**: Uma função Lambda é acionada sempre que um novo recurso é criado. Ela verifica as tags e rejeita a criação se as tags obrigatórias não estiverem presentes.

### **2. Orçamento e Limite de Gastos**
- **Descrição**: Este guardrail permite que você defina orçamentos que monitoram os custos e alertam quando um limite pré-definido é atingido. Isso ajuda a garantir que você não ultrapasse seu orçamento.
- **Como Funciona**: O AWS Budgets é utilizado para configurar alertas de custo. Você pode definir limites específicos e ser notificado via e-mail ou SNS quando seus gastos se aproximarem ou excederem esses limites.

### **3. Auditoria de Recursos Tagueados**
- **Descrição**: Este guardrail garante que todos os recursos em sua conta estejam devidamente tagueados. A falta de tags pode levar a dificuldades na gestão de custos e na conformidade.
- **Como Funciona**: Uma função Lambda é agendada para executar auditorias periódicas. Ela verifica todos os recursos e emite relatórios sobre aqueles que não estão tagueados corretamente.

### **4. Regras de Compliance**
- **Descrição**: Este guardrail é responsável por assegurar que todos os recursos estejam em conformidade com as políticas de segurança e governança da sua organização.
- **Como Funciona**: O AWS Config monitora as configurações dos recursos e gera alertas se alguma configuração não estiver em conformidade com as regras estabelecidas.

### **5. Controle de Acesso e Permissões**
- **Descrição**: Este guardrail garante que apenas usuários e funções autorizadas possam executar ações críticas na infraestrutura da AWS.
- **Como Funciona**: Políticas de IAM são aplicadas para definir permissões. Isso ajuda a mitigar riscos de segurança, garantindo que apenas usuários com as permissões adequadas possam acessar ou modificar recursos sensíveis.

### **6. Uso de Recursos Provisórios**
- **Descrição**: Este guardrail ajuda a identificar e remover recursos não utilizados, reduzindo custos e evitando a proliferação de recursos desnecessários.
- **Como Funciona**: Scripts automatizados são executados para verificar o uso dos recursos e eliminar aqueles que não estão em uso por um determinado período.

### **7. Gerenciamento de Risco de Segurança**
- **Descrição**: Este guardrail é crucial para proteger recursos expostos e vulneráveis na AWS.
- **Como Funciona**: Ferramentas como o AWS Inspector são utilizadas para realizar varreduras de segurança nos recursos provisionados, identificando vulnerabilidades e recomendando ações corretivas.

## **Automação do Processo**
- **Automação Total**: O projeto visa automatizar todo o processo de provisionamento, tagueamento, monitoramento de custos e compliance. Isso garante eficiência e minimiza erros humanos.
- **Relatórios**: Utilize o AWS Cost Explorer para extrair relatórios sobre gastos e monitorar se as tags estão sendo aplicadas corretamente. Isso proporciona uma visão clara e em tempo real dos custos associados a cada recurso.

