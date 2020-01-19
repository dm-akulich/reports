# - *- coding: utf- 8 - *-

import requests
import json
import pandas as pd

from modules.search_engine_detection import search_engine_detection
from modules.dict_to_df import dict_to_df
from modules.tops_percent_count import tops_percent_count
from modules.visibility_percent_count import visibility_percent_count
from modules.api_autorization import api_autorization
from modules.date_validation import date_validation
from modules.data_parser import data_parser
from modules.data_selector import data_selector
from modules.project_selector import project_selector


headers = api_autorization() # Проверка API ключа, авторизация

site_id = project_selector(headers) # Выбор проекта

search_engine_detection_return = search_engine_detection(site_id, headers) # Выбор поисковых систем, используюемых в проекте
site_engine_id = search_engine_detection_return[0]
search_engine_name = search_engine_detection_return[1]

# print('Исторические даты проекта {}'.format(site_id))
historical_dates = requests.get('https://api4.seranking.com/sites/{}/historicalDates'.format(site_id), headers=headers)
historical_dates = historical_dates.json()
last90 = historical_dates['90days']
current = historical_dates['current']


site_positions_json = requests.get('https://api4.seranking.com/sites/{}/positions?date_from={}&date_to={}&site_engine_id={}'.format(site_id, last90, current, site_engine_id), headers=headers)
site_positions = site_positions_json.json()

# Парсим нужные колонки
prepared_list = data_parser(site_positions) 


# Валидация даты начало
val_for_date_validate = prepared_list[:1]
date_list = date_validation(val_for_date_validate)
date_1 = date_list[0]
date_2 = date_list[1]
date_3 = date_list[2]
# Валидация даты конец


# Чистка дат
clear_prepared_list = data_selector(date_1, date_2, date_3, prepared_list) 


# Подготовка таблицы c позициями
ready_df = dict_to_df(clear_prepared_list, date_1, date_2, date_3)
ready_df.to_excel("output-positions.xlsx")


# Подготовка таблицы c ТОПами
# df_with_stats_of_top = tops_percent_count(ready_df, date_1, date_2, date_3)
# df_with_stats_of_top.to_excel("output-tops.xlsx")


# Подготовка таблицы с видимостью
df_with_stats_of_visibility = visibility_percent_count(ready_df, date_1, date_2, date_3, search_engine_name)












