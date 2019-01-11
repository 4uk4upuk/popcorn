from mediaplayer import MediaPlayer
from app import App
import json

with open('mediaplayers.json') as file:
    di = json.load(file)
    players = {}
    k = 1
    for i in di:
        players[k] = MediaPlayer(i, di[i]['clips'], di[i]['promo'])
        k += 1

print('Программа для добавления промо-роликов.')
app = App(players)
app.run()
