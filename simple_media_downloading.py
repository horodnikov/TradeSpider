import requests


def get_extension(headers):
    if "Content-Type" not in headers:
        raise ValueError(f"There are no Content-Type in headers: {headers}")
    return headers["Content-Type"].split("/")[-1]

url = "https://ichef.bbci.co.uk/news/976/cpsprodpb/11C27/production/_123634727_ukraine_east_map_single_mapx2640-nc.png"

r = requests.get(url)
print(get_extension(r.headers))
f"file.{get_extension(r.headers)}"
print()
