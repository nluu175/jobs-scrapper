# https://realpython.com/python-web-scraping-practical-introduction/
from urllib.request import urlopen


url = "http://olympus.realpython.org/profiles/aphrodite"


page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")


print(html)


title_index = html.find("<title>")
start_index = title_index + len("<title>")

print(start_index)

end_index = html.find("</title>")

print(end_index)

title = html[start_index:end_index]

print(title)
