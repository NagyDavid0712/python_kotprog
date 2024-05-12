import sqlite3
from app.entity import Product

class ProductHandler:

    _instance = None

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls._instance = super(ProductHandler, cls).__new__(cls)
            cls.arr_of_products = []
        return cls._instance
    
    def __init__(self):
        self.conn = sqlite3.connect("app/databases/ricerpower.db")
        self.read_products()

    def read_products(self):
        
        cursor = self.conn.execute("SELECT * FROM products")
        for row in cursor:
            p = Product.Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            self.arr_of_products.append(p)
        
    def get_products(self):
        return self.arr_of_products

    def find_product_by_id(self, pid):
        for e in self.arr_of_products:
            if e.id == int(pid):
                return e    
        return None
 
    """
    def filter_products(self, filter_options):
        er = []
        for v in self.arr_of_products:
            if v.engine_type == filter_options["engine_code"] and v not in er:
                er.append(v)
            if v.main_category == filter_options["engine_main_part"] and v not in er:
                er.append(v)
            if v.category == filter_options["engine_part"] and v not in er:
                er.append(v)
        return er
    """
        
    def get_reviews_for_product(self, id):
        cursor = self.conn.cursor()
        sql = "SELECT reviewWriter, rating, reviewText FROM reviews INNER JOIN products ON products.id = reviews.part_id WHERE products.id = " + id
        cursor.execute(sql)
        res = cursor.fetchall()
        print(len(res))
        if(len(res) == 0):
            return None
        
        p = []

        for r in res:
            c = ""
            if int(r[1]) >= 0 and int(r[1]) <= 2:
                c = "bad"
            elif int(r[1]) >= 3 and int(r[1]) <= 4:
                c = "notgreat"
            elif int(r[1]) >= 5 and int(r[1]) <= 6:
                c = "mid"
            elif int(r[1]) >= 7 and int(r[1]) <= 8:
                c = "good"
            else:
                c = "great"
            
            p.append({
                "reviewWriter" : r[0],
                "rating" : r[1],
                "reviewText" : r[2],
                "class" : c
            })

        return p
    
    def add_review_for_product(self, rev):
        cursor = self.conn.cursor()

        cursor.execute("INSERT INTO reviews (part_id, reviewWriter, rating, reviewText) VALUES (?, ?, ?, ?)", (rev["part_id"], rev["reviewWriter"], rev["rating"], rev["reviewText"]))

        self.conn.commit()

        pass