import json

def cache_recommendations(redis_client, user_id, recommendations):
    key = f"user:{user_id}:recommendations"
    redis_client.set(key, json.dumps(recommendations), ex=300) 

def get_cached_recommendations(redis_client, user_id):
    key = f"user:{user_id}:recommendations"
    cached = redis_client.get(key)
    if cached:
        return json.loads(cached)
    return None
