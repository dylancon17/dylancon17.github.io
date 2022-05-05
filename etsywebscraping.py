# YouTube Link:

# Ensure that you have both beautifulsoup and requests installed:
#   pip install beautifulsoup4
#   pip install requests

from cgitb import text
from logging.config import valid_ident
from turtle import clear
import requests
from bs4 import BeautifulSoup

# Using the requests module, we use the "get" function
# provided to access the webpage provided as an
# argument to this function:
result = requests.get("https://www.etsy.com/ca/shop/CakesByJennele")

# To make sure that the website is accessible, we can
# ensure that we obtain a 200 OK response to indicate
# that the page is indeed present:
# print(result.status_code)

# For other potential status codes you may encounter,
# consult the following Wikipedia page:
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# We can also check the HTTP header of the website to
# verify that we have indeed accessed the correct page:
# print(result.headers)

# For more information on HTTP headers and the information
# one can obtain from them, you may consult:
# https://en.wikipedia.org/wiki/List_of_HTTP_header_fields

# Now, let us store the page content of the website accessed
# from requests to a variable:
src = result.content


soup = BeautifulSoup(src, "html.parser")

text_and_money = soup.find_all("div", {"class": "v2-listing-card__info"})


cash = []
for div in text_and_money:
    money = div.find("span", {"class": "currency-value"})
    cash.append(money.text)
# print(cash)

title = []
for div in text_and_money:
    name = div.find("h3")
    title.append(name.text)


titles_edited = []
for label in title:
    label_shorter = label[2:]
    label_clear = label_shorter.strip()
    titles_edited.append(label_clear)
# print(titles_edited)

link = soup.find_all("a", {"class": "listing-link wt-display-inline-block wt-transparent-card"})

posting_link = []
for div in link:
    posting_link.append(div['href'])
# print(posting_link)



images = soup.find_all("div", {"class": "height-placeholder"})

posting_image = []
for image in images:
    try:
        posting_image.append(image.img['src'])
    except:
        posting_image.append(image.img['data-src'])


print('CurrentToppersForSale.objects.bulk_create([')
for slot, title in enumerate(titles_edited):
    # print(title)
    # print(slot)
    print(f'CurrentToppersForSale(Name=\'{titles_edited[slot]}\', Cost=\'{cash[slot]}\', Image=\'{posting_image[slot]}\', Url=\'{posting_link[slot]}\'),')

print('])')
