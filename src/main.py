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

    arena = Arena(
        cfg.ARENA_LEFT,
        cfg.ARENA_TOP,
        cfg.ARENA_WIDTH,
        cfg.ARENA_HEIGHT,
        cfg.ARENA_BORDER_THICKNESS,
        cfg.ARENA_BORDER_COLOR
    )

    player_1 = Ball(
        position=(cfg.WINDOW_WIDTH // 4+ 100, cfg.WINDOW_HEIGHT // 2),
        radius=cfg.PLAYER_STARTING_RADIUS,
        color=cfg.RED,
        velocity=(-1, 0),
        mass=1.0
    )

    player_2 = Ball(
        position=(3 * cfg.WINDOW_WIDTH // 4 - 100, cfg.WINDOW_HEIGHT // 2),
        radius=cfg.PLAYER_STARTING_RADIUS,
        color=cfg.BLUE,
        velocity=(1, 1)
    )

    player_3 = Ball(
        position=(cfg.WINDOW_WIDTH // 2, cfg.WINDOW_HEIGHT // 2),
        radius=cfg.PLAYER_STARTING_RADIUS,
        color=cfg.WHITE,
        velocity=(1, 0)
    )

    balls = [player_1, player_2, player_3]

    for i in range(7):
        ball = Ball(
            position=(cfg.WINDOW_WIDTH // 2, cfg.WINDOW_HEIGHT // 2),
            radius=cfg.PLAYER_STARTING_RADIUS,
            color=(200, 200, 0),
            velocity=(0 , 0),
            mass=1.0
        )
        balls.append(ball)

    while True:
        clock.tick(cfg.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(cfg.BACKGROUND_COLOR)
        arena.draw(screen)
        
        for ball in balls:
            ball.move()
            ball.check_wall_collision(arena)
            ball.draw(screen)

        # phys.handle_ball_collision(player_1, player_2)
        
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                phys.handle_ball_collision(balls[i], balls[j])
        pygame.display.flip()