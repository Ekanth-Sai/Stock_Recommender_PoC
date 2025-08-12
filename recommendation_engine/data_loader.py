import pandas as pd

def load_stock_features():
    data = {
        'stock': ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK'],
        'sector_vector': [
            [1,0,0],
            [0,1,0],
            [0,1,0],
            [1,0,0],
            [1,0,0]
        ]
    }
    return pd.DataFrame(data)

def load_user_portfolio(user_id):
    portfolios = {
        1: ['RELIANCE', 'TCS'],
        2: ['INFY', 'HDFCBANK'],
    }
    return portfolios.get(user_id, [])
