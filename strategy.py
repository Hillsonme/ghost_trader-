import pandas as pd
import yfinance as yf

def moving_average_signal(symbol="AAPL", short=10, long=50):
    # Pull 6 months free historical data
    data = yf.download(symbol, period="6mo", interval="1d")
    data['SMA_10'] = data['Close'].rolling(window=short).mean()
    data['SMA_50'] = data['Close'].rolling(window=long).mean()
    
    latest_short = data['SMA_10'].iloc[-1]
    latest_long = data['SMA_50'].iloc[-1]
    prev_short = data['SMA_10'].iloc[-2]
    prev_long = data['SMA_50'].iloc[-2]
    
    # The ONE concrete rule
    if prev_short <= prev_long and latest_short > latest_long:
        return "BUY"
    elif prev_short >= prev_long and latest_short < latest_long:
        return "SELL"
    else:
        return "HOLD"
