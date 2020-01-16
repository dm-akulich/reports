a = {'name': 'Dima'}

# print(a['name'])

x_list = [{'id': '69683225', 'positions': [{'date': '2020-01-02', 'pos': 9},
                                            {'date': '2020-01-05', 'pos': 9},
                                            {'date': '2020-01-08', 'pos': 9},
                                            {'date': '2020-01-11', 'pos': 10}],
                                            'name': 'ременный компрессор купить'}]
for item_dict in x_list:
    new_dict = item_dict['positions']
    id_key = item_dict['id']
    name_key = item_dict['name']
    print('\nВыберите даты, которые необходимо оставить (3шт):')
    for item in new_dict:
        # print(item['date'])
        pass

x_list_new = {}
date_1_val = '2020-01-02' #date_1_key = input('date_1 = ')
date_2_val = '2020-01-05' #date_2_key = input('date_2 = ')
date_3_val = '2020-01-08' #date_3_key = input('date_3 = ')

x_list_new['id'] = 'id'
x_list_new['name'] = 'name'
x_list_new['date_1_val'] = date_1_val
x_list_new['date_2_val'] = date_2_val
x_list_new['date_3_val'] = date_3_val
x_list_new = x_list_new
print(x_list_new)