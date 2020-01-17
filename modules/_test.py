f = open("project_list.txt", "r")

list_of_projects = []
for line in f:
    project = line.split(' - ')
    list_of_projects.append(project)

print(list_of_projects)

    