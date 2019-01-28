import re
import requests
import json
import os
from bs4 import BeautifulSoup as bs


def writeJson(filename,data):
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        # checks if file exists
        print ("File exists. Iterate next")
    else:
        with open(filename, 'w') as f:
            json.dump(data, f)


def scrape_full_page(introduction, link):
    while introduction:

        if introduction.name == 'h2':
            data = {}
            title = introduction.find('span', class_='mw-headline').text
            data['heading'] = title
            data['content'] = ""
            # print(intro.find('span', class_='mw-headline').text)

            value = introduction.find_next_sibling()

            while value and value.name != 'h2':
                if value.attrs.get('class') :
                    if value.attrs.get('class')[0] == 'collapsible':
                        value = value.find_next_sibling()
                        continue

                if len(value.text) > 20:
                    data['content'] += '\n' + value.text
                    # print(content.text)

                value = value.find_next_sibling()

            if value and value.attrs.get('class') and value.attrs.get('class')[0] == 'collapsible':
                value = value.find_next_sibling()
                continue

            introduction = value

            filename = "extra1/" + title.replace('/', '_') + "_" + link.split("/")[-1] + ".json"
            print(filename)

            writeJson(filename, data)


def scrape_introduction(begin):
    while begin:

        for i in begin.find_all("a", href=re.compile("/wiki/Java_Programming/")):
            # print i
            link = 'https://en.wikibooks.org' + i.get("href")
            # print "**********YOOOOOO***********"
            # print link
            r = requests.get(link)
            soup = bs(r.content, features="lxml")

            data = {}

            introduction = soup.find('table', class_='wikitable')
            if introduction:
                introduction = introduction.find_next_sibling()

            title = 'intro_' + link.split("/")[-1]

            data['heading'] = title
            data['content'] = ""

            while introduction and introduction.name != 'h2':
                if len(introduction.text) > 10:
                    data['content'] = data['content'] + ' ' + introduction.text
                    # print(intro.text)

                introduction = introduction.find_next_sibling()

            filename = "extra1/" + title + ".json"
            # print(filename)
            writeJson(filename, data)
            scrape_full_page(introduction, link)

            # inner_Data(link)

        begin = begin.find_next_sibling()


def inner_Data(link):
    # Crawling 2nd layer of data in java wikibooks... i.e. : links within the subpage
    # print "**********"
    # print link
    re = requests.get(link)

    soup1 = bs(re.content, features="lxml")

    if soup1.find('span', class_='mw-headline'):

        if soup1.find('span', class_='mw-headline').find_parent() is not None:

            begin1 = soup1.find('span', class_='mw-headline').find_parent()

            begin1 = begin1.find_next_sibling()

            scrape_introduction(begin1)


def main():

    r = requests.get('https://en.wikibooks.org/wiki/Java_Programming')

    soup = bs(r.content, features="lxml")

    begin = soup.find('span', class_='mw-headline').find_parent()

    begin = begin.find_next_sibling()

    scrape_introduction(begin)

main()
