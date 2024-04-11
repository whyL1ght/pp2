import pygame

pygame.init()

music_files = ["1.mp3", "2.mp3"]

current_song_index = 0

WINDOW_WIDTH, WINDOW_HEIGHT = 400, 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music Player")

pygame.mixer.music.load(music_files[current_song_index])
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()

    pygame.display.update()

pygame.quit()
