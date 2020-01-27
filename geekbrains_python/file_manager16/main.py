import sys

from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_wdir, start_game

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print("Укажите параметры. Для справки - параметр help")
else:

    if command == "list":
        get_list()
    elif command == "create_file":
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == "create_folder":
        try:
            name = sys.argv[2]
            create_folder(name)
        except FileExistsError:
            print('Такая папка уже существует')
    elif command == "delete":
        try:
            name = sys.argv[2]
            delete_file(name)
        except FileNotFoundError:
            print("Этого файла или папки уже не существует")
    elif command == "copy":
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
            copy_file(name, new_name)
        except FileExistsError:
            print('Такая папка уже существует')

    elif command == 'change_dir':
        new_dir = sys.argv[2]
        change_wdir(new_dir)

    elif command == 'game':
        start_game()





    elif command == "help":
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('change_dir - смена рабочей директории')
        print('game - сыграть в игру с компьютером')

    save_info('Конец')
