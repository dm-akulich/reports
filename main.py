import requests
import json
import pandas as pd

headers = {
    'Authorization': 'Token 28db9a3c44bb37307afcbccea4276b0dfd7d3893',
}

# Ввод id проекта
site_id = '1038110' # Для теста
########### site_id = str(input('\nВведите id проекта (смотрим в трекере) = '))

# Какие поисковые системы используются в проекте
print('Поисковые системы проекта {}'.format(site_id))
search_engines_list = requests.get('https://api4.seranking.com/sites/{}/search-engines'.format(site_id), headers=headers)
search_engines = search_engines_list.json()
# Введите site_engine_id = 
for i in search_engines:
    print('ПС 1: site_engine_id =', i['site_engine_id'], '; search_engine_id =', i['search_engine_id'])

site_engine_id = '1157702'
######### site_engine_id = str(input('Введите site_engine_id = '))

# print('Исторические даты проекта {}'.format(site_id))
historical_dates = requests.get('https://api4.seranking.com/sites/{}/historicalDates'.format(site_id), headers=headers)
historical_dates = historical_dates.json()
last90 = historical_dates['90days']
current = historical_dates['current']


site_positions_json = requests.get('https://api4.seranking.com/sites/{}/positions?date_from={}&date_to={}&site_engine_id={}'.format(site_id, last90, current, site_engine_id), headers=headers)
site_positions = site_positions_json.json()

# В данный момент данные о позициях выглядят типа [{key: data ...}] - словарь в списке. Достнем его оттуда с помощью цикла for
# print('Тип переменной', type(site_positions))
for i in site_positions:
    site_positions = i

# print(type(site_positions))
# Ура

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
    
# Вроде пропарсили ^_^

# можно проверить как пропарсились данные, раскомментив код ниже
'''
for i in prepared_list:
    print('\nanother Keyword')
    print(i)
'''
# print(prepared_list) # Вывести полуготовые данные целиком в виде словаря, с которыми можно уже работать

print('Список доступных дат:')
#### Вывод доступных дат
for i in prepared_list[:1]:
    for date_dict in i['positions']:
        print(date_dict['date'])


print('\nВыберите 3 даты:')
date_1 = '2020-01-02'
date_2 = '2020-01-05'
date_3 = '2020-01-11'
######### date_1 = (input('Дата 1 = '))
######### date_2 = (input('Дата 2 = '))
######### date_3 = (input('Дата 3 = '))

#### Чистка prepared_list, чтобы оставить там три выбранные даты
clear_prepared_list = []
for i in prepared_list:
    clear_prepared_row = {}
    clear_prepared_row['name'] = i['name']
    clear_prepared_row['volume'] = i['volume']
    list_of_dicts = []
    for position_date in i['positions']:
        if position_date['date'] == date_1:
            list_of_dicts.append(position_date)
        elif position_date['date'] == date_2:
            list_of_dicts.append(position_date)
        elif position_date['date'] == date_3:
            list_of_dicts.append(position_date)
    clear_prepared_row['positions'] = list_of_dicts
    # print(list_of_dicts)

    clear_prepared_list.append(clear_prepared_row)
### Теперь в списке только нужные даты





# Подготовка таблицы c позициями
from def_dict_to_df import dict_to_df
ready_df = dict_to_df(clear_prepared_list, date_1, date_2, date_3)
ready_df.to_excel("output-positions.xlsx")


# Подготовка таблицы c ТОПами
from def_tops_percent_count import tops_percent_count
df_with_stats_of_top = tops_percent_count(ready_df, date_1, date_2, date_3)
df_with_stats_of_top.to_excel("output-positions.xlsx")











