# В файле alastor.py

import argparse

def install_command(args):
    """Обработчик команды AL install."""
    print("Создание директории для библиотеки Alastor...")

def help_command(args):
    """Обработчик команды AL help."""
    print("Список доступных команд:")
    print("AL install - создает директорию для библиотеки Alastor")
    print("AL help - выводит список доступных команд")

def run():
    """Запускает консоль с командами для библиотеки Alastor."""
    parser = argparse.ArgumentParser(description="Консоль с командами для библиотеки Alastor")
    subparsers = parser.add_subparsers(title="Доступные команды", dest="command")

    # Команда AL install
    parser_install = subparsers.add_parser("install", help="Создает директорию для библиотеки Alastor")
    parser_install.set_defaults(func=install_command)

    # Команда AL help
    parser_help = subparsers.add_parser("help", help="Выводит список доступных команд")
    parser_help.set_defaults(func=help_command)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        return

    args.func(args)
