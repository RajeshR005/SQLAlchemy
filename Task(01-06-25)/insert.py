from sqlalchemy.orm import sessionmaker
from models import User,Product,Order,OrderItem,engine,MainCategory,SubCategory
from datetime import datetime

Session=sessionmaker(bind=engine)
session=Session()

user = [
    User(username="Rajesh", email="rajesh@example.com", password="hello@05", user_type=1, status=2, created_by=None),
    User(username="Sandhiya", email="sandhiya2@example.com", password="hello@02", user_type=1, status=1, created_by=None),
    User(username="Kiruba", email="kiruba@example.com", password="hello@02", user_type=1, status=2, created_by=None),
    User(username="krithika", email="krithika@example.com", password="hello@02", user_type=3, status=1, created_by=None),
    User(username="Mohan", email="mohan@example.com", password="hello@02", user_type=2, status=2, created_by=None),
    User(username="Boobalan", email="boobalan@example.com", password="hello@02", user_type=3, status=2, created_by=None),
    User(username="Raja", email="raja@example.com", password="hello@02", user_type=2, status=2, created_by=None),
]


main_categories = [
    MainCategory(name="Electronics", status=1, created_by=1),
    MainCategory(name="Clothing", status=1, created_by=2),
    MainCategory(name="Books", status=1, created_by=3),
    MainCategory(name="Home Appliances", status=1, created_by=4),
    MainCategory(name="Sports", status=1, created_by=5),
    MainCategory(name="Toys", status=1, created_by=6),
    MainCategory(name="Beauty", status=1, created_by=7),
]


sub_categories = [
    SubCategory(main_category_id=1, name="Mobile Phones", status=1, created_by=1),
    SubCategory(main_category_id=1, name="Laptops", status=1, created_by=2),
    SubCategory(main_category_id=2, name="Men's Wear", status=1, created_by=3),
    SubCategory(main_category_id=2, name="Women's Wear", status=1, created_by=4),
    SubCategory(main_category_id=3, name="Fiction", status=1, created_by=5),
    SubCategory(main_category_id=3, name="Non-fiction", status=1, created_by=6),
    SubCategory(main_category_id=4, name="Kitchen Appliances", status=1, created_by=7),
]

products = [
    Product(vendor_id=1, sub_category_id=1, name="Realme 60x 5g", description="New Gen AI Based", price=13999.99, stock=20, status=1, created_by=1),
    Product(vendor_id=1, sub_category_id=2, name="Asus Vivo Book 16", description="Hyper Laptop", price=58999.00, stock=5, status=1, created_by=2),
    Product(vendor_id=2, sub_category_id=3, name="Men's Jacket", description="Winter jacket", price=799.99, stock=70, status=1, created_by=3),
    Product(vendor_id=2, sub_category_id=4, name="Women's Dress", description="Summer dress", price=1299.99, stock=50, status=1, created_by=4),
    Product(vendor_id=3, sub_category_id=5, name="Airbender", description="Fiction book", price=899.99, stock=100, status=1, created_by=5),
    Product(vendor_id=3, sub_category_id=6, name="Biography", description="Non-fiction book", price=499.99, stock=170, status=1, created_by=6),
    Product(vendor_id=4, sub_category_id=7, name="Grinder", description="Kitchen blender", price=4999.99, stock=6, status=1, created_by=7),
]



orders = [
    Order(buyer_id=5, order_date=datetime.strptime("2025-06-02 10:00:00", "%Y-%m-%d %H:%M:%S"), total_amount=1999.98, status=1, created_by=1),
    Order(buyer_id=3, order_date=datetime.strptime("2025-06-03 11:15:00", "%Y-%m-%d %H:%M:%S"), total_amount=799.99, status=1, created_by=2),
    Order(buyer_id=7, order_date=datetime.strptime("2025-05-11 12:30:00", "%Y-%m-%d %H:%M:%S"), total_amount=58999.99, status=1, created_by=3),
    Order(buyer_id=2, order_date=datetime.strptime("2025-04-15 13:45:00", "%Y-%m-%d %H:%M:%S"), total_amount=1299.00, status=1, created_by=4),
    Order(buyer_id=1, order_date=datetime.strptime("2025-01-27 14:00:00", "%Y-%m-%d %H:%M:%S"), total_amount=13999.99, status=1, created_by=5),
    Order(buyer_id=4, order_date=datetime.strptime("2025-01-25 15:20:00", "%Y-%m-%d %H:%M:%S"), total_amount=499.99, status=1, created_by=6),
    Order(buyer_id=6, order_date=datetime.strptime("2025-02-21 16:30:00", "%Y-%m-%d %H:%M:%S"), total_amount=1299.99, status=1, created_by=7),
]


order_items = [
    OrderItem(order_id=1, product_id=1, quantity=1, price=13999.99, status=1, created_by=1),
    OrderItem(order_id=1, product_id=2, quantity=1, price=58999.99, status=1, created_by=1),
    OrderItem(order_id=2, product_id=2, quantity=1, price=58999.99, status=1, created_by=2),
    OrderItem(order_id=3, product_id=3, quantity=1, price=799.99, status=1, created_by=3),
    OrderItem(order_id=4, product_id=6, quantity=1, price=499.00, status=1, created_by=4),
    OrderItem(order_id=5, product_id=7, quantity=1, price=4999.99, status=1, created_by=5),
    OrderItem(order_id=6, product_id=2, quantity=1, price=58999.99, status=1, created_by=6),
]
session.add_all(order_items)
session.add_all(orders)
session.add_all(products)
session.add_all(sub_categories)
session.add_all(main_categories)
session.add_all(user)
                
session.commit()