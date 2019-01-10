from mediaplayer import MediaPlayer
from menu import Menu
import json

with open('mediaplayers.json') as file:
    di = json.load(file)
    players = {}
    k = 1
    for i in di:
        players[k] = MediaPlayer(i, di[i]['unc'], di[i]['clips'], di[i]['promo'])
        k += 1

print('Программа для добавления промо-роликов.')
menu = Menu(players)
menu.menu_main()
