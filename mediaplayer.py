from prettytable import PrettyTable
from cm import ExcelWrite
import os


class MediaPlayer:
    def __init__(self, name, unc, clips, promo):
        self.name = name
        self.unc = unc
        self.clips = clips
        self.promo_down = promo

    def listdir_promo(self):
        return os.listdir(os.path.join(self.unc, self.promo_down))

    def listdir_clips(self):
        di = {}
        path = os.path.join(self.unc, self.clips)
        listdir = os.listdir(path)
        for i in listdir:
            di[i] = sorted(os.listdir(os.path.join(path, i)))
        return di

    def table_promo(self):
        table = PrettyTable(['№', 'Промо-ролики'])
        k = 1
        for i in self.listdir_promo():
            table.add_row([k, i])
            k += 1
        print(table)

    def get_file(self):
        with ExcelWrite('excel/{}_clips.xls'.format(self.name)) as ex:
            c = 0
            for k, v in self.listdir_clips().items():
                r = 0
                ex.write(r, c, k)
                r += 1
                for i in sorted(v):
                    ex.write(r, c, i)
                    r += 1
                c += 1
