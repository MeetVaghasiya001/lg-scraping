from parser import *
from db import *


create_db()
all_products = get_all_varient('https://www.oppo.com/in/smartphones/')

for i in all_products:
    product_name = i.get('product')
    product_url = i.get('product_url')
    for v in i.get('varients'):
        varint_name = v.get('varient_name')
        sku = v.get('sku')
        sale_price = v.get('sale_price')
        original_price = v.get('original_price')
        now_price = v.get('now_price')
        color = v.get('color')
        storage = v.get('storage')
        stock = v.get('stock')


        data = (product_name,varint_name,sku,sale_price,original_price,now_price,color,storage,product_url,stock)
        insert_products(data)