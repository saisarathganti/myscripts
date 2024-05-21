import requests
import re
from random import choice

url = "https://www.example.com/"
req = requests.get(url)
website_as_text = req.text 
# print(website_as_text)

if "This domain is for use in" in website_as_text:
    new_website_text = re.sub(r'\b{}\b'.format("This domain is for use in"), 'Sharu thopu eheee', website_as_text)
    # print(new_website_text)
    with open("new_website.html", "w") as f:
        f.write(new_website_text)


# Extracting body of html
html_body = re.findall('<body>[\S\s]*</body>', website_as_text)
print(html_body)