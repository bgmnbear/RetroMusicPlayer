import os
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

        pygame.mixer.init()

    def get_music_list(self):
        music_path = MUSIC_PATH
        music_list = os.listdir(music_path)
        return music_list

    def load_music(self):
        self.filename = self.filename.encode('utf-8')
        track = pygame.mixer.music.load(self.filename)
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
        self.music_pos = (self.music_pos - 1) % self.music_list_length
        self.start()

    def next_music(self):
        self.music_pos = (self.music_pos + 1) % self.music_list_length
        self.start()

    def start(self):
        self.filename = self.music_list[self.music_pos]
        self.load_music()
        self.play_music()

    def play_or_unpause(self):
        play = self.audio_status.get('play')
        pause = self.audio_status.get('pause')
        if play and pause:
            self.unpause_music()
        else:
            self.start()
