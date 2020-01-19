# - *- coding: utf- 8 - *-

def date_validation(val_for_date_validate):
    print('Список доступных дат:')
    data_counter = 0
    dict_of_available_dates = {}
    for i in val_for_date_validate:
        for date_dict in i['positions']:
            data_counter += 1
            dict_of_available_dates[data_counter] = date_dict['date']
            print('{}) {}'.format(data_counter, date_dict['date']))
    


    print('\nВыберите 3 даты (вписать число):')
    date_list = list([])
    while True:
        try:
            date_1 = dict_of_available_dates[int((input('Дата 1 =>')))] # Это готовый код, раскомментить, когда будет готов подсчет видимости
            date_2 = dict_of_available_dates[int((input('Дата 2 =>')))] # Это готовый код, раскомментить, когда будет готов подсчет видимости
            date_3 = dict_of_available_dates[int((input('Дата 3 =>')))] # Это готовый код, раскомментить, когда будет готов подсчет видимости
            # date_1 = '2019-10-19' # А вот это нужно будет закомментить
            # date_2 = '2019-12-12' # А вот это нужно будет закомментить
            # date_3 = '2020-01-11' # А вот это нужно будет закомментить
            print('Выбраны даты: {}; {}; {}'.format(date_1, date_2, date_3)) 
            date_list.append(date_1)
            date_list.append(date_2)
            date_list.append(date_3)
            break
        except ValueError:
            print('Похоже, было выбрано не число, попробуйте еще раз')
        except KeyError:
            print('Похоже, такого числа нет, попробуйте еще раз.')

    return date_list