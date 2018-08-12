import threading

import pygame


# TODO, 重构，增加歌词加载功能
class Lyric(object):
    def __init__(self, app):
        self.app = app
        self.lyric = {}
        self.sentence = ''

        self.get_lyric()

    def min_to_sec(self, min):
        if min == '' or min is None:
            pass
        else:
            return int(min.split(r':')[0]) * 60 + int(min.split(r':')[1].split(r'.')[0])

    def get_lyric(self):
        lyric = open(r"C:\RetroMusicPlayer\lyric\失落沙洲_歌词.lrc", "r", encoding="utf-8")
        l = lyric.read()
        s = l.split(r'[')
        for i in s[1:]:
            a = i.split(r']')
            a[0] = self.min_to_sec(a[0])
            self.lyric[str(a[0])] = a[1]

    def start_update_lyric_thread(self):
        update_lyric_thread = threading.Thread(target=self.lyric_update)
        update_lyric_thread.daemon = True
        update_lyric_thread.start()

    def lyric_update(self):
        while True:
            pos = pygame.mixer.music.get_pos()
            pos = int(pos / 1000)
            if self.lyric.__contains__(str(pos)):
                self.sentence = self.lyric.get(str(pos))
