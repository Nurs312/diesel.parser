import requests
from bs4 import BeautifulSoup
url = 'https://www.avito.ru/moskva/telefony?p=15q=htc'
def get_html(url):
    r = requests.get(url)
    return r
get_html(url)

# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     return soup


# def main():
#     #https://www.avito.ru/moskva/telefony?p=15q=htc
#     pass


# if __name__ == '__main__':
#     main()
