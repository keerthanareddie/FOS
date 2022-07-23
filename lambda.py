import boto3

client = boto3.client('ce', region_name='us-east-1')
def get_total_billing(client) -> dict:
    (start_date, end_date) = get_total_cost_date_range()
response = client.get_cost_and_usage(
    TimePeriod={
        'Start': 'start_date',
        'End': 'end_date'
    },
    Granularity='MONTHLY',
    Metrics=[
        'AmortizedCost',
    ]
)

print(response)