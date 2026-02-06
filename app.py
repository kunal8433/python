from flask import Flask, render_template

app = Flask("Kunal Clothing Store")

# This is your product database
products = [
    {
        "id": 1,
        "name": "Classic Denim Jacket",
        "price": 1200,
        "image": "jacket.jpg" # Make sure this exists in static/
    },
    {
        "id": 2,
        "name": "Premium White T-Shirt",
        "price": 500,
        "image": "tshirt.jpg"
    }
]

@app.route('/')
def home():
    return render_template('index.html', store_name="Kunal Clothing Store", items=products)

if __name__ == '__main__':
    app.run(debug=True)