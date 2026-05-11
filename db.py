import mysql.connector


def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="oppo"
    )

    cur = conn.cursor()

    return conn,cur 

def create_db():
    conn,cur = connection()
    cur.execute("""CREATE TABLE IF NOT EXISTS all_products(
                p_id INT AUTO_INCREMENT PRIMARY KEY,
                p_name VARCHAR(255),
                varient_name VARCHAR(255),
                sku VARCHAR(255),
                sale_price INT,
                original_price INT,
                now_price INT,
                color VARCHAR(255),
                storage VARCHAR(255),
                product_url TEXT,
                stock BOOl
            )
        """)
    conn.commit()
    conn.close()


def insert_products(data):
    conn,cur = connection()
    cur.execute("""
        INSERT INTO all_products(p_name,varient_name,sku,sale_price,original_price,now_price,color,storage,product_url,stock) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,data)
    conn.commit()
    conn.close()
