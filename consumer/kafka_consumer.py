from kafka import KafkaConsumer
import json
import pandas as pd
import os

# Pastikan folder batch_data ada
os.makedirs('batch_data', exist_ok=True)

# Kafka Consumer
consumer = KafkaConsumer(
    'accident-topic',  
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='accident-group'  
)

batch = []
batch_size = 10000
batch_id = 0

print("Consumer is running and listening to topic...")

for message in consumer:
    print("Received message")
    try:
        data = json.loads(message.value.decode('utf-8'))
        batch.append(data)

        if len(batch) >= batch_size:
            df = pd.DataFrame(batch)
            output_file = f'batch_data/batch_{batch_id}.csv'
            df.to_csv(output_file, index=False)
            print(f"Saved batch to {output_file}")
            batch_id += 1
            batch = []

    except Exception as e:
        print(f"Error processing message: {e}")
