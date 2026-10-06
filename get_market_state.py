import MetaTrader5 as mt5
import pandas as pd
import json

def get_market_data():
    if not mt5.initialize():
        return json.dumps({"error": "MT5 not initialized"})
    
    # Get last 24 candles of H1 (1 Day)
    rates = mt5.copy_rates_from_pos("XAUUSD", mt5.TIMEFRAME_H1, 0, 24)
    if rates is None:
        return json.dumps({"error": "Cannot get data"})
        
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    
    current_price = df.iloc[-1]['close']
    high_24h = df['high'].max()
    low_24h = df['low'].min()
    
    data = {
        "symbol": "XAUUSD",
        "current_price": float(current_price),
        "support_24h": float(low_24h),
        "resistance_24h": float(high_24h),
    }
    mt5.shutdown()
    return json.dumps(data)

if __name__ == "__main__":
    print(get_market_data())
