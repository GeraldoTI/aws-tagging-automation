# Projeto de Tagueamento Automatizado na AWS

## Objetivo
Este projeto demonstra como provisionar uma aplicação na AWS com um orçamento de US$ 10.000, garantindo que todos os recursos estejam devidamente tagueados para controle financeiro.

## Estrutura do Projeto
- `architecture/`: Diagrama da arquitetura.
- `lambda/tagging/lambda_function.py`: Função Lambda para tagueamento.
- `lambda/buildspec.yml`: Configuração de build para a Lambda.
- `templates/template.yaml`: Modelo CloudFormation para provisionamento dos recursos.
- `templates/pipeline.yaml`: Definição do pipeline de CI/CD.

## Como Usar
1. Faça o upload da função Lambda no AWS.
2. Execute o modelo CloudFormation para provisionar os recursos.
3. Monitore os custos usando AWS Budgets e Cost Explorer.


Você pode criar um diagrama que inclua os seguintes componentes:

AWS Lambda: Representa a função Lambda que aplica tags.
EC2 Instances: Representa as instâncias EC2 que serão tagueadas.
RDS Instances: Representa as instâncias RDS que serão tagueadas.
AWS CodePipeline: Representa o pipeline que automatiza o processo de build e deploy.
Conclusão
Após seguir esses passos, seu repositório estará configurado com todos os arquivos necessários para o projeto de tagueamento automatizado na AWS. 


Guardrails para o Projeto de Tagueamento Automatizado
Validação de Tags em Tempo de Criação

Descrição: Antes de qualquer recurso ser criado, o pipeline deve validar se as tags obrigatórias estão sendo aplicadas. Se as tags não atenderem aos critérios definidos, a criação do recurso é rejeitada.
Implementação: Use uma função Lambda para verificar as tags antes da criação do recurso.
Orçamento e Limite de Gastos

Descrição: Configure orçamentos no AWS Budgets para monitorar e alertar quando os custos atingirem um limite específico (ex. US$ 10.000).
Implementação: O pipeline deve incluir uma etapa para verificar as configurações de orçamento e enviar alertas por meio do Amazon SNS se o limite estiver próximo.
Auditoria de Recursos Tagueados

Descrição: Implementar um processo de auditoria para verificar se todos os recursos estão tagueados corretamente. Recursos não tagueados podem ser automaticamente desativados ou removidos.
Implementação: Uma função Lambda pode ser agendada para rodar periodicamente e verificar as tags nos recursos.
Regras de Compliance

Descrição: Implementar regras de compliance utilizando o AWS Config para garantir que as instâncias e recursos estejam sempre em conformidade com as políticas definidas.
Implementação: No pipeline, adicione uma etapa que verifica as configurações de compliance e gera relatórios.
Controle de Acesso e Permissões

Descrição: Definir políticas de IAM para limitar o acesso a recursos e operações críticas. Somente usuários e serviços autorizados devem ter permissão para criar ou modificar tags.
Implementação: O pipeline deve incluir verificações de permissões em cada etapa, garantindo que apenas entidades autorizadas possam interagir com o projeto.
Uso de Recursos Provisórios

Descrição: Para evitar custos desnecessários, implemente uma estratégia para desativar ou excluir recursos não utilizados. Isso pode incluir instâncias EC2 ou RDS que não estão em uso.
Implementação: O pipeline pode incluir uma etapa de limpeza para identificar e remover recursos não utilizados.
Gerenciamento de Risco de Segurança

Descrição: Implementar práticas de segurança, como a configuração de grupos de segurança e listas de controle de acesso (ACLs), para proteger recursos expostos.
Implementação: O pipeline deve incluir uma revisão de segurança, utilizando o AWS Inspector ou outras ferramentas de segurança, para verificar a configuração de segurança dos recursos.# aws-tagging-automation
