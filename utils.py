import pygame


def test_end_event():
    pygame.mixer.music.set_pos(250)


def test_get_pos():
    print(pygame.mixer.music.get_pos())
