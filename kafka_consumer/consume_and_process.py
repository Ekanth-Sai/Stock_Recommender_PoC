from kafka import KafkaConsumer
import json
import redis
from recommendation_engine.recommender import recommend_stocks
from redis_cache.cache_manager import cache_recommendations

consumer = KafkaConsumer(
    'market_data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

redis_client = redis.Redis(host='localhost', port=6379)

def process_market_data():
    for message in consumer:
        data = message.value
        print(f"Received market data: {data}")

        user_id = 1
        recommendations = recommend_stocks(user_id)
        print(f"Updated recommendations for user {user_id}: {recommendations}")

        cache_recommendations(redis_client, user_id, recommendations)

if __name__ == "__main__":
    process_market_data()
