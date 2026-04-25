import re
import yfinance as yf


def detect_intent(query):
    query = query.lower()

    if any(word in query for word in ["price", "current", "cost"]):
        return "price"

    elif any(word in query for word in ["buy", "sell", "predict", "should"]):
        return "prediction"

    elif any(word in query for word in ["what", "how", "why", "explain"]):
        return "education"

    return "general"


def extract_stock(query):
    query = query.upper()

    mapping = {
        "RELIANCE": "RELIANCE.NS",
        "TCS": "TCS.NS",
        "INFOSYS": "INFY.NS",
        "HDFC": "HDFCBANK.NS",
        "ICICI": "ICICIBANK.NS",
        "APPLE": "AAPL",
        "TESLA": "TSLA",
        "GOOGLE": "GOOGL",
        "AMAZON": "AMZN",
        "MICROSOFT": "MSFT"
    }

    for name in mapping:
        if name in query:
            return mapping[name]

    words = re.findall(r'\b[A-Z]{2,10}\b', query)

    for word in words:
        try:
            data = yf.Ticker(word)
            if not data.history(period="1d").empty:
                return word
        except:
            continue

    return None