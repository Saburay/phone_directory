# ----------------------
#   Code by Radimich
#   Date: 2023
#   Land:Larnevsk
# ----------------------
# ######################## часть чтения и записи в файл #############################

def readfile(name):
    try:
        with open(name,'r') as f:
            f.readlines()

    except:
        print('\t\t**********************************\n\t\tВНИМАНИЕ: Данных еще не сохранено!\n ')
        return []


def savedata(data, name):
    with open(name, 'w', encoding='utf-8') as f:
        f.writelines((data[0]))
    for i in data[1:]:
        if len(i)>20:
            try:
                with open(name, 'a', encoding='utf-8') as f:
                    f.writelines((i ))

            except Exception as e:
                print('Error savedata: ', e)



################## ввод и проверка данных ########################3

def correct_input(text):
    ''' проверка на ввод'''
    name = input(f'{text} > ')
    if name == '*':
        return name
    return name.capitalize()


def correct_number(text):
    ''' проверка номера'''
    print('номер +7 код номер без пробелов -> ')
    number = input(f'{text} > ')
    while True:
        if number[0] == '+' and number[1:].isdigit() and len(number) == 12:
            return number
        elif number[0] == '8' and number[1:].isdigit() and len(number) == 11:
            return number
        else:
            print('не корректный ввод')
        number = input(f'{text} > ')

def data_search(listsearch):
    ''' функция поиска данных'''
    list_fun = [correct_input]
    return [fun(text) for text, fun in zip(listsearch, list_fun)]

def data_change(listchange):
    ''' функция изменения данных'''
    list_fun = [correct_input,correct_input, correct_input]
    return [fun(text) for text, fun in zip(listchange, list_fun)]


def data_input(listfields):
    ''' функция получения данных'''
    list_fun = [correct_input, correct_input, correct_input, correct_input, correct_number, correct_number]
    return [fun(text) for text, fun in zip(listfields, list_fun)]


################ функции для работы со справочником ##################
def look(data):
    ''' Просмотр записей справочника '''
    print(f"Len directory:{len(data)}")
    print(f'Type directory {type(data)}')
    try:
        z = 1
        for obj in data[1:]:
            if len(obj)>20:
                print(f"{z} запись:{obj} \n ")
                print(f'Type {type(obj)}')
                z += 1

    except:
        TypeError(print('Записей нет'))


def search(listsearch,data):
    ''' Поиск по справочнику'''
    database = data_search(listsearch)  # функция получения данных
    client = ' '.join(database[:])
    n = 0
    trigger = 1
    for obj in data:
        if client in obj:
            trigger=0
            n+=1
            print(f'Найдено {n}e совпадение ',obj)
    if trigger:
        print('совпадений не найдено')
        return



def addmember(listfields, data, name):
    ''' Добавление новой записи '''
    database = data_input(listfields)# функция получения данных
    client = ' '.join(database[:2])
    for obj in data:
        if client in obj:
            print('Фамилия и имя существуют ! ! !Выберите другие.')
            return
    memb = str(database)
    #data.append(memb)  # добавляем обьект в список
    try:
        with open(name, 'a', encoding='utf-8') as f:
            f.writelines((memb+ '\n'))
            print('Пользователь добавлен\n##########################')

    except Exception as e:
        print('Error savedata: ',e)
    #savedata(data, name)  # перезаписываем файл c новыми данными

def change(listfields,data,name):
    ''' изменение значения'''
    database = data_change(listfields[:3])  # функция получения данных
    d_b= [i.capitalize() for i in database]
    for obj in data:
        if d_b[0] in obj and d_b[1] in obj and d_b[2] in obj:
            print(f'Найдено совпадение: {obj}')
            database = data_input(listfields)  # функция получения данных
            in_dex = data.index(obj)
            #memb = str(database)
            data[in_dex] = (str(database)+'\n')  # добавляем обьект в список
            print('Пользователь изменён\n##########################')
            savedata(data, name)


def get_pages(data):
    data = data[1:]
    '''Постраничный вывод записей'''
    num_ob = int(input('Введите выводимое количество записей на странице:'))
    num_pg = int(input('Введите номер страницы:'))
    try:
        for i in range((num_ob*(num_pg-1)),(num_ob*num_pg)):
            print(data[i])
    except:
        IndexError(print('------>Последняя запись справочника!!!'))