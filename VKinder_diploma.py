import requests
from pprint import pprint
import time
import json


# user = input('Введите id или имя пользователя')
find_city = 'Нижний Новогород' #input('Введите название города строкой')
find_sex = 1 # input('Введите пол. Возможные значения: '
                 # '1 — женщина;'
                 # '2 — мужчина;'
                 # '0 — любой (по умолчанию).')
find_age_from = 25 #input('Введите возраст от')
find_age_to = 31 #input('Введите возраст до')

with open('take_token.txt', encoding='utf-8') as f:
    TOKEN = f.read()

params = {
    'v': '5.92',
    'access_token': TOKEN,
    # 'user_id': user,
    'count': 10,
    'offset': 10,
    'sex': find_sex,
    'hometown': find_city,
    'age_from': find_age_from,
    'age_to': find_age_to,
    'sort': 0,
    # 'fields': 'domain',
    # 'status': 6
}


def users_search():
    id_list = []
    resp_js_gr = requests.get('https://api.vk.com/method/users.search', params).json()['response']['items']
    # pprint(resp_js_gr)
    for user in resp_js_gr:
        id_list.append(user['id'])
    return id_list

pprint(users_search())