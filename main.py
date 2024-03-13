# https://realpython.com/python-web-scraping-practical-introduction/
# https://medium.com/@chatur.agus.priyono/a-comprehensive-guide-to-scraping-data-from-linkedin-with-python-e128c46c5c74

import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)  # Remove HTML tags

print(title)
