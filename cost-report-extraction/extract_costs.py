
#### 2. `extract_costs.py`

Aqui está um exemplo simples de como você pode implementar a extração de dados de custo usando Boto3:

```python
import boto3
import datetime

# Configurar o cliente do Cost Explorer
client = boto3.client('ce')

def extract_costs(start_date, end_date):
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date,
            'End': end_date
        },
        Granularity='DAILY',
        Metrics=['BlendedCost']
    )
    
    return response

if __name__ == "__main__":
    # Define o período para o relatório de custos
    today = datetime.date.today()
    start_date = (today - datetime.timedelta(days=30)).strftime('%Y-%m-%d')  # 30 dias atrás
    end_date = today.strftime('%Y-%m-%d')  # Data de hoje

    costs = extract_costs(start_date, end_date)

    # Exibe os resultados
    for result in costs['ResultsByTime']:
        print(f"Data: {result['TimePeriod']['Start']} - Custo: {result['Total']['BlendedCost']['Amount']} {result['Total']['BlendedCost']['Unit']}")
