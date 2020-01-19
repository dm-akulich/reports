import re

def project_selector_3_remove_project(headers):
    # Считываем список проектов из txt файла
    f = open(".project_list", "r")
    list_of_projects = []
    for line in f:
        project = line.split(':')
        list_of_projects.append(project)
    
    #Удалить символ \n в списке
    for i in list_of_projects:
        i[1] = re.sub(r"\n", "", i[1])

    # print(list_of_projects)
    
    # Выводим список проектов
    counter_for_project_list = 0
    print('\nКакой проект удалить?:')
    for project in list_of_projects:
        counter_for_project_list += 1
        project.append(counter_for_project_list)
        print('{}) {}'.format(project[2], project[1]))

    # print('Список с которым работаем: ', list_of_projects)
    while True:
        try:
            user_input = input('=>')
            remove_item = int(user_input) - 1
            del list_of_projects[remove_item]
            print('Проект удален из списка.')
            break
        except ValueError:
            print('Введено что-то не то. Попробуйте еще раз.')
    
    # Запись в файл
    f = open(".project_list", "w")
    for item in list_of_projects:
        f.write('{}:{}\n'.format(item[0], item[1]))

    f.close()

    # Этот функционал еще не реализован
    return print('Список проектов обновлен.')