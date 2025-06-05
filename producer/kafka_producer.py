from kafka import KafkaProducer
import time
import pandas as pd
import json
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', 
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

topic = 'accident-topic'

df = pd.read_csv('UK_Accident.csv')

for _, row in df.iterrows():
    message = row.to_dict()
    producer.send(topic, message)
    time.sleep(random.uniform(0.1, 1))  # simulasi stream
    print(f"Sent message: {message}")  # pindahkan ke sini agar tiap pesan diprint
