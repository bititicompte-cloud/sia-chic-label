from flask import Flask, render_template

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Pink Dress",
        "price": "299 DH",
        "image": "ea416787-58f0-49c9-999c-048d6899acc7 - Copie.jpg","gallery": [],
        "description": "Robe élégante idéale pour les occasions spéciales."
    },
    {
        "id": 2,
        "name": "Grey Dress",
        "price": "299 DH",
        "image": "greydress.webp" , "gallery" : ["greey2.webp" ,"greeey3.webp" ],
        "description": "Robe élégante idéale pour les occasions spéciales."
    },
    {
        "id": 3,
        "name": "Red Dress",
        "price": "299 DH",
        "image": "5821236319399644865 - Copie.jpg" , "gallery" : ["reeed2.jpg" ,"reeeed3.jpg" ],
        "description": "Robe élégante idéale pour les occasions spéciales."
    },
    {
        "id": 4,
        "name": "Turkois Dress",
        "price": "299 DH",
        "image": "turkoisdress.webp" , "gallery": [],
        "description": "Robe élégante idéale pour les occasions spéciales."
    },
    {
        "id": 5,
        "name": "Blue Dress",
        "price": "299 DH",
        "image": "39517044-0bf9-49f7-9427-c471171ff666.jpg" , "gallery": [],
        "description": "Robe élégante idéale pour les occasions spéciales."
    },
    {
        "id": 6,
        "name": "White Dress",
        "price": "299 DH",
        "image": "white dress.jpg" , "gallery" : ["whiiite2.jpg" , "whiiiite3.jpg"],
        "description": "Robe élégante idéale pour les occasions spéciales."
    },
    {
        "id": 7,
        "name": "Pink Dress",
        "price": "299 DH",
        "image": "pinkdreeees.jpg" , "gallery": [],
        "description": "Robe élégante idéale pour les occasions spéciales."
    }
]
@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/product/<int:id>")
def product_page(id):

    for product in products:
        if product["id"] == id:
            return render_template("product.html", product=product,products=products)

    return "Product not found"

if __name__ == "__main__":
app.run(debug=True)