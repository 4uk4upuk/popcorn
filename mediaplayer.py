from prettytable import PrettyTable
from cm import ExcelWrite
import os
import re


class MediaPlayer:
    def __init__(self, name, clips, promo):
        self.name = name
        self.clips = clips
        self.promo = promo

    def listdir_promo(self):
        return os.listdir(self.promo)

    def listdir_clips(self):
        di = {}
        listdir = os.listdir(self.clips)
        for i in listdir:
            di[i] = sorted(os.listdir(os.path.join(self.clips, i)))
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

    def rewrite_promo(self):
        for i in self.listdir_clips():
            print(i)

    def rename_without_num(self):
        for folder, clips in self.listdir_clips().items():
            full_path_folder = os.path.join(self.clips, folder)
            for clip in clips:
                if re.search('promo', clip):
                    os.remove(os.path.join(full_path_folder, clip))
                else:
                    try:
                        clip_old = os.path.join(full_path_folder, clip)
                        clip_new = os.path.join(full_path_folder, '{}'.format(clip.split(' ')[1]))
                        os.rename(clip_old, clip_new)
                    except:
                        pass
