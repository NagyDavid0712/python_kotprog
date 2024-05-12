import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from app.entity import User

class UsersHandle:
    _instance = None
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls._instance = super(UsersHandle, cls).__new__(cls)
        return cls._instance
    
    def find_user(self, username, password):
        conn = sqlite3.connect("app/databases/ricerpower.db")
        res = conn.execute("SELECT * FROM users")
        for r in res:
            #print(r)
            if r[5] == username and check_password_hash(r[6], password):
                user = User.User(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
                return user
        conn.close()
        return None

    def add_user(self, user_dict):
        conn = sqlite3.connect("app/databases/ricerpower.db")
        cursor = conn.cursor()

        try:
            sql = "INSERT INTO users (cs_nev, k_nev, szul_d, fel_h, jelszo, email, nem, prof_pic_loc) VALUES (?,?,?,?,?,?,?,?)"
            pw_hash = generate_password_hash(user_dict["reg_password"])
            cursor.execute(sql, (user_dict["reg_firstname"], user_dict["reg_lastname"], user_dict["reg_date"], user_dict["reg_name"], pw_hash, user_dict["reg_email"], user_dict["reg_gender"], "img/user/default_user.png"))
            conn.commit()
            #print("asd")
        except sqlite3.Error as e:
            #print("Nem sikerült beszúrni", e.sqlite_errorcode)
            conn.rollback()
            return False
        conn.close()
        return True
    
    """
    def update_prof_pic(self, npp):
        fname = npp.filename
        nw = session["user"]["felh_n"]
        print(fname)
        npp.save(os.path.join("../../static/img/user/", fname))
        #os.rename(os.path.join(app.config["UPLOAD_FOLDER"], fname), os.path.join(app.config["UPLOAD_FOLDER"], nw))
        
        conn = sqlite3.connect("app/databases/ricerpower.db")
        cursor = conn.cursor()

        #cursor.execute("UPDATE users SET prof_pic_loc = ? WHERE id = ?", (fname, session["user"]["id"]))
        #conn.commit()
    """
        
    def update_password(self, p, felh): 
        conn = sqlite3.connect("app/databases/ricerpower.db")
        cursor = conn.cursor()

        pw_hash = generate_password_hash(p)

        try:
            sql = "UPDATE users SET jelszo = ? WHERE fel_h = ?"
            cursor.execute(sql, (pw_hash, felh))
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            conn.close()
            return False
        
        conn.close()
        return True

    def get_user_reviews(self, felh_n):
        conn = sqlite3.connect("app/databases/ricerpower.db")
        cursor = conn.cursor()
        #print(felh_n)
        sql = "SELECT rating, reviewText, products.product_title AS product FROM reviews INNER JOIN products ON products.id = reviews.part_id WHERE reviewWriter = '" + felh_n + "'"
        cursor.execute(sql)
        
        res = cursor.fetchall()
        #print(len(res))
        if(len(res) == 0):
            return None
        
        p = []

        for r in res:
            c = ""
            if int(r[0]) >= 0 and int(r[0]) <= 2:
                c = "bad"
            elif int(r[0]) >= 3 and int(r[0]) <= 4:
                c = "notgreat"
            elif int(r[0]) >= 5 and int(r[0]) <= 6:
                c = "mid"
            elif int(r[0]) >= 7 and int(r[0]) <= 8:
                c = "good"
            else:
                c = "great"
            
            p.append({
                "product" : r[2],
                "rating" : r[0],
                "reviewText" : r[1],
                "class" : c
            })

        conn.close()
        return p