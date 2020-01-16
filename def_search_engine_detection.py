import pandas as pd
import numpy as np
import ast
import json
import requests

print('hi')


def search_engine_detection(site_id, headers):
    print('Поисковые системы проекта {}'.format(site_id))
    search_engines_list = requests.get('https://api4.seranking.com/sites/{}/search-engines'.format(site_id), headers=headers)
    search_engines = search_engines_list.json()

    for i in search_engines:
        if i['region_id'] == 0:
            print('It is a Google! Site Engine = ', i['site_engine_id'])
            google_site_engine_id = i['site_engine_id']

        elif i['region_id'] != 0:
            print('It is a Yandex! Site Engine = ', i['site_engine_id'])
            yandex_site_engine_id = i['site_engine_id']
    
    # Выбор ПС для пользователя
    search_engine_detection_user_input = int(input('\nВыберите ПС (вписать цифру): \n0) Google;\n1) Yandex\nПС = '))
    if search_engine_detection_user_input == 0:
        print('Выбрана ПС Google')
        site_engine_id = google_site_engine_id
    elif search_engine_detection_user_input == 1:
        print('Выбрана ПС Yandex')
        site_engine_id = yandex_site_engine_id
    else:
        print('Упс. Что-то пошло не так :(')
    return site_engine_id
    

