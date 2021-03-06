import re

def project_selector_1_select_project():
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
    print('\nСписок ваших проектов:')
    for project in list_of_projects:
        counter_for_project_list += 1
        project.append(counter_for_project_list)
        print('{}) {}'.format(project[2], project[1]))
    
    while True:
        try:
            user_input_select_site = int(input('\nВведите номер проекта\n=>'))
            for i in list_of_projects:
                if user_input_select_site == i[2]:
                    print('Выбран проект =>', i[1])
                    site_id = i[0]
            break
        except (ValueError, IndexError) :
            print('Необходимо ввести число из списка. Попробуйте еще раз')
    return site_id