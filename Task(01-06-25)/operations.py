from models import engine,User,Product,Order,OrderItem,MainCategory,SubCategory
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc,extract
from datetime import datetime, timedelta, timezone



Session=sessionmaker(bind=engine)
session=Session()


def top():
    top_products = (session.query(Product.product_id,Product.name,func.sum(OrderItem.quantity).label("total_quantity_sold")).join(OrderItem, Product.product_id == OrderItem.product_id).group_by(Product.product_id).order_by(desc("total_quantity_sold")).limit(5).all())
    print("Top 5 best-selling products:")
    for prod in top_products:
        print(f"Product ID: {prod.product_id} Name: {prod.name} Quantity Sold: {prod.total_quantity_sold}")

def month():
    monthly_revenue = (session.query(extract('year', Order.order_date).label('year'),extract('month', Order.order_date).label('month'),func.sum(Order.total_amount).label('total_revenue')).filter(Order.order_date >= 180).group_by(extract('year', Order.order_date),extract('month', Order.order_date)).order_by(extract('year', Order.order_date),extract('month', Order.order_date)).all())
    print("\nTotal revenue per month (last 6 months):")
    for year, month, revenue in monthly_revenue:
        print(f"{int(year)}-{int(month):02d}: ${revenue:.2f}")

def vendor():
    top_vendors = (session.query(User.user_id,User.username,func.count(Product.product_id).label('product_count')).join(Product, User.user_id == Product.vendor_id).group_by(User.user_id).order_by(desc('product_count')).all())
    print("\nVendors with the most products listed:")
    for vendor in top_vendors:
        print(f"User ID: {vendor.user_id} Username: {vendor.username} Products Listed: {vendor.product_count}")


def low_stock():
    low_stock_products = (session.query(Product).filter(Product.stock < 10).order_by(Product.stock).all())
    print("\nLow stock products less than 10:")
    for p in low_stock_products:
        print(f"Product ID: {p.product_id} Name: {p.name} Stock: {p.stock}")


def average_ord():
    avg_order_value = (session.query(User.user_id,User.username,func.avg(Order.total_amount).label('average_order_value')).join(Order, User.user_id == Order.buyer_id).group_by(User.user_id).all())
    print("\nAverage order value per buyer:")
    for user_id, username, avg_val in avg_order_value:
        print(f"User ID: {user_id} Username: {username} Average Order Value: ${avg_val:.2f}")

def product_count():
    category_product_count = (session.query(MainCategory.main_category_id,MainCategory.name,func.count(Product.product_id).label('total_products')).join(SubCategory, SubCategory.main_category_id == MainCategory.main_category_id).join(Product, Product.sub_category_id == SubCategory.sub_category_id).group_by(MainCategory.main_category_id).all())
    print("\nCategory-wise total product count:")
    for cat_id, cat_name, total in category_product_count:
        print(f"Category ID: {cat_id} Name: {cat_name}, Total Products: {total}")


def top_buyers():
    top_buyers = (session.query(User.user_id,User.username,func.sum(Order.total_amount).label('total_spent')).join(Order, User.user_id == Order.buyer_id).group_by(User.user_id).order_by(desc('total_spent')).limit(3).all())
    print("\nTop 3 buyers by total spendimg:")
    for buyer in top_buyers:
        print(f"User ID: {buyer.user_id} Username: {buyer.username} Total Spent: ${buyer.total_spent:.2f}")

def daily_ord_count():
    now1=datetime.now(timezone.utc)
    startweek=timedelta(days=datetime.now().weekday())
    startweek1 = (now1 - startweek).replace(hour=0, minute=0, second=0, microsecond=0)
    daily_order_count = (session.query(func.date(Order.order_date).label('order_date'),func.count(Order.order_id).label('order_count')).filter(Order.order_date >= startweek1).group_by(func.date(Order.order_date)).order_by(func.date(Order.order_date)).all())
    print("\nDaily order count for the current week:")
    for order_date, count in daily_order_count:
        print(f"{order_date}: {count} orders")




