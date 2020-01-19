import requests
import json
import pandas as pd

def data_parser(site_positions):
    # В данный момент данные о позициях выглядят типа [{key: data ...}] - словарь в списке. Достнем его оттуда с помощью цикла for
    # print('Тип переменной', type(site_positions))
    for i in site_positions:
        site_positions = i
    # print(type(site_positions))
    # Полный датасет c позициями, у которого колонки говно
    data = pd.DataFrame(site_positions, columns=site_positions.keys())
    # нам нужна только колонка keywords
    keywords_df = pd.DataFrame(data['keywords'])
    # Список, в который будем собирать необходимые значения с помощью цикла
    prepared_list = []
    for index, row in keywords_df.iterrows():
        keyword_dict = row['keywords']
        temporary_dict = {}
        for key in keyword_dict:
            # print(key, '-->',keyword_dict[key])
            # Временный словарь-контейнер, в который кидаем данные каждого поискового запроса. Забираем пары ключ-значение id, name, date{}
            if key == 'id':
                temporary_dict['id'] = keyword_dict[key]
            elif key == 'name':
                temporary_dict['name'] = keyword_dict[key]
            elif key == 'volume':
                temporary_dict['volume'] = keyword_dict[key]
            elif key == 'positions':
                temporary_list_for_positions = []
                # print('####### Im here START')
                # итерируемся по словарю с датами
                for key_date in keyword_dict['positions']:
                    key_date_dict = {}
                    for val in key_date:
                        if val == 'date':
                            key_date_dict['date'] = key_date[val]
                        elif val == 'pos':
                            key_date_dict['pos'] = key_date[val]
                        else:
                            pass
                    temporary_list_for_positions.append(key_date_dict)
                # print(temporary_list_for_positions)
                # print(type(temporary_list_for_positions))
                temporary_dict['positions'] = temporary_list_for_positions
            #### Конец
            else:
                pass
        prepared_list.append(temporary_dict)
    # можно проверить как пропарсились данные, раскомментив код ниже
    '''
    for i in prepared_list:
        print('\nanother Keyword')
        print(i)
    '''
    # print(prepared_list) # Вывести полуготовые данные целиком в виде словаря, с которыми можно уже работать
    return prepared_list