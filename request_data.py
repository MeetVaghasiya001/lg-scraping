import requests
import json
from lxml import html
import re
def request(url):
    cookies = {
        'otrack_jssdk_is_first_day': 'true',
        '_gcl_gs': '2.1.k1$i1778480109$u36156926',
        '_gcl_au': '1.1.2007190443.1778480111',
        '_ga': 'GA1.1.1002256372.1778480111',
        'source_param': 'google',
        'utm_source': 'google',
        'utm_medium': 'cpc',
        'utm_campaign': 'OPPO_PHD_India_English_FindX9_Ultra_Preheat_All_India_CPC_Product_KWs_20260507-20260514_Traffic_Conversion',
        '_twpid': 'tw.1778480112661.833194155251040154',
        '_hjSession_2052333': 'eyJpZCI6ImY3ZjY1MGI2LTQ4NzAtNDVlMS05MjUxLTBlOTg2ODA1ODc1YiIsImMiOjE3Nzg0ODAxMTI4MDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
        '_gcl_aw': 'GCL.1778480113.Cj0KCQjw2YDQBhD_ARIsAE1qeSeK8I0E8fXbYEprBs2Xhe06urZklfAsgpHwwGKIglcJEDJrS585KL4aAussEALw_wcB',
        '_fbp': 'fb.1.1778480113302.758858283128298394',
        'tfpsi': '80c62ee1-8b6c-4f73-9cc6-017478f5d516',
        '_clck': 'qfb0wl%5E2%5Eg5y%5E0%5E2322',
        '_hjSessionUser_2052333': 'eyJpZCI6ImRkMmUyOWEyLTQ1NTctNTk5Zi05OWU0LWM5ZTQzMTA0ZDUzOSIsImNyZWF0ZWQiOjE3Nzg0ODAxMTI4MDYsImV4aXN0aW5nIjp0cnVlfQ==',
        'cookiesaccepted': 'true',
        'otrack_jssdk_store_106002': 'eyJkZXZpY2VJZCI6ImE4Nzc1YjgzLTg0ZWYtNDVlYi1iNTQxLTNhYmVhYTk1NjMzYyIsInVzZXJJZCI6IiIsImN1c3RvbUF0dHJzIjp7InByb3BzIjp7fSwiaWRlbnRpdGllcyI6eyIkaWRlbnRpdHlfY29va2llX2lkIjoiYTg3NzViODMtODRlZi00NWViLWI1NDEtM2FiZWFhOTU2MzNjIiwiJGlkZW50aXR5X2Fub255bW91c19pZCI6ImE4Nzc1YjgzLTg0ZWYtNDVlYi1iNTQxLTNhYmVhYTk1NjMzYyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6ImE4Nzc1YjgzLTg0ZWYtNDVlYi1iNTQxLTNhYmVhYTk1NjMzYyJ9LCJsaWIiOnsiJGxpYiI6ImpzIiwiJGxpYl9tZXRob2QiOiJjb2RlIiwiJGxpYl92ZXJzaW9uIjoiMS4yNC42In0sImg1YXBwIjp7fX19',
        '_hjSession_2075538': 'eyJpZCI6Ijk5ZDY3YWRkLTYxNzctNDJjNy1iOGVhLTU4ZDAxNzU4ZGVjZiIsImMiOjE3Nzg0ODAxODI3NTAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
        'IR_gbd': 'oppo.com',
        '_ga_nefid_': '3m7Cp9FG7cdFVkFVBRLH%2BBdnjKL60pOv',
        '_hjSessionUser_2075538': 'eyJpZCI6IjRmNGU5ODlmLTJiOTktNTY1Yi1iNmI1LTFlMzljZDI2YjgzMCIsImNyZWF0ZWQiOjE3Nzg0ODAxODI3NDksImV4aXN0aW5nIjp0cnVlfQ==',
        'IR_15008': '1778480524340%7C0%7C1778480524340%7C%7C',
        'obus-track_106002_session': 'Z4MuGsoy,1778480110807,1778480612442',
        'WEBSITE_URL': 'https://www.oppo.com/in/smartphones/',
        '_ga_DTXFPC1MML': 'GS2.1.s1778480110$o1$g1$t1778480617$j55$l0$h0',
        'RT': '"z=1&dm=www.oppo.com&si=6a6d2479-fb80-4712-8359-5f60edd77664&ss=mp0t50lq&sl=6&tt=7kj&bcn=%2F%2F684d0d46.akstat.io%2F&obo=2&ld=avkb"',
        '_clsk': '13avn6w%5E1778480619015%5E8%5E1%5Ex.clarity.ms%2Fcollect',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.oppo.com/',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': 'otrack_jssdk_is_first_day=true; _gcl_gs=2.1.k1$i1778480109$u36156926; _gcl_au=1.1.2007190443.1778480111; _ga=GA1.1.1002256372.1778480111; source_param=google; utm_source=google; utm_medium=cpc; utm_campaign=OPPO_PHD_India_English_FindX9_Ultra_Preheat_All_India_CPC_Product_KWs_20260507-20260514_Traffic_Conversion; _twpid=tw.1778480112661.833194155251040154; _hjSession_2052333=eyJpZCI6ImY3ZjY1MGI2LTQ4NzAtNDVlMS05MjUxLTBlOTg2ODA1ODc1YiIsImMiOjE3Nzg0ODAxMTI4MDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _gcl_aw=GCL.1778480113.Cj0KCQjw2YDQBhD_ARIsAE1qeSeK8I0E8fXbYEprBs2Xhe06urZklfAsgpHwwGKIglcJEDJrS585KL4aAussEALw_wcB; _fbp=fb.1.1778480113302.758858283128298394; tfpsi=80c62ee1-8b6c-4f73-9cc6-017478f5d516; _clck=qfb0wl%5E2%5Eg5y%5E0%5E2322; _hjSessionUser_2052333=eyJpZCI6ImRkMmUyOWEyLTQ1NTctNTk5Zi05OWU0LWM5ZTQzMTA0ZDUzOSIsImNyZWF0ZWQiOjE3Nzg0ODAxMTI4MDYsImV4aXN0aW5nIjp0cnVlfQ==; cookiesaccepted=true; otrack_jssdk_store_106002=eyJkZXZpY2VJZCI6ImE4Nzc1YjgzLTg0ZWYtNDVlYi1iNTQxLTNhYmVhYTk1NjMzYyIsInVzZXJJZCI6IiIsImN1c3RvbUF0dHJzIjp7InByb3BzIjp7fSwiaWRlbnRpdGllcyI6eyIkaWRlbnRpdHlfY29va2llX2lkIjoiYTg3NzViODMtODRlZi00NWViLWI1NDEtM2FiZWFhOTU2MzNjIiwiJGlkZW50aXR5X2Fub255bW91c19pZCI6ImE4Nzc1YjgzLTg0ZWYtNDVlYi1iNTQxLTNhYmVhYTk1NjMzYyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6ImE4Nzc1YjgzLTg0ZWYtNDVlYi1iNTQxLTNhYmVhYTk1NjMzYyJ9LCJsaWIiOnsiJGxpYiI6ImpzIiwiJGxpYl9tZXRob2QiOiJjb2RlIiwiJGxpYl92ZXJzaW9uIjoiMS4yNC42In0sImg1YXBwIjp7fX19; _hjSession_2075538=eyJpZCI6Ijk5ZDY3YWRkLTYxNzctNDJjNy1iOGVhLTU4ZDAxNzU4ZGVjZiIsImMiOjE3Nzg0ODAxODI3NTAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; IR_gbd=oppo.com; _ga_nefid_=3m7Cp9FG7cdFVkFVBRLH%2BBdnjKL60pOv; _hjSessionUser_2075538=eyJpZCI6IjRmNGU5ODlmLTJiOTktNTY1Yi1iNmI1LTFlMzljZDI2YjgzMCIsImNyZWF0ZWQiOjE3Nzg0ODAxODI3NDksImV4aXN0aW5nIjp0cnVlfQ==; IR_15008=1778480524340%7C0%7C1778480524340%7C%7C; obus-track_106002_session=Z4MuGsoy,1778480110807,1778480612442; WEBSITE_URL=https://www.oppo.com/in/smartphones/; _ga_DTXFPC1MML=GS2.1.s1778480110$o1$g1$t1778480617$j55$l0$h0; RT="z=1&dm=www.oppo.com&si=6a6d2479-fb80-4712-8359-5f60edd77664&ss=mp0t50lq&sl=6&tt=7kj&bcn=%2F%2F684d0d46.akstat.io%2F&obo=2&ld=avkb"; _clsk=13avn6w%5E1778480619015%5E8%5E1%5Ex.clarity.ms%2Fcollect',
    }

    response = requests.get(url, cookies=cookies, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)
        print(response.text)
        return None










def price_request(json_data):
    cookies = {
        'frontend': '662edb398ae0477da20efccf96a4864e',
        '_gcl_gs': '2.1.k1$i1778480109$u36156926',
        '_gcl_au': '1.1.2007190443.1778480111',
        '_ga': 'GA1.1.1002256372.1778480111',
        'source_param': 'google',
        'utm_source': 'google',
        'utm_medium': 'cpc',
        'utm_campaign': 'OPPO_PHD_India_English_FindX9_Ultra_Preheat_All_India_CPC_Product_KWs_20260507-20260514_Traffic_Conversion',
        '_twpid': 'tw.1778480112661.833194155251040154',
        '_hjSession_2052333': 'eyJpZCI6ImY3ZjY1MGI2LTQ4NzAtNDVlMS05MjUxLTBlOTg2ODA1ODc1YiIsImMiOjE3Nzg0ODAxMTI4MDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
        '_gcl_aw': 'GCL.1778480113.Cj0KCQjw2YDQBhD_ARIsAE1qeSeK8I0E8fXbYEprBs2Xhe06urZklfAsgpHwwGKIglcJEDJrS585KL4aAussEALw_wcB',
        '_fbp': 'fb.1.1778480113302.758858283128298394',
        'tfpsi': '80c62ee1-8b6c-4f73-9cc6-017478f5d516',
        '_clck': 'qfb0wl%5E2%5Eg5y%5E0%5E2322',
        '_hjSessionUser_2052333': 'eyJpZCI6ImRkMmUyOWEyLTQ1NTctNTk5Zi05OWU0LWM5ZTQzMTA0ZDUzOSIsImNyZWF0ZWQiOjE3Nzg0ODAxMTI4MDYsImV4aXN0aW5nIjp0cnVlfQ==',
        'cookiesaccepted': 'true',
        '_hjSession_2075538': 'eyJpZCI6Ijk5ZDY3YWRkLTYxNzctNDJjNy1iOGVhLTU4ZDAxNzU4ZGVjZiIsImMiOjE3Nzg0ODAxODI3NTAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
        'IR_gbd': 'oppo.com',
        '_hjSessionUser_2075538': 'eyJpZCI6IjRmNGU5ODlmLTJiOTktNTY1Yi1iNmI1LTFlMzljZDI2YjgzMCIsImNyZWF0ZWQiOjE3Nzg0ODAxODI3NDksImV4aXN0aW5nIjp0cnVlfQ==',
        'WEBSITE_URL': 'https://www.oppo.com/in/product/oppo-reno14-5g.P.P1110071',
        'IR_15008': '1778480244430%7C0%7C1778480244430%7C%7C',
        '_clsk': '13avn6w%5E1778480258236%5E4%5E1%5Ex.clarity.ms%2Fcollect',
        '_ga_DTXFPC1MML': 'GS2.1.s1778480110$o1$g1$t1778480267$j34$l0$h0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.oppo.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.oppo.com/',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': 'frontend=662edb398ae0477da20efccf96a4864e; _gcl_gs=2.1.k1$i1778480109$u36156926; _gcl_au=1.1.2007190443.1778480111; _ga=GA1.1.1002256372.1778480111; source_param=google; utm_source=google; utm_medium=cpc; utm_campaign=OPPO_PHD_India_English_FindX9_Ultra_Preheat_All_India_CPC_Product_KWs_20260507-20260514_Traffic_Conversion; _twpid=tw.1778480112661.833194155251040154; _hjSession_2052333=eyJpZCI6ImY3ZjY1MGI2LTQ4NzAtNDVlMS05MjUxLTBlOTg2ODA1ODc1YiIsImMiOjE3Nzg0ODAxMTI4MDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _gcl_aw=GCL.1778480113.Cj0KCQjw2YDQBhD_ARIsAE1qeSeK8I0E8fXbYEprBs2Xhe06urZklfAsgpHwwGKIglcJEDJrS585KL4aAussEALw_wcB; _fbp=fb.1.1778480113302.758858283128298394; tfpsi=80c62ee1-8b6c-4f73-9cc6-017478f5d516; _clck=qfb0wl%5E2%5Eg5y%5E0%5E2322; _hjSessionUser_2052333=eyJpZCI6ImRkMmUyOWEyLTQ1NTctNTk5Zi05OWU0LWM5ZTQzMTA0ZDUzOSIsImNyZWF0ZWQiOjE3Nzg0ODAxMTI4MDYsImV4aXN0aW5nIjp0cnVlfQ==; cookiesaccepted=true; _hjSession_2075538=eyJpZCI6Ijk5ZDY3YWRkLTYxNzctNDJjNy1iOGVhLTU4ZDAxNzU4ZGVjZiIsImMiOjE3Nzg0ODAxODI3NTAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; IR_gbd=oppo.com; _hjSessionUser_2075538=eyJpZCI6IjRmNGU5ODlmLTJiOTktNTY1Yi1iNmI1LTFlMzljZDI2YjgzMCIsImNyZWF0ZWQiOjE3Nzg0ODAxODI3NDksImV4aXN0aW5nIjp0cnVlfQ==; WEBSITE_URL=https://www.oppo.com/in/product/oppo-reno14-5g.P.P1110071; IR_15008=1778480244430%7C0%7C1778480244430%7C%7C; _clsk=13avn6w%5E1778480258236%5E4%5E1%5Ex.clarity.ms%2Fcollect; _ga_DTXFPC1MML=GS2.1.s1778480110$o1$g1$t1778480267$j34$l0$h0',
    }

    
    response = requests.post(
        'https://opsg-gateway-in.oppo.com/v2/api/rest/mall/product/page/list/price',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        print(response.json())
        return None

