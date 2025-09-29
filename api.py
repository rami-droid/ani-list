import requests

base_url = "https://api.jikan.moe/v4"
url_top = "/top/anime"

response = requests.get(url_top)
