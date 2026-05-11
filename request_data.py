import requests
import json

def request(url):
    cookies = {
        'coveo-search-token': 'eyJhbGciOiJIUzI1NiJ9.eyJ2OCI6dHJ1ZSwiZW5mb3JjZWREaWN0aW9uYXJ5RmllbGRDb250ZXh0Ijp7ImVjX2Rpc2NvdW50X3JhdGUiOiJOT1RfTE9HR0VEX0lOIiwiZWNfZ3Vlc3RfcHJpY2UiOiJOT1RfTE9HR0VEX0lOIiwiZWNfY2hlYXBlcl9wcmljZSI6Ik5PVF9MT0dHRURfSU4iLCJlY19kaXNjb3VudF9yYXRlX2RlY2ltYWwiOiJOT1RfTE9HR0VEX0lOIiwiZWNfZGlzY291bnRfdG9vbHRpcCI6Ik5PVF9MT0dHRURfSU4iLCJlY19vcmlnaW5hbF9wcmljZSI6Ik5PVF9MT0dHRURfSU4iLCJlY19pbnRyb190ZXh0IjoiTk9UX0xPR0dFRF9JTiIsImVjX3ByaWNlIjoiTk9UX0xPR0dFRF9JTiIsImVjX2Zsb2Ffb2ZmZXJzX29mZmVycyI6Ik5PVF9MT0dHRURfSU4iLCJlY19kaXNjb3VudF9hbW91bnQiOiJOT1RfTE9HR0VEX0lOIiwiZWNfZmxvYV9vZmZlcnNfYW1vdW50IjoiTk9UX0xPR0dFRF9JTiJ9LCJ0b2tlbklkIjoicWxxN2FmcXNrcmliZHRkc3VocmFod2NncnkiLCJvcmdhbml6YXRpb24iOiJsZ2NvcnBvcmF0aW9ucHJvZHVjdGlvbjBmeGN1MHF4IiwidXNlcklkcyI6W3sidHlwZSI6IlVzZXIiLCJuYW1lIjoiYW5vbnltb3VzIiwicHJvdmlkZXIiOiJFbWFpbCBTZWN1cml0eSBQcm92aWRlciJ9XSwicm9sZXMiOlsicXVlcnlFeGVjdXRvciJdLCJpc3MiOiJTZWFyY2hBcGkiLCJleHAiOjE3NzgzNDIyNjQsImlhdCI6MTc3ODI1NTg2NH0.u94RDBDsb8zu3MPI_3xxtyQhEVIVDm13AxFipfDj8HE',
        'AMCV_91F51CFE532954550A490D45%40AdobeOrg': '179643557%7CMCIDTS%7C20582%7CMCMID%7C01557881007721027582618519901383424257%7CMCAAMLH-1778860664%7C12%7CMCAAMB-1778860664%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1778263064s%7CNONE%7CvVersion%7C5.5.0',
        'whatap_user_id_45677': 'x4r96paqapsef3',
        'coveo_visitorId': '8c25ec77-afb1-4247-ad02-ad2305b044b5',
        '_ga': 'GA1.1.867040899.1778255866',
        '_sfid_b182': '{%22anonymousId%22:%225a0e04226b778bdd%22%2C%22consents%22:[{%22consent%22:{%22provider%22:%22Web%20Provider%22%2C%22purpose%22:%22Tracking%22%2C%22status%22:%22Opt%20In%22}%2C%22lastUpdateTime%22:%222026-05-08T15:57:46.005Z%22}]}',
        'BVBRANDID': '484a2c13-4a8c-4827-b3fd-36f246c88019',
        '_fbp': 'fb.1.1778255866170.196815818797123762',
        '_gcl_au': '1.1.773041223.1778255866',
        '__qca': 'P1-9d93359f-1c28-4dfa-831a-f84d5ec745f9',
        'GLOBAL_LGCOM_ANALYSIS_OF_SITE': 'Y',
        'GLOBAL_LGCOM_IMPROVEMENTS': 'Y',
        'GLOBAL_LGCOM_ADVERTISING': 'Y',
        '_ga_V4TNXPS4SD': 'GS2.1.s1778256066$o1$g0$t1778256071$j55$l0$h31134871',
        'AT_LGCOM_ANALYSIS_OF_SITE': 'Y',
        'AT_LGCOM_IMPROVEMENTS': 'Y',
        'AT_LGCOM_ADVERTISING': 'Y',
        'cf_72097_id': 'bc20ba66-a67f-4c8b-a70c-55ef0bd074d8',
        'cf_72097_first_touch': '%7B%22landing_page%22%3A%22https%3A//www.lg.com/at/wireless-earbuds/tone-free/%22%2C%22timestamp%22%3A1778256160256%7D',
        '_ga_HQ6Q0FMGPW': 'GS2.1.s1778256157$o1$g1$t1778256169$j48$l0$h1919158612',
        'AKA_A2': 'A',
        'whatap_session_id_45677': 'z117hpu3mceqjn',
        'whatap_session_max_expired_45677': 'Sat, 09 May 2026 16:24:56 GMT',
        'whatap_session_collect_type_45677': '0',
        'at_check': 'true',
        '_gcl_gs': '2.1.k1$i1778329494$u144366120',
        'BVBRANDSID': '3f3dcf34-7dc0-48f2-b91c-633b369c5188',
        'FPGSID': '1.1778329497.1778329497.G-L4KSHMGE1T.PWOlmcOM0m5lLkAHxZDiXw',
        '_clck': '19z1dss%5E2%5Eg5w%5E0%5E2319',
        '_tt_enable_cookie': '1',
        '_ttp': '01KR6B5EKSQRZK402Z4JCD6532_.tt.1',
        'at_plplistclick': 'no',
        '_gcl_aw': 'GCL.1778329523.CjwKCAjwtvvPBhBuEiwAPMijrwmAexC5tNJAURlMgMPkdQXzsmPtpfJ6zYRoOgjA9hJyVD5zvQBuBxoC8zwQAvD_BwE',
        'mbox': 'PC#6d09f098fa7a4527a71673dd0f9ebb40.41_0#1841574325|session#c3bda8dc1b1143d5a760ecf4791c8689#1778331385',
        '_ga_L4KSHMGE1T': 'GS2.1.s1778329498$o2$g1$t1778329526$j32$l0$h803231252',
        '_uetsid': 'a7d205304af611f1b4b27767b5b745e1',
        '_uetvid': 'a7d218804af611f1aa6fb34b794a0082',
        '_clsk': 'chuj4j%5E1778329529503%5E3%5E1%5Ez.clarity.ms%2Fcollect',
        'cto_bundle': '6NnOqF9LSkpRUGFRYmszRFRVUCUyQjhSTzJmJTJCNDljS2JVUjZCajR6ZUh2JTJCTVNUQVNxQk1LaDFLbVVLcU1uYVJGUTlQd25wTEp1TzdNQ2QyYjkxdWJzcWxoSTglMkJyUjdNZ3ZpdiUyQmg3N3RaeTRhdWZxSXJqMmN1Qkx3QUpkZjZQbTN4ZGN2TXRxUlB5TVR0ZVZoeTM0ZHglMkZ5WDNYdmclM0QlM0Q',
        'RT': '"z=1&dm=lg.com&si=0dc8b910-38ea-450d-ba93-53f1ce63a21c&ss=moybgrkm&sl=3&tt=kw4&bcn=%2F%2F684d0d47.akstat.io%2F&ld=sks"',
        'ttcsid': '1778329500291::6xtE-ktSPvaCyBRzgFCU.1.1778329533371.0::1.17117.27443::1623.1.82.92::742.2.0',
        'ttcsid_CUGNBCRC77U27ULH3T3G': '1778329500290::1ASTjYL3BKBzJM-85FLp.1.1778329533371.1',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.lg.com/in/promotions/tvs-offers/?utm_source=google&utm_medium=cpc&utm_campaign=%7Bcampaign.id%7D&utm_id=20564378379&utm_term=Feb_Phase_2&utm_content=New+Beginnings&utm_adgroup=%7Badgroup.id%7D&utm_ad=%7Bcreative.id%7D&utm_placement=&utm_device=c&utm_matchtype=&utm_adposition=&utm_network=x&gad_source=1&gad_campaignid=21498794854&gbraid=0AAAAABxEkUSwA6lwGNz7R4Wq5RyJK2pf2&gclid=CjwKCAjwtvvPBhBuEiwAPMijrwmAexC5tNJAURlMgMPkdQXzsmPtpfJ6zYRoOgjA9hJyVD5zvQBuBxoC8zwQAvD_BwE',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': 'coveo-search-token=eyJhbGciOiJIUzI1NiJ9.eyJ2OCI6dHJ1ZSwiZW5mb3JjZWREaWN0aW9uYXJ5RmllbGRDb250ZXh0Ijp7ImVjX2Rpc2NvdW50X3JhdGUiOiJOT1RfTE9HR0VEX0lOIiwiZWNfZ3Vlc3RfcHJpY2UiOiJOT1RfTE9HR0VEX0lOIiwiZWNfY2hlYXBlcl9wcmljZSI6Ik5PVF9MT0dHRURfSU4iLCJlY19kaXNjb3VudF9yYXRlX2RlY2ltYWwiOiJOT1RfTE9HR0VEX0lOIiwiZWNfZGlzY291bnRfdG9vbHRpcCI6Ik5PVF9MT0dHRURfSU4iLCJlY19vcmlnaW5hbF9wcmljZSI6Ik5PVF9MT0dHRURfSU4iLCJlY19pbnRyb190ZXh0IjoiTk9UX0xPR0dFRF9JTiIsImVjX3ByaWNlIjoiTk9UX0xPR0dFRF9JTiIsImVjX2Zsb2Ffb2ZmZXJzX29mZmVycyI6Ik5PVF9MT0dHRURfSU4iLCJlY19kaXNjb3VudF9hbW91bnQiOiJOT1RfTE9HR0VEX0lOIiwiZWNfZmxvYV9vZmZlcnNfYW1vdW50IjoiTk9UX0xPR0dFRF9JTiJ9LCJ0b2tlbklkIjoicWxxN2FmcXNrcmliZHRkc3VocmFod2NncnkiLCJvcmdhbml6YXRpb24iOiJsZ2NvcnBvcmF0aW9ucHJvZHVjdGlvbjBmeGN1MHF4IiwidXNlcklkcyI6W3sidHlwZSI6IlVzZXIiLCJuYW1lIjoiYW5vbnltb3VzIiwicHJvdmlkZXIiOiJFbWFpbCBTZWN1cml0eSBQcm92aWRlciJ9XSwicm9sZXMiOlsicXVlcnlFeGVjdXRvciJdLCJpc3MiOiJTZWFyY2hBcGkiLCJleHAiOjE3NzgzNDIyNjQsImlhdCI6MTc3ODI1NTg2NH0.u94RDBDsb8zu3MPI_3xxtyQhEVIVDm13AxFipfDj8HE; AMCV_91F51CFE532954550A490D45%40AdobeOrg=179643557%7CMCIDTS%7C20582%7CMCMID%7C01557881007721027582618519901383424257%7CMCAAMLH-1778860664%7C12%7CMCAAMB-1778860664%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1778263064s%7CNONE%7CvVersion%7C5.5.0; whatap_user_id_45677=x4r96paqapsef3; coveo_visitorId=8c25ec77-afb1-4247-ad02-ad2305b044b5; _ga=GA1.1.867040899.1778255866; _sfid_b182={%22anonymousId%22:%225a0e04226b778bdd%22%2C%22consents%22:[{%22consent%22:{%22provider%22:%22Web%20Provider%22%2C%22purpose%22:%22Tracking%22%2C%22status%22:%22Opt%20In%22}%2C%22lastUpdateTime%22:%222026-05-08T15:57:46.005Z%22}]}; BVBRANDID=484a2c13-4a8c-4827-b3fd-36f246c88019; _fbp=fb.1.1778255866170.196815818797123762; _gcl_au=1.1.773041223.1778255866; __qca=P1-9d93359f-1c28-4dfa-831a-f84d5ec745f9; GLOBAL_LGCOM_ANALYSIS_OF_SITE=Y; GLOBAL_LGCOM_IMPROVEMENTS=Y; GLOBAL_LGCOM_ADVERTISING=Y; _ga_V4TNXPS4SD=GS2.1.s1778256066$o1$g0$t1778256071$j55$l0$h31134871; AT_LGCOM_ANALYSIS_OF_SITE=Y; AT_LGCOM_IMPROVEMENTS=Y; AT_LGCOM_ADVERTISING=Y; cf_72097_id=bc20ba66-a67f-4c8b-a70c-55ef0bd074d8; cf_72097_first_touch=%7B%22landing_page%22%3A%22https%3A//www.lg.com/at/wireless-earbuds/tone-free/%22%2C%22timestamp%22%3A1778256160256%7D; _ga_HQ6Q0FMGPW=GS2.1.s1778256157$o1$g1$t1778256169$j48$l0$h1919158612; AKA_A2=A; whatap_session_id_45677=z117hpu3mceqjn; whatap_session_max_expired_45677=Sat, 09 May 2026 16:24:56 GMT; whatap_session_collect_type_45677=0; at_check=true; _gcl_gs=2.1.k1$i1778329494$u144366120; BVBRANDSID=3f3dcf34-7dc0-48f2-b91c-633b369c5188; FPGSID=1.1778329497.1778329497.G-L4KSHMGE1T.PWOlmcOM0m5lLkAHxZDiXw; _clck=19z1dss%5E2%5Eg5w%5E0%5E2319; _tt_enable_cookie=1; _ttp=01KR6B5EKSQRZK402Z4JCD6532_.tt.1; at_plplistclick=no; _gcl_aw=GCL.1778329523.CjwKCAjwtvvPBhBuEiwAPMijrwmAexC5tNJAURlMgMPkdQXzsmPtpfJ6zYRoOgjA9hJyVD5zvQBuBxoC8zwQAvD_BwE; mbox=PC#6d09f098fa7a4527a71673dd0f9ebb40.41_0#1841574325|session#c3bda8dc1b1143d5a760ecf4791c8689#1778331385; _ga_L4KSHMGE1T=GS2.1.s1778329498$o2$g1$t1778329526$j32$l0$h803231252; _uetsid=a7d205304af611f1b4b27767b5b745e1; _uetvid=a7d218804af611f1aa6fb34b794a0082; _clsk=chuj4j%5E1778329529503%5E3%5E1%5Ez.clarity.ms%2Fcollect; cto_bundle=6NnOqF9LSkpRUGFRYmszRFRVUCUyQjhSTzJmJTJCNDljS2JVUjZCajR6ZUh2JTJCTVNUQVNxQk1LaDFLbVVLcU1uYVJGUTlQd25wTEp1TzdNQ2QyYjkxdWJzcWxoSTglMkJyUjdNZ3ZpdiUyQmg3N3RaeTRhdWZxSXJqMmN1Qkx3QUpkZjZQbTN4ZGN2TXRxUlB5TVR0ZVZoeTM0ZHglMkZ5WDNYdmclM0QlM0Q; RT="z=1&dm=lg.com&si=0dc8b910-38ea-450d-ba93-53f1ce63a21c&ss=moybgrkm&sl=3&tt=kw4&bcn=%2F%2F684d0d47.akstat.io%2F&ld=sks"; ttcsid=1778329500291::6xtE-ktSPvaCyBRzgFCU.1.1778329533371.0::1.17117.27443::1623.1.82.92::742.2.0; ttcsid_CUGNBCRC77U27ULH3T3G=1778329500290::1ASTjYL3BKBzJM-85FLp.1.1778329533371.1',
    }

    response = requests.get(url, cookies=cookies, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)
        print(response.text)
        return None
    

# responce = request('https://www.lg.com/in/')
# with open('html pages/lg_main.html','w',encoding='utf-8') as f:
#     f.write(responce)
    
