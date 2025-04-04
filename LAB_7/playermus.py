import pygame


def run():
    pygame.init()
    pygame.mixer.init()

    window_width = 600
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Music Player")

    font = pygame.font.SysFont("Verdana", 20)

    songs = ['1.mp3', '2.mp3', '3.mp3']
    current_song_index = 0
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()

    def play_next_song():
        nonlocal current_song_index
        current_song_index = (current_song_index + 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play()

    def play_previous_song():
        nonlocal current_song_index
        current_song_index = (current_song_index - 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play()

    def stop_music():
        pygame.mixer.music.stop()

    def play_pause_music():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    running = True
    is_paused = False

    while running:
        window.fill((255, 255, 255))
        status_text = "Playing: " + songs[current_song_index]
        text_surface = font.render(status_text, True, (0, 0, 0))
        window.blit(text_surface, (20, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play_pause_music()
                    is_paused = not is_paused
                elif event.key == pygame.K_n:
                    play_next_song()
                elif event.key == pygame.K_p:
                    play_previous_song()
                elif event.key == pygame.K_s:
                    stop_music()
                    is_paused = True

        pygame.display.flip()

    pygame.quit()


run()
