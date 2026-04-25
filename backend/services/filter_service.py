import re

def is_stock_query(query):
    query_lower = query.lower()

    stock_keywords = [
        "stock", "stocks", "share", "shares",
        "market", "trading", "price", "chart",
        "buy", "sell", "invest", "investment",
        "portfolio", "dividend",
        "nifty", "sensex", "nasdaq", "dow",
        "profit", "loss", "trend", "analysis",
        "company", "earnings", "revenue"
    ]

    if any(word in query_lower for word in stock_keywords):
        return True

    # Stock symbol like AAPL, TSLA
    if re.search(r'\b[A-Z]{2,5}\b', query):
        return True

    # Common companies
    if any(word in query_lower for word in ["apple", "tesla", "reliance", "tcs", "infosys"]):
        return True

    return False