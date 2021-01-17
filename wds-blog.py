import requests
from bs4 import BeautifulSoup
from os import path
import csv

def load_html():
    # open html file
    if (path.isfile('wds-blog.html')):
        with open('wds-blog.html') as html_page:
            soup = BeautifulSoup(html_page, 'html.parser')
            print('file loaded from local dir')
            # print(soup.prettify())
            return soup
    else:
        print('file is not on local. it is getting downloaded form server')
        source = requests.get('https://blog.webdevsimplified.com/').content
        print('file download is completed')
        soup = BeautifulSoup(source, 'html.parser')
        # print(soup.prettify())
        print('file download is completed')
        # saving html file so that I don't need to request it from the server every time
        html_file = open('wds-blog.html', 'w')
        html_file.write(soup.prettify())
        html_file.close()
        print('file has been saved on the local dir')
        return soup


csv_file = open('wds_blog_scrapped_data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['heading', 'publish_date', 'topic', 'description'])

soup = load_html()
for article in soup.find_all('article'):
    # getting data

    heading = article.header.h3.a.text
    heading = " ".join(heading.split())

    publish_date = article.header.small.text
    publish_date = " ".join(publish_date.split())

    topic = article.header.div.small.div.label.span.text
    topic = " ".join(topic.split())

    description = article.section.text
    description = " ".join(description.split())

    csv_writer.writerow([heading, publish_date, topic, description])

csv_file.close()
print('done')