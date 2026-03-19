def play_music_loop(path):
    import pygame
    print("lance la musique")
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)