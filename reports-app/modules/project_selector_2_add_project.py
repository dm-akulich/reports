import requests

def project_selector_2_add_project(headers):
    site_name = input('Введите название проекта\n=>')
    while True:
        try:
            site_id = int(input('Введите id проекта\n=>'))
            break
        except:
            print('id проекта должны быть числа.')
    add_request = requests.get('https://api4.seranking.com/sites/{}/search-engines'.format(site_id), headers=headers)
    print(add_request)
    if str(add_request) == '<Response [400]>':
        print('Ошибка 4хх. Возможно, id сайта введен неверно')

    elif str(add_request) == '<Response [200]>':
        f = open(".project_list", "a")
        f.write('{}:{}\n'.format(site_id, site_name))
        print('Cайт успешно добавлен в список проектов')
        f.close()
    else:
        print('Неопознанная ошибка')
    return print('')