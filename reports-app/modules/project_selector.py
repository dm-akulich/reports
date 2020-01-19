import re

from modules.project_selector_1_select_project import project_selector_1_select_project
from modules.project_selector_2_add_project import project_selector_2_add_project
from modules.project_selector_3_remove_project import project_selector_3_remove_project

def project_selector(headers):
    while True:
        user_input = input('\n1) Выбрать проект для расчета\n2) Добавить проект\n3) Удалить проект\n=>')
        if user_input == '1':
            site_id = project_selector_1_select_project()
            break
        
        elif user_input == '2':
            project_selector_2_add_project(headers)
        
        elif user_input == '3':
            project_selector_3_remove_project(headers)
        
        else:
            ######
            print('Что-то пошло не так. Попробуйте еще раз или Ctrl+C, чтобы выйти из программы')


    return site_id