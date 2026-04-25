import yfinance as yf


def get_stock(symbol):
    try:
        df = yf.download(symbol, period="3mo")

        if df.empty:
            return None

        return {
            "symbol": symbol,
            "price": float(df['Close'].iloc[-1]),
            "high": float(df['High'].iloc[-1]),
            "low": float(df['Low'].iloc[-1])
        }

    except:
        return None