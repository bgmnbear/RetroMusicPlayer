import os
import threading
from random import randint

import eyed3
import pygame

from settings import MUSIC_PATH


class App:
    def __init__(self):
        self.filename = None
        self.volume = 0.5
        self.volume_offset = 0.1
        self.music_pos = 0
        self.audio_status = {'play': False, 'pause': False, }
        self.music_list = self.get_music_list()
        self.music_list_length = len(self.music_list)
        self.playback_mode = 0
        self.music_end = 0

        pygame.init()
        pygame.mixer.init()

    def get_music_list(self):
        music_path = MUSIC_PATH
        music_list = os.listdir(music_path)
        return music_list

    def load_music(self):
        path = MUSIC_PATH + self.filename
        path = path.encode('utf-8')
        track = pygame.mixer.music.load(path)
        return track

    def play_music(self):
        pygame.mixer.music.play()
        self.audio_status.update(play=True, pause=False)

    def pause_music(self):
        busy = self.get_busy()
        if busy:
            pygame.mixer.music.pause()
            self.audio_status.update(play=True, pause=True)

    def unpause_music(self):
        play = self.audio_status.get('play')
        pause = self.audio_status.get('pause')
        if play and pause:
            pygame.mixer.music.unpause()
            self.audio_status.update(pause=False)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.audio_status.update(play=False, pause=False)

    def get_busy(self):
        return pygame.mixer.music.get_busy()

    def volume_up(self):
        self.volume = self.get_volume() + self.volume_offset
        self.set_volume()

    def volume_down(self):
        self.volume = self.get_volume() - self.volume_offset
        self.set_volume()

    def get_volume(self):
        return pygame.mixer.music.get_volume()

    def set_volume(self):
        pygame.mixer.music.set_volume(self.volume)

    def pre_music(self):
        mode = self.playback_mode
        if mode == 0 or mode == 1:
            self.music_pos = (self.music_pos - 1) % self.music_list_length
            self.start()
        elif mode == 2:
            self.music_pos = randint(0, self.music_list_length - 1)
            self.start()

    def next_music(self):
        mode = self.playback_mode
        if mode == 0 or mode == 1:
            self.music_pos = (self.music_pos + 1) % self.music_list_length
            self.start()
        elif mode == 2:
            self.music_pos = randint(0, self.music_list_length - 1)
            self.start()

    def start(self):
        self.start_auto_switch_thread()
        self.filename = self.music_list[self.music_pos]
        self.load_music()
        self.play_music()

    def start_auto_switch_thread(self):
        auto_switch_thread = threading.Thread(target=self.auto_switch)
        auto_switch_thread.daemon = True
        auto_switch_thread.start()

    def auto_switch(self):
        self.music_end = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(self.music_end)
        while True:
            for event in pygame.event.get():
                if event.type == self.music_end and self.audio_status.get('play'):
                    if self.playback_mode == 1:
                        self.play_music()
                    else:
                        self.next_music()

    def play_or_unpause(self):
        play = self.audio_status.get('play')
        pause = self.audio_status.get('pause')
        if play and pause:
            self.unpause_music()
        else:
            self.start()

    # TODO, some music formats are not supported
    def get_music_duration(self):
        # if self.filename is None:
        #     return 0
        # else:
        #     mp3 = eyed3.load(MUSIC_PATH + self.filename)
        #     time_secs = mp3.info.time_secs
        #     return time_secs
        r = randint(200, 240)
        return r

    def switch_playback_mode(self):
        self.playback_mode = (self.playback_mode + 1) % 3
