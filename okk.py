import requests, json
# res  = requests.get("https://www.okx.com/zh-hans/p2p-markets/thb/buy-usdt")
# print(res.text)
try:
    headers2 = {
    # 'Cookie':'insert_cookie=59063098; JSESSIONID=6301641DEE636034E53A550C09C3F8B7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    res  = requests.get("https://www.okx.com/v3/c2c/tradingOrders/getMarketplaceAdsPrelogin?side=sell&paymentMethod=all&userType=all&hideOverseasVerificationAds=false&sortType=price_asc&limit=100&cryptoCurrency=USDT&fiatCurrency=THB&currentPage=1&numberPerPage=10&t=1744882961584",headers=headers2)
    print(res.text)
    ress = json.loads(res.text)
    print(len(ress['data']['sell']))
    first_name = ress['data']['sell'][0]["nickName"]
    price  = ress['data']['sell'][0]['price']
    if first_name == "FastTrans_":
        requests.get("https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/"+first_name+"\t"+price+"?group=okk")
    else:
        requests.get("https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/"+"Low"+first_name+"\t"+price+"?group=okk")
except Exception as e:
    requests.get("https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/okk错误：" + str(e) + "?group=okk")
