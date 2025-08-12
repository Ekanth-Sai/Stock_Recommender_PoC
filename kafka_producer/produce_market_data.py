from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

stocks = ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK']

def generate_market_data():
    return {
        'stock': random.choice(stocks),
        'price': round(random.uniform(1000, 3000), 2),
        'volume': random.randint(100, 10000),
        'timestamp': time.time()
    }

if __name__ == "__main__":
    while True:
        data = generate_market_data()
        print(f"Producing: {data}")
        producer.send('market_data', value=data)
        time.sleep(1)
