from flask import Flask, render_template, request, redirect, url_for

# Імпорт моделей таблиць та сессії для роботи з БД
from databases import Session, Product, Order

app = Flask(__name__)


# Головна сторінка
@app.route("/")
def index():
    return render_template("index.html")


# Сторінка з усіма товарами
@app.route("/products")
def products():
    with Session() as session:
        all_products = session.query(Product).all()  # Взяття усіх товарів з БД

    return render_template(
        "products.html", products=all_products
    )  # Передача html-файлу разом з інформацією про товари


# Сторінка замовлення
@app.route("/order/<int:product_id>", methods=["GET", "POST"])
def order(product_id):
    with Session() as session:
        product = session.query(Product).get(
            product_id
        )  # Забираємо данні про товар за його id

        if not product:
            return "Товар не знайдено", 404

        if request.method == "POST":
            phone = request.form["phone"]
            email = request.form["email"]

            # Створюємо нове замовлення
            new_order = Order(phone=phone, email=email, product_id=product_id)
            session.add(new_order)
            session.commit()

            return redirect(
                url_for("index")
            )  # Повертаємо користувача на головну сторінку
        return render_template(
            "order.html", product=product
        )  # Передаємо данні про товар разом з html-файлом


if __name__ == "__main__":
    app.run(debug=True, port=8080)
