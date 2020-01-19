# - *- coding: utf- 8 - *-

import pandas as pd
import numpy as np
import ast

def tops_percent_count(ready_df, date_1, date_2, date_3):
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

    # print(df_with_stats)
    # Считаем % ТОП-1
    def top_1_counter(ready_df):
        row_of_top_1 = list(['ТОП-1', ])
        how_much_top1_1 = 0
        for i in ready_df.iloc[:, 2]: # Итерация по первому столбцу с датами
            if i == 1:
                how_much_top1_1 += 1
        percent_of_top_1 = how_much_top1_1 / len(ready_df.iloc[:, 0]) * 100
        row_of_top_1.append(round(percent_of_top_1, 3))
        how_much_top1_2 = 0
        for i in ready_df.iloc[:, 3]: # Итерация по второму столбцу с датами
            if i == 1:
                how_much_top1_2 += 1
        percent_of_top_1 = how_much_top1_2 / len(ready_df.iloc[:, 0]) * 100
        row_of_top_1.append(round(percent_of_top_1, 3))

        how_much_top1_3 = 0
        for i in ready_df.iloc[:, 4]: # Итерация по третьему столбцу с датами
            if i == 1:
                how_much_top1_3 += 1
        percent_of_top_1 = how_much_top1_3 / len(ready_df.iloc[:, 0]) * 100
        row_of_top_1.append(round(percent_of_top_1, 3))

        return row_of_top_1

    row_of_top_1 = top_1_counter(ready_df)


    # Считаем % ТОП-5
    def top_5_counter(ready_df):
        row_of_top_5 = list(['ТОП-5', ])
        how_much_top5_1 = 0
        for i in ready_df.iloc[:, 2]: # Итерация по первому столбцу с датами
            if i in range(1, 6):
                how_much_top5_1 += 1
        percent_of_top_5 = how_much_top5_1 / len(ready_df.iloc[:, 0]) * 100
        row_of_top_5.append(round(percent_of_top_5, 3))
        how_much_top5_2 = 0
        for i in ready_df.iloc[:, 3]: # Итерация по второму столбцу с датами
            if i in range(1, 6):
                how_much_top5_2 += 1
        percent_of_top_5 = how_much_top5_2 / len(ready_df.iloc[:, 0]) * 100
        row_of_top_5.append(round(percent_of_top_5, 3))

        how_much_top5_3 = 0
        for i in ready_df.iloc[:, 4]: # Итерация по третьему столбцу с датами
            if i in range(1, 6):
                how_much_top5_3 += 1
        percent_of_top_5 = how_much_top5_3 / len(ready_df.iloc[:, 0]) * 100
        row_of_top_5.append(round(percent_of_top_5, 3))

        return row_of_top_5
        
    row_of_top_5 = top_5_counter(ready_df)


        # Считаем % ТОП-10
    def top_10_counter(ready_df):
        row_of_top_10 = list(['ТОП-10', ])
        how_much_top10_1 = 0
        for i in ready_df.iloc[:, 2]: # Итерация по первому столбцу с датами
            if i in range(1, 11):
                how_much_top10_1 += 1
        percent_of_top_10 = how_much_top10_1 / len(ready_df.iloc[:, 0]) * 100
        row_of_top_10.append(round(percent_of_top_10, 3))
        how_much_top10_2 = 0
        for i in ready_df.iloc[:, 3]: # Итерация по второму столбцу с датами
            if i in range(1, 11):
                how_much_top10_2 += 1
        percent_of_top_10 = how_much_top10_2 / len(ready_df.iloc[:, 0]) * 100
        row_of_top_10.append(round(percent_of_top_10, 3))

        how_much_top10_3 = 0
        for i in ready_df.iloc[:, 4]: # Итерация по третьему столбцу с датами
            if i in range(1, 11):
                how_much_top10_3 += 1
        percent_of_top_10 = how_much_top10_3 / len(ready_df.iloc[:, 0]) * 100
        row_of_top_10.append(round(percent_of_top_10, 3))

        return row_of_top_10
        
    row_of_top_10 = top_10_counter(ready_df)


    print('Строка с ТОП-1', row_of_top_1) 
    print('Строка с ТОП-5', row_of_top_5) 
    print('Строка с ТОП-10', row_of_top_10)

    # Добавляем полученные строки в df 
    df_with_stats_of_top.loc['1'] = row_of_top_1 # метод loc вставляет строку по индексу
    df_with_stats_of_top.loc['2'] = row_of_top_5
    df_with_stats_of_top.loc['3'] = row_of_top_10
    # print(df_with_stats_of_top)

    # Сохраняем в xlsx
    # df_with_stats_of_top.to_excel('output-tops.xlsx')


    return df_with_stats_of_top


