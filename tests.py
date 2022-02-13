import requests
from bs4 import BeautifulSoup
a = {

"accept": "application/json, text/plain, */*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
"content-length": "145",
"content-type": "application/json;charset=UTF-8",
"origin": "https://www.k-rauta.fi",
"sec-ch-ua": '"Opera GX";v="83", "Chromium";v="97", ";Not A Brand";v="99"',
"sec-ch-ua-mobile": "?1",
"sec-ch-ua-platform": "Android",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36"
}
r = requests.post("https://www.k-rauta.fi/api/price/ecom/products", headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}, data={"eans":["6438313491118","6438313491279","6438313491347"]})


print(r.text)
