import pandas as pd
import numpy as np
import ast
import json
import requests



def search_engine_detection(site_id, headers):
    print('\nПоисковые системы проекта {}'.format(site_id))
    search_engines_list = requests.get('https://api4.seranking.com/sites/{}/search-engines'.format(site_id), headers=headers)
    search_engines = search_engines_list.json()

    for i in search_engines:
        if i['region_id'] == 0:
            # print('It is a Google! Site Engine = ', i['site_engine_id'])
            google_site_engine_id = i['site_engine_id']

        elif i['region_id'] != 0:
            # print('It is a Yandex! Site Engine = ', i['site_engine_id'])
            yandex_site_engine_id = i['site_engine_id']
    
    # Выбор ПС для пользователя
    while True:
        search_engine_detection_user_input = input('\nВыберите ПС (вписать цифру): \n1) Google;\n2) Yandex\n=>')
        if search_engine_detection_user_input == '1':
            print('Выбрана ПС Google. Доступные даты загружаются...')
            search_engine_name = 'google'
            site_engine_id = google_site_engine_id
            break
        elif search_engine_detection_user_input == '2':
            print('Выбрана ПС Yandex. Доступные даты загружаются...')
            site_engine_id = yandex_site_engine_id
            search_engine_name = 'yandex'
            break
        else:
            print('Вы ввели что-то не то. Попробуйте еще раз или нажмите Ctrl+C, чтобы выйти из программы.')
    search_engine_detection_return = [site_engine_id, search_engine_name]
    return search_engine_detection_return
    # return site_engine_id
    






