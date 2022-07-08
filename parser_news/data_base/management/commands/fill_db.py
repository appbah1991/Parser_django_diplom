import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from data_base.models import Title, Url, News


class Command(BaseCommand):

    def handle(self, *args, **options):

        req = str('javascript').replace(' ', '+')

        num_of_page = 1

        url = f'https://pythondigest.ru/feed/?q={req}'

        responce = requests.get(url)

        while str(responce) != '<Response [404]>':

            url = f'https://pythondigest.ru/feed/?q={req}&page={num_of_page}'

            responce = requests.get(url)
            soup = BeautifulSoup(responce.text, 'html.parser')

            list_of_find_one_page = soup.find_all('div', class_="news-line-item")

            for item in list_of_find_one_page:

                url_one_news = item.a['href']

                soup_header = item.a.get_text()

                block_of_news = item.get_text()

                block_of_news = str(block_of_news).replace(soup_header, '')

                Title.objects.create(name=f'{soup_header}')
                Url.objects.create(name=f'{url_one_news}')
                News.objects.create(text=f'{block_of_news}', title = Title.objects.create(name=f'{soup_header}'), url = Url.objects.create(name=f'{url_one_news}'))

            print(f'Страница {num_of_page} пройдена...')

            num_of_page += 1
