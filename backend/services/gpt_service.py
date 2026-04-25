import os
from dotenv import load_dotenv
from openai import OpenAI

# 🔥 Load .env from project root (2 levels up)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)

# 🔑 Get API Key
api_key = os.getenv("OPENAI_API_KEY")

# 🧪 Debug (remove later)
print("DEBUG KEY:", api_key)

# ❌ Stop if key not found
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Check your .env file!")

# 🤖 Create client
client = OpenAI(api_key=api_key)


# 🚀 MAIN FUNCTION
def gpt_response(query, stock_data=None, prediction=None, news=None):

    # 🎯 System behavior (this controls your AI personality)
    system_prompt = """
You are a smart Stock Market AI Assistant.

Rules:
- Answer ONLY stock, trading, finance related questions
- If user asks unrelated questions (love, jokes, random talk), politely refuse
- Understand messy human questions
- Do NOT force stock name every time
- Give helpful, natural, human-like answers
- If buy/sell asked without stock, give general advice
- If stock data is given, include insights
"""

    # 📊 Add stock context
    context = ""
    if stock_data:
        context += f"\nStock: {stock_data.get('symbol')}"
        context += f"\nPrice: {stock_data.get('price')}"
        context += f"\nPrediction: {prediction}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query + context}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ AI Error: {str(e)}"