import pandas as pd
import numpy as np
import ast

def visibility_percent_count(ready_df, date_1, date_2, date_3):
    '''
    Функция, которая подсчитывает процент запросов в различных ТОПах.
    Вывод ---> Итоговая таблица имеет вид:

    ---------------------------------------------------
    | Вид ТОПа | <Дата 1>   | <Дата 2>   | <Дата 3>   |
    ---------------------------------------------------
    | ТОП-1    | <Значение> | <Значение> | <Значение> |
    ---------------------------------------------------
    '''
    
    # Хедер для таблицы
    header_for_df = "{'Type of TOP': [], '" + str(date_1) + "': [], '" + str(date_2) + "': [], '" + str(date_3) + "': []}"
    header_for_df = ast.literal_eval(header_for_df)
    df_with_stats_of_top = pd.DataFrame(header_for_df)
    return print('hi')