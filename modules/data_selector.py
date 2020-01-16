def data_selector(date_1, date_2, date_3, prepared_list):
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
    
    return clear_prepared_list
