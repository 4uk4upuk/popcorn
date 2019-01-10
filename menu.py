from functions import *


class Menu:
    def __init__(self, players):
        self.players = players

    def menu_main(self):
        while True:
            q = print_menu_main(self.players)
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
            print_menu_players()
            player = self.players[choice]
            try:
                menu_player_choice = int(input())
            except ValueError:
                menu_player_choice = 0
            if menu_player_choice == 4:
                break
            elif menu_player_choice == 1:
                table_promo(player.listdir_promo())
            elif menu_player_choice == 2:
                get_file(player.name, player.listdir_clips())
            elif menu_player_choice == 3:
                rewrite_promo(player.listdir_clips())

