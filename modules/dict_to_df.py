import pandas as pd
import json
import ast

# Функция, которая преобразует сложный дикт в dataframe


def dict_to_df(clear_prepared_list, date_1, date_2, date_3):
    '''
    Функция, которая будет превращать сложный словарь в dataframe.
    Dataframe будет иметь следующий вид:
    
    ----------------------------------------------
    | id |    name    | dd-Mon | dd-Mon | dd-Mon |
    ----------------------------------------------
    | 12 | компрессор |   3    |    1   |    2   |
    ----------------------------------------------
    '''
    header_for_df = "{'name': [], 'volume': [], '" + str(date_1) + "': [], '" + str(date_2) + "': [], '" + str(date_3) + "': []}"
    header_for_df = ast.literal_eval(header_for_df)
    
    df_with_stats = pd.DataFrame(header_for_df)

    # добавляем в df имена ключевых слов
    numbers_of_row = len(clear_prepared_list)
    index_value = 0
    for row in clear_prepared_list:
        # print(row)
        keyword_name = row['name']
        volume = row['volume']
        prepared_row = [keyword_name, volume]
        for key in row:
            if key == 'positions':
                pos_list = []
                for i in row['positions']:
                    prepared_row.append(i['pos'])
                # print(pos_list)
            else:
                pass
        # print('new row', prepared_row)
        index_value += 1


        # добавляем подготовленную строку в df
        df_with_stats.loc[index_value] = prepared_row


    print(df_with_stats)

    return df_with_stats


# print(dict_to_df(prepared_list))