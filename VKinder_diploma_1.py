import requests
from pprint import pprint
import json
from datetime import datetime, date
import random
import time


now = date.today().year
user_name = input('Введите id или имя пользователя')  # 3877297

with open('take_token.txt', encoding='utf-8') as f:
    TOKEN = f.read()

params = {
    'v': '5.92',
    'access_token': TOKEN,
    'user_id': user_name,
}


def user_bdate():
    params['fields'] = 'bdate'
    resp_js_gr = requests.get('https://api.vk.com/method/users.get', params).json()['response'][0]
    if 'bdate' in resp_js_gr:
        d = resp_js_gr['bdate'].split('.')
        birth_year = int(d[2])
        user_age = now - birth_year
    else:
        user_age = input('Введите ваш возраст')
    return user_age


def user_sex():
    params['fields'] = 'city, sex, bdate'
    resp_js_gr = requests.get('https://api.vk.com/method/users.get', params).json()['response'][0]
    if 'sex' in resp_js_gr:
        user_sex = resp_js_gr['sex']
    else:
        user_sex = input('Введите ваш пол')
    return user_sex


def user_city():
    params['fields'] = 'city'
    resp_js_gr = requests.get('https://api.vk.com/method/users.get', params).json()['response'][0]
    if 'city' in resp_js_gr:
        user_city = resp_js_gr['city']['title']
    else:
        user_city = input('Введите название вашего города')
    return user_city


def users_search():
    id_list = []
    params['sex'] = sex
    params['age_from'] = age
    params['age_to'] = age
    params['count'] = 1000
    params['fields'] = 'home_town'
    # pprint(params)
    resp_js_gr = requests.get('https://api.vk.com/method/users.search', params).json()
    # pprint(resp_js_gr)
    for user in resp_js_gr['response']['items']:
        try:
            if user['home_town'] == city:
                id_list.append(user['id'])
        except KeyError:
            pass
            # print('Город не указан')
    return id_list


def random_users():
    random_users_id_list = random.sample(users_id_list, 10)
    return random_users_id_list


def users_popular_photo():
    random_users_id_list = random_users()
    users_dict = {}
    for user in random_users_id_list:
        params['owner_id'] = user
        params['count'] = 200
        params['extended'] = 1
        resp_js_gr = requests.get('https://api.vk.com/method/photos.getAll', params).json()
        user_photo_list = resp_js_gr['response']['items']
        time.sleep(0.4)
        user_top3_photos = sorted(user_photo_list, key=lambda x: x['likes']['count'], reverse=True)[:3]
        list_user_top3_photos = []
        for photo in user_top3_photos:
            list_user_top3_photos.append(photo['sizes'][-1]['url'])
        users_dict[user] = list_user_top3_photos
    return users_dict


age = user_bdate()
city = user_city()
sex = user_sex()
users_id_list = users_search()
random_users_id_list = random_users()
user_photo_list = users_popular_photo()
users_popular_photo = users_popular_photo()

with open("data_file.json", "w") as write_file:
    json.dump(users_popular_photo, write_file)
