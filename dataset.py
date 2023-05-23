

import pandas as pd
import os

#import urllib.request

#from bs4 import BeautifulSoup
#from lxml import html
#from urllib.parse import urljoin


data = pd.read_csv("corgis_dataset.csv", usecols=["metadata.id", "bibliography.languages", "bibliography.subjects", "bibliography.title", "bibliography.type", "metadata.downloads", "metadata.url",  "bibliography.author.name", "bibliography.publication.day", "bibliography.publication.month", "bibliography.publication.year"])


print(data.head(3))

print(data.shape)

imgs = []
epubs = []

"""
for url in data["metadata.url"]: 

    with urllib.request.urlopen(url) as response:
        page = response.read()

        xpath_img =  "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/img"
        xpath_img2 = '//*[@id="cover"]/img/@src'
        xpath_epub = '/html/body/div[1]/div[1]/div[2]/div[4]/div/div[1]/div/table/tbody/tr[4]/td[2]/a'


        tree = html.fromstring(page)
        img = tree.xpath(xpath_img2)[0]
        #epub = tree.xpath(xpath_epub)


        soup = BeautifulSoup(page, 'lxml')

        epub = soup.find('a', type="application/epub+zip")[ 'href']
        epub = urljoin(url, epub)

        print(url)
        print((img, epub))

        imgs.append(img)
        epubs.append(epub)

        f = open("imgs.txt", "w")
        f.write('\n'.join(imgs))
        f.close()

        f = open("epubs.txt", "w")
        f.write('\n'.join(epubs))
        f.close()
"""


for _id in data["metadata.id"]:

    imgs.append("https://www.gutenberg.org/cache/epub/{}/pg{}.cover.medium.jpg".format(_id, _id))
    epubs.append("https://www.gutenberg.org/ebooks/{}.epub3.images".format(_id))



print(imgs)
print(epubs)

data.insert(0, "metadata.cover", imgs, True)
data.insert(0, "metadata.epub", epubs, True)


print(data.head(3))
print(data.shape)


# remove type dataset and stillimage
data = data[data["bibliography.type"] == "Text"]

print(data.head(3))
print(data.shape)


data.to_csv("data.csv")

