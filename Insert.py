import MySQLdb
def insert(r1, r2, r3, b1, b2, b3, y1, y2, y3):
    db = MySQLdb.connect("localhost", "root", "universe", "products")
    cursor = db.cursor()
    sql = "insert into product values (%d,%d,%d,%d,%d,%d,%d,%d,%d)" % (r1,r2,r3,b1,b2,b3,y1,y2,y3)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def delete_all():
    db = MySQLdb.connect("localhost", "root", "universe", "products")
    cursor = db.cursor()
    sql = "delete from product"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

delete_all()
