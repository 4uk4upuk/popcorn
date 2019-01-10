class App:
    def __init__(self, players):
        self.players = players

    def run(self):
        while True:
            q = self.print_menu_main()
            try:
                menu_main_choice = int(input())
            except ValueError:
                menu_main_choice = 0
            if menu_main_choice == q:
                break
            if menu_main_choice in self.players:
                self.menu_player(menu_main_choice)

    def menu_player(self, choice):
        while True:
            print('1. Просмотр загруженных промо-роликов')
            print('2. Выгрузить список клипов в файл')
            print('3. Перезалить промо-ролики')
            print('4. Назад')
            player = self.players[choice]
            try:
                menu_player_choice = int(input())
            except ValueError:
                menu_player_choice = 0
            if menu_player_choice == 4:
                break
            elif menu_player_choice == 1:
                player.table_promo()
            elif menu_player_choice == 2:
                player.get_file()
            elif menu_player_choice == 3:
                print('Внимание! Все промо-ролики находящиеся в папке "Promo" будут добавлены в плейлист, старые удалены!')
                for i in player.listdir_clips():
                    print(i)

    def print_menu_main(self):
        print('Выберите медияплеер:')
        for k, v in self.players.items():
            print('{}. {}'.format(k, v.name))
        print('{}. Выход'.format(len(self.players) + 1))
        return len(self.players) + 1