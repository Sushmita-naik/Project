from flask import Flask, request, jsonify
from flask_cors import CORS

from services.nlp_service import extract_stock, detect_intent
from services.stock_service import get_stock
from services.prediction_service import predict_stock
from services.gpt_service import gpt_response
from services.filter_service import is_stock_query

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "🚀 Stock AI running"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        query = data.get("message", "")

        # 🔴 STRICT FILTER
        if not is_stock_query(query):
            return jsonify({
                "response": "❌ I only answer stock market related questions."
            })

        symbol = extract_stock(query)
        intent = detect_intent(query)

        stock_data = None
        if symbol:
            stock_data = get_stock(symbol)

        # 📘 EDUCATION
        if intent == "education":
            response = gpt_response(query, {}, "N/A", [])
            return jsonify({"response": response})

        # 💰 PRICE
        if intent == "price":
            if not stock_data:
                return jsonify({"response": "Please mention a valid stock like RELIANCE or AAPL."})

            return jsonify({
                "response": f"Current price of {symbol} is ₹{round(stock_data['price'], 2)}"
            })

        # 📈 PREDICTION
        if intent == "prediction":
            if not stock_data:
                return jsonify({"response": "Please mention a stock for prediction."})

            prediction = predict_stock([
                stock_data["price"],
                50,
                0
            ])

            response = gpt_response(query, stock_data, prediction, [])
            return jsonify({"response": response})

        # 🤖 GENERAL STOCK RESPONSE
        response = gpt_response(query, stock_data or {}, "N/A", [])
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
