import pygame
from ball import Ball
from arena import Arena
import config as cfg
import physics as phys

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT))
    pygame.display.set_caption(cfg.TITLE)
    clock = pygame.time.Clock()

    player_1 = Ball(
        position=(cfg.WINDOW_WIDTH // 4+ 100, cfg.WINDOW_HEIGHT // 2),
        radius=cfg.PLAYER_BASE_RADIUS,
        color=cfg.RED,
        velocity=(-10, 0),
        mass=1.0
    )

    player_2 = Ball(
        position=(3 * cfg.WINDOW_WIDTH // 4 - 100, cfg.WINDOW_HEIGHT // 2),
        radius=cfg.PLAYER_BASE_RADIUS,
        color=cfg.BLUE,
        velocity=(1, 9)
    )

    arena = Arena(
        cfg.ARENA_LEFT,
        cfg.ARENA_TOP,
        cfg.ARENA_WIDTH,
        cfg.ARENA_HEIGHT,
        cfg.ARENA_BORDER_THICKNESS,
        cfg.ARENA_BORDER_COLOR,
        fighters=[player_1, player_2]
    )

    while True:
        clock.tick(cfg.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(cfg.BACKGROUND_COLOR)
        arena.draw(screen)
        
        arena.update_fighters(screen)

        pygame.display.flip()