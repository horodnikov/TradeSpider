import requests
# Python3.6
# from urllib import request
# Python3.8
from urllib import parse

search = "материнская плата asus"
search = parse.quote_plus(search.encode("cp1251"))
print(search)
url = f"https://www.onlinetrade.ru/sitesearch.html?query={search}"
print(url)

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
response = requests.get(url, headers=headers)

print(response)

# response = requests.get(url, headers=headers)
#
# print(response)
