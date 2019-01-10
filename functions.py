from prettytable import PrettyTable
from cm import ExcelWrite


def table_promo(li: list):
    table = PrettyTable(['№', 'Промо-ролики'])
    k = 1
    for i in li:
        table.add_row([k, i])
        k += 1
    print(table)


def get_file(name: str, di: dict):
    with ExcelWrite('{}_clips.xls'.format(name)) as ex:
        c = 0
        for k, v in di.items():
            r = 0
            ex.write(r, c, k)
            r += 1
            for i in sorted(v):
                ex.write(r, c, i)
                r += 1
            c += 1


def print_menu_players():
    print('1. Просмотр загруженных промо-роликов')
    print('2. Выгрузить список клипов в файл')
    print('3. Перезалить промо-ролики')
    print('4. Назад')


def print_menu_main(players: dict):
    print('Выберите медияплеер:')
    for k, v in players.items():
        print('{}. {}'.format(k, v.name))
    print('{}. Выход'.format(len(players) + 1))
    return len(players) + 1


def rewrite_promo(di: list):
    print('Внимание! Все промо-ролики находящиеся в папке "Promo" будут добавлены в плейлист, старые удалены!')
    for i in di:
        print(i)
