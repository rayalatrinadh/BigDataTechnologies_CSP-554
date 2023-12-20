from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'sample',
    bootstrap_servers='172.31.16.110:9092',
    auto_offset_reset='earliest',
    group_id='my-group'
)

for message in consumer:
    key = message.key.decode('utf-8') if message.key else None
    value = message.value.decode('utf-8') if message.value else None
    print(f"Key={key}, Value='{value}'")

consumer.close()