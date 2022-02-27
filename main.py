import pygame
import os
from Balloon import Balloon
from Monkey import Monkey
from Dart import Dart

WIDTH, HEIGHT = 1500, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon TD")


WHITE = (255, 255, 255)

FPS = 60

POP_BLOON = pygame.USEREVENT + 1


def draw_window(balloons, monkeys, darts):
    WIN.fill(WHITE)

    # Show Balloons
    for b in balloons:
        b_image = pygame.transform.scale(
            b.image, (b.width, b.height))
        WIN.blit(b_image, (b.x, b.y))

    # Show Monkeys
    for m in monkeys:
        m_image = pygame.transform.scale(
            m.image, (m.width, m.height))
        m.draw_radius()
        WIN.blit(m_image, (m.x, m.y))

    # For testing
    balloons[0].move()

    for d in darts:
        d_image = pygame.transform.scale(
            d.image, (d.width, d.height))
        d.move()
        WIN.blit(d_image, (d.x, d.y))
    # if d:
    #     d_image = pygame.transform.scale(
    #         d.image, (d.width, d.height))
    #     if d.active:
    #         d.move()
    #         WIN.blit(d_image, (d.position))

    pygame.display.update()


def main():

    clock = pygame.time.Clock()

    balloons = []
    monkeys = []
    darts = []

    # Initialize
    b = Balloon(0, 0, 1)
    m = Monkey(200, 100, 150, 1, WIN)

    monkeys.append(m)
    balloons.append(b)

    run = True

    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        cur = pygame.time.get_ticks()
        d = m.shoot(b, cur)
        if d:
            darts.append(d)

        draw_window(balloons, monkeys, darts)

    pygame.quit()


if __name__ == "__main__":
    main()
