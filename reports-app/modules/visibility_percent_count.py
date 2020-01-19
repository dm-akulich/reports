import pandas as pd
import numpy as np
import ast

def visibility_percent_count(ready_df, date_1, date_2, date_3, search_engine_name):
    '''
    Функция, которая подсчитывает видимость.
    Вывод ---> Итоговая таблица имеет вид:

    ----------------------------------------------------------
    | Вид ТОПа  |   <Дата 1>   |   <Дата 2>   |   <Дата 3>   |
    ---------------------------------------------------
    | Имя ПС    | <Значение 1> | <Значение 2> | <Значение 3> |
    ----------------------------------------------------------
    '''
    
    # Хедер для таблицы
    header_for_df = "{'Name of SE': [], '" + str(date_1) + "': [], '" + str(date_2) + "': [], '" + str(date_3) + "': []}"
    header_for_df = ast.literal_eval(header_for_df)
    df_with_stats_of_visibility = pd.DataFrame(header_for_df)
    
    koef = {1:1, 2:1, 3:1, 4:0.85, 5:0.60, 6:0.50, 7:0.50, 8:0.30, 9:0.30, 10:0.2} # Коэфициенты для пересчета
    
    # суммарная частотность
    sum_of_volume = 0
    for index, row in ready_df.iterrows():
        sum_of_volume += row['volume']

    # Подсчет для даты 1
    visibility_for_date_1 = 0
    for index, row in ready_df.iterrows():
        try:
            koef_for_position = koef[row[date_1]]
            # print(koef_for_position)
            visibility_for_date_1 += row['volume'] * koef_for_position
        except KeyError:
            pass # Просто пропускаем значения, которые не попадают под значения коэфициентов: позиции 0, 11, 12 и тп
            # print('-')
    visibility_for_date_1 = visibility_for_date_1 / sum_of_volume * 100

    # Подсчет для даты 2
    visibility_for_date_2 = 0
    for index, row in ready_df.iterrows():
        try:
            koef_for_position = koef[row[date_2]]
            # print(koef_for_position)
            visibility_for_date_2 += row['volume'] * koef_for_position
        except KeyError:
            pass 
    visibility_for_date_2 = visibility_for_date_2 / sum_of_volume * 100

    # Подсчет для даты 3
    visibility_for_date_3 = 0
    for index, row in ready_df.iterrows():
        try:
            koef_for_position = koef[row[date_3]]
            # print(koef_for_position)
            visibility_for_date_3 += row['volume'] * koef_for_position
        except KeyError:
            pass 
    visibility_for_date_3 = visibility_for_date_3 / sum_of_volume * 100        
    

    # Добавляем в df
    df_with_stats_of_visibility.loc[1] = [search_engine_name, visibility_for_date_1, visibility_for_date_2, visibility_for_date_3]

    # df_with_stats_of_visibility.to_excel('output-visibility.xlsx')
    
    return df_with_stats_of_visibility