import requests
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_links(html):
    links = []
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('table', id='forum_table').find_all(
        'div', class_='is_colorized')
    for div in range(1, len(divs)):
        a = divs[div].find('a').get('href')
        full_link = 'http://diesel.elcat.kg/index.php?showforum=442' + a
        links.append(full_link)
    return links


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        head = soup.find('h1', class_='ipsType_pagetitle').text.strip()
    except:
        head = ''
    try:
        date = soup.find('span', itemprop='dateCreated').text.strip()
    except:
        date = ''
    try:
        author = soup.find('span', itemprop='name').text.strip()
    except:
        author = ''
    data = {
        'head': head, 'price': date, 'author': author
    }
    return data


def write_csv(data):
    with open('laptops.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data["head"], data["price"], data["author"]))
        print(data["head"], data["price"], data["author"])


def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)


def main():
    url = 'http://diesel.elcat.kg/index.php?showforum=442'
    all_links = get_all_links(get_html(url))
    with Pool(40) as p:
        p.map(make_all, all_links)
    return


if __name__ == '__main__':
    main()
