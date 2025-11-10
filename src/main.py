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
        color=cfg.YELLOW,
        velocity=(-10, 0),
        health=3
    )

    player_2 = Ball(
        position=(3 * cfg.WINDOW_WIDTH // 4 - 100, cfg.WINDOW_HEIGHT // 2),
        radius=cfg.PLAYER_BASE_RADIUS,
        color=cfg.BLUE,
        velocity=(1, 9),
        health=1
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

    arena.add_health_up()

    while True:
        clock.tick(cfg.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(cfg.BACKGROUND_COLOR)
        
        arena.draw(screen)
        arena.update(screen)

        pygame.display.flip()

        # --- Debugging output ---
        # print player health
        for i, fighter in enumerate(arena.fighters):
            print(f"Fighter {i + 1} Health: {fighter.health}")