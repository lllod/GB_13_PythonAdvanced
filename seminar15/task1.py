# Задача №6 из семинара, которая не была решена.
# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.


import os
import logging
from collections import namedtuple
import argparse

logging.basicConfig(filename='file_info.log', level=logging.INFO)
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def process_directory(directory_path):
    try:
        list_dir = os.listdir(directory_path)
        for i in list_dir:
            path = os.path.join(directory_path, i)
            is_directory = os.path.isdir(path)
            name, extension = os.path.splitext(i) if not is_directory else (i, None)
            parent_directory = os.path.basename(directory_path)
            item_found = FileInfo(name, extension, is_directory, parent_directory)
            logging.info(f'{item_found}')
    except Exception as e:
        logging.error(f'Error! Directory: {directory_path}\n{e}')


def parser():
    cmd_parser = argparse.ArgumentParser()
    cmd_parser.add_argument('directory_path', type=str)
    cmd_path = cmd_parser.parse_args()
    process_directory(cmd_path.directory_path)


if __name__ == "__main__":
    parser()
