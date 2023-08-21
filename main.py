from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class product(Base):
    __tablename__ = "products"

    item = Column("item",Integer,primary_key = True)
    productname = Column("productname",String)
    quantity = Column("quantity",Integer)

    def __init__(self,item,name,quantity):
        self.item = item
        self.productname = name
        self.quantity = quantity

    def __repr__(self):
        return f"({self.item},{self.productname},{self.quantity})"

engine = create_engine("sqlite:///Grocery.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

Product = product(1,"Lays",10)
session.add(Product)
session.commit()

p1=product(2,"ice-cream",5)
p2=product(3,"Jam",1)

session.add(p1)
session.add(p2)
session.commit()

results = session.query(product).all()
print(results)
