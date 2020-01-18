import pandas as pd
import numpy as np
import ast

def visibility_percent_count(ready_df, date_1, date_2, date_3, search_engine_name):
    '''
    Функция, которая подсчитывает видимость.
    Вывод ---> Итоговая таблица имеет вид:

    ---------------------------------------------------
    | Вид ТОПа  | <Дата 1>   | <Дата 2>   | <Дата 3>   |
    ---------------------------------------------------
    | Имя ПС    | <Значение> | <Значение> | <Значение> |
    ---------------------------------------------------
    '''
    
    # Хедер для таблицы
    header_for_df = "{'Name of SE': [], '" + str(date_1) + "': [], '" + str(date_2) + "': [], '" + str(date_3) + "': []}"
    header_for_df = ast.literal_eval(header_for_df)
    df_with_stats_of_visibility = pd.DataFrame(header_for_df)
    
    # Пересчитываем значение первой даты
    koef = {1:1, 2:1, 3:1, 4:0.85, 5:0.60, 6:0.50, 7:0.50, 8:0.30, 9:0.30, 10:0.2}# Коэфициенты для пересчета
    
    visibility1 = 0
    for index, row in ready_df.iterrows():
        print(row['volume'], row[date_1])



    # Добавляем в df
    df_with_stats_of_visibility.loc[1] = [search_engine_name, 26, 'Bangalore', 'India']

    
    return print('hi!!!!\n', df_with_stats_of_visibility)