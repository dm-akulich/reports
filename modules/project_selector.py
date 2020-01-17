def project_selector():
    while True:
        user_input = input('\n1) Выбрать проект из списка;\n2) Добавить проект в список\n=>')
        if user_input == '1':
            f = open("project_list.txt", "r")
            list_of_projects = []
            for line in f:
                project = line.split(' - ')
                list_of_projects.append(project)

            print(list_of_projects)
            break # закончил тут
        elif user_input == '2':
            print('OK 2')
            break
        else:
            print('Что-то пошло не так. Попробуйте еще раз или Ctrl+C, чтобы выйти из программы')
        



    site_id = '1038110' # Для теста

    # site_id = str(input('\nВведите id проекта (смотрим в трекере) = ')) # Ввод id проекта


    # параметр в open 'a'	открытие на дозапись, информация добавляется в конец файла.
    return site_id