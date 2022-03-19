import requests
# import wget
import wget

url = "https://ichef.bbci.co.uk/news/976/cpsprodpb/11C27/production/_123634727_ukraine_east_map_single_mapx2640-nc.png"

# response = requests.get(url)
# print(response)
# with open("file.png", "wb") as f:
#     f.write(response.content)
#     print()

wget.download(url)
