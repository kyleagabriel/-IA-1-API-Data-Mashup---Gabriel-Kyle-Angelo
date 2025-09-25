from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def test():
    return "hello world"

def product_list(limit):
    url = "https://fakestoreapi.com/products" 
    req = requests.get(url, params={"limit":limit})
    return req.json()

def exchange_rate(amount):
    url = "https://api.exchangerate.host/convert"
    req = requests.get(url, params={"access_key":"fc6be6524c09d3f97bee2dfc0cc2d2b1","from":"USD", "to":"PHP", "amount":amount})
    return req.json()["result"]

@app.get("/products")
def products():
    limit = request.args.get("limit", 10, type=int)
    products = product_list(limit)
    items = [{
        "id": p["id"], 
        "category": p["category"],
        "title": p["title"], 
        "description":p["description"],
        "price_usd": p["price"]
        } 
        for p in products
    ]
    return {"count": len(items), "items": items}

@app.get("/rate")
def rate():
    amount = request.args.get("amount", 1, type=float)
    rate = exchange_rate(amount)
    return {"USD ($)":amount, "PHP (P)":rate}

@app.get("/join")
def join():
    limit = request.args.get("limit", 10, type=int)
    amount = request.args.get("amount", 1, type=float)

    try:
        products = product_list(limit)         
        rate = exchange_rate(amount)           

        items = [
            {
                "title": p["title"],
                "category": p["category"],
                "description": p["description"],
                "price_usd": float(p["price"]),
                "price_php": round(float(p["price"]) * rate, 2),
            }
            for p in products
        ]

        return {"count": len(items), "items": items}

    except requests.exceptions.RequestException:
        return {"error": "⚠️ Network issue while fetching data. Please try again."}, 502
    
    except (ValueError, KeyError, TypeError):
        return {"error": "⚠️ Bad data received from API. Please try again later."}, 502

@app.get("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(port=5000)