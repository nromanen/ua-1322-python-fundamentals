from functools import wraps

from flask import Flask, session, current_app
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for, flash

db = SQLAlchemy()
app = Flask(__name__)

app.config['SECRET_KEY'] = 'abracadabraparol'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ADMIN_USERNAME'] = 'admin'
app.config['ADMIN_PASSWORD'] = 'admin'

db.init_app(app)

with app.app_context():
    from models.models import Category, Product, Order, OrderItem
    db.create_all()


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
         if not session.get('admin'):
             flash("Тільки адміністратор має доступ до цієї сторінки", "danger")
             return redirect(url_for('login'))
         return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('index.html', products=products, categories=categories)

@app.route('/category/<int:category_id>')
def category_products(category_id):
    category = Category.query.get_or_404(category_id)
    products = Product.query.filter_by(category_id=category.id).all()
    categories = Category.query.all()
    return render_template('category_products.html', category=category, products=products, categories=categories)


@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    flash(f"{product.name} додано до корзини", "success")
    return redirect(url_for('index'))


@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    product = Product.query.get_or_404(product_id)
    if str(product_id) in cart:
        cart.pop(str(product_id))
        session['cart'] = cart
        flash(f"{product.name} видалено з корзини", "success")
    return redirect(url_for('cart'))


@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    products = []
    total = 0.0
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            item_total = product.price * quantity
            total += item_total
            products.append({'product': product, 'quantity': quantity, 'item_total': item_total})
    return render_template('cart.html', products=products, total=total)


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', {})
    if not cart:
        flash("Ваша корзина пуста", "warning")
        return redirect(url_for('index'))

    items = []
    total = 0.0
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            item_total = product.price * quantity
            total += item_total
            items.append({'product': product, 'quantity': quantity, 'item_total': item_total})

    if request.method == 'POST':
        customer_email = request.form.get('email')
        if not customer_email:
            flash("Будь ласка, вкажіть email", "danger")
            return redirect(url_for('checkout'))
        new_order = Order(customer_email=customer_email)
        db.session.add(new_order)
        db.session.commit()

        for item in items:
            order_item = OrderItem(
                order_id=new_order.id,
                product_id=item['product'].id,
                quantity=item['quantity'],
                price=item['product'].price
            )
            db.session.add(order_item)
        db.session.commit()
        session['cart'] = {}
        flash("Замовлення оформлено!", "success")
        return redirect(url_for('index'))

    return render_template('checkout.html', items=items, total=total)


@app.route('/search')
def search():
    from sqlalchemy import or_
    query = request.args.get('q', '')
    results = []
    if query:
        results = Product.query.filter(
            or_(
                Product.name.ilike(f"%{query}%"),
                Product.description.ilike(f"%{query}%")
            )
        ).all()
    categories = Category.query.all()
    return render_template('search_results.html', query=query, results=results, categories=categories)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        admin_username = current_app.config.get('ADMIN_USERNAME')
        admin_password = current_app.config.get('ADMIN_PASSWORD')
        if username == admin_username and password == admin_password:
            session['admin'] = True
            flash("Ви успішно увійшли як адміністратор", "success")
            return redirect(url_for('index'))
        else:
            flash("Невірні облікові дані", "danger")
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('admin', None)
    flash("Ви вийшли з системи", "success")
    return redirect(url_for('index'))


@app.route('/add_product', methods=['GET', 'POST'])
@admin_required
def add_product():
    categories = Category.query.all()
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        category_id = request.form.get('category_id')
        if not (name and price and category_id):
            flash("Заповніть всі обов’язкові поля", "danger")
            return redirect(url_for('add_product'))
        try:
            price = float(price)
        except ValueError:
            flash("Невірно вказана ціна", "danger")
            return redirect(url_for('add_product'))
        product = Product(name=name, description=description, price=price, category_id=category_id)
        db.session.add(product)
        db.session.commit()
        flash("Товар додано", "success")
        return redirect(url_for('index'))
    return render_template('add_product.html', categories=categories)


@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
@admin_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    categories = Category.query.all()
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        try:
            product.price = float(request.form.get('price'))
        except ValueError:
            flash("Невірно вказана ціна", "danger")
            return redirect(url_for('edit_product', product_id=product.id))
        product.category_id = request.form.get('category_id')
        db.session.commit()
        flash("Товар оновлено", "success")
        return redirect(url_for('index'))
    return render_template('edit_product.html', product=product, categories=categories)


@app.route('/delete_product/<int:product_id>', methods=['POST'])
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Товар видалено", "success")
    return redirect(url_for('index'))


@app.route('/add_category', methods=['GET', 'POST'])
@admin_required
def add_category():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            flash("Вкажіть назву категорії", "danger")
            return redirect(url_for('add_category'))
        existing = Category.query.filter_by(name=name).first()
        if existing:
            flash("Категорія з такою назвою вже існує", "danger")
            return redirect(url_for('add_category'))
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        flash("Категорію додано", "success")
        return redirect(url_for('index'))
    return render_template('add_category.html')


@app.route('/edit_category/<int:category_id>', methods=['GET', 'POST'])
@admin_required
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == 'POST':
        new_name = request.form.get('name')
        if not new_name:
            flash("Вкажіть назву категорії", "danger")
            return redirect(url_for('edit_category', category_id=category.id))
        category.name = new_name
        db.session.commit()
        flash("Категорію оновлено", "success")
        return redirect(url_for('list_categories'))
    return render_template('edit_category.html', category=category)


@app.route('/delete_category/<int:category_id>', methods=['POST'])
@admin_required
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    if category.products:
        flash("Неможливо видалити категорію, бо вона містить товари", "danger")
        return redirect(url_for('list_categories'))
    db.session.delete(category)
    db.session.commit()
    flash("Категорію видалено", "success")
    return redirect(url_for('list_categories'))


@app.route('/categories')
@admin_required
def list_categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)


@app.route('/admin/orders')
@admin_required
def admin_orders():
    orders = Order.query.order_by(Order.timestamp.desc()).all()
    return render_template('admin_orders.html', orders=orders)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
