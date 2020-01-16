

def date_validation(val_for_date_validate):
    print('Список доступных дат:')
    for i in val_for_date_validate:
        for date_dict in i['positions']:
            print(date_dict['date'])


    print('\nВыберите 3 даты:')
    date_1 = '2020-01-02' # Даты для теста
    date_2 = '2020-01-05' # Даты для теста
    date_3 = '2020-01-11' # Даты для теста
    date_list = [date_1, date_2, date_3]
    ######### date_1 = (input('Дата 1 = '))
    ######### date_2 = (input('Дата 2 = '))
    ######### date_3 = (input('Дата 3 = '))
    return date_list