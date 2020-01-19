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

    remove = input('=>')
    print('Этот функционал еще не реализован')
    
    # Этот функционал еще не реализован
    pass