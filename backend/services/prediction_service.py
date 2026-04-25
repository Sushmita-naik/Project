def predict_stock(features):
    price = features[0]

    # Simple logic (can replace with ML later)
    if price > 1000:
        return "BUY"
    else:
        return "SELL"