from fastapi import FastAPI, HTTPException
import redis
from redis_cache.cache_manager import get_cached_recommendations


app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379)

@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: int):
    recs = get_cached_recommendations(redis_client, user_id)
    if recs is None:
        raise HTTPException(status_code=404, detail="No recommendations found")
    return {"user_id": user_id, "recommendations": recs}
