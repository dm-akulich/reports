l = [['777555849', 'remeza-europe.de', 1], ['234343', 'miltex.by', 2], ['2312344e3', 'remeza.by', 3]]
f = open("project_list.txt", "w")
for item in l:
    f.write('{}:{}\n'.format(item[0], item[1]))

f.close()