import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from .data_loader import load_stock_features, load_user_portfolio
import numpy as np

def recommend_stocks(user_id):
    stock_features = load_stock_features()
    user_stocks = load_user_portfolio(user_id)

    if not user_stocks:
        return []

    user_vecs = stock_features[stock_features['stock'].isin(user_stocks)]['sector_vector'].tolist()
    user_profile = np.mean(user_vecs, axis=0).reshape(1, -1)
    stock_features['similarity'] = stock_features['sector_vector'].apply(lambda x: cosine_similarity([x], user_profile)[0][0])

    recommendations = stock_features[~stock_features['stock'].isin(user_stocks)].sort_values(by='similarity', ascending=False)
    return recommendations['stock'].tolist()
