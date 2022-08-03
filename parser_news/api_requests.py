# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parser_news.settings')
import requests
import pprint
from rest_framework.authtoken.models import Token

# set DJANGO_SETTINGS_MODULE= Django_1_project.settings
token = '25fba3a1cdf92b72880b3fc998ee5e3dc566e1b0'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/url/', headers=headers)

pprint.pprint(response.json())