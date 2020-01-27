# Функция для создания файла
import os, shutil, datetime
import guessing_game_comp


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    os.mkdir(name)


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_wdir(name):
    print(os.getcwd())
    new_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(new_path)
    except FileExistsError:
        print('Эта директория уже существует')
        os.chdir(new_path)
    os.chdir(new_path)
    print(os.getcwd())

def start_game():
    guessing_game_comp


if __name__ == '__main__':
    # create_file('text.dat')
    # create_file('text.dat', 'some text')
    # create_folder('new_f')
    # get_list()
    # get_list(True)
    # # delete_file('new_f')
    # delete_file('text.dat')
    # copy_file('new_f', 'copy_new_f')
    # create_file('text.dat', 'some text')
    # copy_file('text.dat', 'new_text.dat')
    # save_info('abc')
    change_wdir('test_folder')
