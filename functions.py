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
