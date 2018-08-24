import threading
from time import sleep

import pygame

# TODO, 重构，增加歌词加载功能
from settings import LYRIC_PATH


class Lyric(object):
    def __init__(self, app):
        self.app = app
        self.lyric = {}
        self.sentence = ''

    def min_to_sec(self, min):
        if min == '' or min is None:
            pass
        else:
            return int(min.split(r':')[0]) * 60 + int(min.split(r':')[1].split(r'.')[0])

    def load_lyric(self):
        self.lyric = {}
        self.sentence = ''
        if self.app.filename is not None:
            try:
                path = self.app.filename.split('.')[0].split('-')[1] + '_歌词.lrc'
                lyric = open(LYRIC_PATH + path, "r", encoding="utf-8")
            except FileNotFoundError:
                self.lyric[str(0)] = '无歌词'
            else:
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

    def start_auto_switch_lyric_thread(self):
        auto_switch_lyric_thread = threading.Thread(target=self.auto_switch_lyric)
        auto_switch_lyric_thread.daemon = True
        auto_switch_lyric_thread.start()

    def auto_switch_lyric(self):
        while True:
            if self.app.music_on_change:
                print(self.app.filename)
                self.load_lyric()
                self.app.music_on_change = False
