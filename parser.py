from request_data import *
import gzip

def all_phones(url):
    data = request(url)
    tree = html.fromstring(data)
    s = tree.xpath("//script[contains(.,'window.pageDsl')]/text()")[0]

    i = s.find("{", s.find("window.pageDsl"))
    c = 0

    for j in range(i, len(s)):
        if s[j] == "{": c += 1
        elif s[j] == "}":
            c -= 1
            if c == 0:
                data2 = json.loads(s[i:j+1])
                return data2


def key_finder(data, key):
    res = []

    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                res.append(v)
            res.extend(key_finder(v, key))

    elif isinstance(data, list):
        for item in data:
            res.extend(key_finder(item, key))

    return res
                





def get_all_id(url):
    product=[]
    data = all_phones(url)
    all_product = key_finder(data,'productItem')
    for i in all_product:
        for j in i:
            product.append({
                'phone_name':j.get('productName'),
                'spu':j.get('spu'),
                'url':j.get('buyButtonLink') if j.get('buyButtonLink') else j.get('learnMoreButtonLink')
            })

    return product


def add_page_save(page):
    folder_path = 'C:/Users/meet.vaghasiya/Desktop/bif files/oppo'

    with gzip.open(f'{folder_path}/price.json.gz','wt',encoding='utf-8') as f:
        json.dump(page,f,indent=4,default=str)

def get_all_varient(url):
    all_products = []
    data = get_all_id(url)
    all_id = [i.get('spu') for i in data]
    json_data = {
        'productCodes':all_id,
        'storeViewCode': 'in',
        'countryCode': 'IN',
        'deviceType': 4,
        'needPre': True,
    }

    respoce = price_request(json_data)
    add_page_save(respoce)
    if respoce.get('data'):
        for i in respoce.get('data'):
            all_products.append({
                'product':i.get('productName'),
                'product_url':i.get('productDetailUrl'),
                'varients':[{
                    'varient_name':v.get('skuName'),
                    'sku':v.get('skuCode'),
                    'sale_price':v.get('salePrice'),
                    'original_price':v.get('originalPrice'),
                    'now_price':v.get('nowPrice'),
                    'color':v.get('color').get('optLabel'),
                    'storage':v.get('rom').get('optLabel'),
                    'stock':v.get('hasStock')
                } for v in i.get('skuList')]
            })

            print('='*30)
            print(f'{i.get('productName')} was process!')
                    
        return all_products
        
    else:
        print('Not ok')
        return None






