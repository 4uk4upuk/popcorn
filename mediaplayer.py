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
