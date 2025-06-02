
from sqlalchemy import create_engine,text,Column,Integer,String,Text,ForeignKey,DateTime,DECIMAL,func
from sqlalchemy.orm import declarative_base,relationship
from datetime import datetime


db_url="mysql+pymysql://root:2741@localhost:3307/ecommerce"
engine=create_engine(db_url)
Base = declarative_base()




class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_type = Column(Integer, nullable=False)  # 1 = vendor, 2 = buyer, 3 = admin
    status = Column(Integer, default=1)  # 1 = active, 2 = inactive, -1 = deleted
    created_by = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    created_at = Column(DateTime,  server_default=func.now())

    created_main_categories = relationship('MainCategory', back_populates='creator', foreign_keys='MainCategory.created_by')
    created_sub_categories = relationship('SubCategory', back_populates='creator', foreign_keys='SubCategory.created_by')
    products = relationship('Product', back_populates='vendor', foreign_keys='Product.vendor_id')
    created_products = relationship('Product', back_populates='creator', foreign_keys='Product.created_by')
    orders = relationship('Order', back_populates='buyer', foreign_keys='Order.buyer_id')
    created_orders = relationship('Order', back_populates='creator', foreign_keys='Order.created_by')
    created_order_items = relationship('OrderItem', back_populates='creator', foreign_keys='OrderItem.created_by')


class MainCategory(Base):
    __tablename__ = 'main_categories'

    main_category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    status = Column(Integer, default=1)  # 1 = active, 2 = inactive, -1 = deleted
    created_by = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    created_at = Column(DateTime,  server_default=func.now())

    creator = relationship('User', back_populates='created_main_categories', foreign_keys=[created_by])
    sub_categories = relationship('SubCategory', back_populates='main_category')


class SubCategory(Base):
    __tablename__ = 'sub_categories'

    sub_category_id = Column(Integer, primary_key=True, autoincrement=True)
    main_category_id = Column(Integer, ForeignKey('main_categories.main_category_id'), nullable=False)
    name = Column(String(100), nullable=False)
    status = Column(Integer, default=1)  # 1 = active, 2 = inactive, -1 = deleted
    created_by = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    created_at = Column(DateTime,  server_default=func.now())

    main_category = relationship('MainCategory', back_populates='sub_categories')
    creator = relationship('User', back_populates='created_sub_categories', foreign_keys=[created_by])
    products = relationship('Product', back_populates='sub_category')


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    sub_category_id = Column(Integer, ForeignKey('sub_categories.sub_category_id'), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, default=0)
    status = Column(Integer, default=1)  # 1 = active, 2 = inactive, -1 = deleted
    created_by = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    created_at = Column(DateTime,  server_default=func.now())

    vendor = relationship('User', back_populates='products', foreign_keys=[vendor_id])
    sub_category = relationship('SubCategory', back_populates='products')
    creator = relationship('User', back_populates='created_products', foreign_keys=[created_by])
    order_items = relationship('OrderItem', back_populates='product')


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    buyer_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    order_date = Column(DateTime, server_default=func.now())
    total_amount = Column(DECIMAL(10, 2), nullable=True)
    status = Column(Integer, default=1)  # 1 = active, 2 = inactive, -1 = deleted
    created_by = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    buyer = relationship('User', back_populates='orders', foreign_keys=[buyer_id])
    creator = relationship('User', back_populates='created_orders', foreign_keys=[created_by])
    order_items = relationship('OrderItem', back_populates='order')


class OrderItem(Base):
    __tablename__ = 'order_items'

    order_item_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Integer, default=1)  # 1 = active, 2 = inactive, -1 = deleted
    created_by = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    created_at = Column(DateTime,  server_default=func.now())

    order = relationship('Order', back_populates='order_items')
    product = relationship('Product', back_populates='order_items')
    creator = relationship('User', back_populates='created_order_items', foreign_keys=[created_by])
    
Base.metadata.create_all(engine)