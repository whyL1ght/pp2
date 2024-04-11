import pygame
import sys
from datetime import datetime
import math
import time

pygame.init()
WIDTH, HEIGHT = 849, 833
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Часы")
clock_img = pygame.image.load("mickeyclock.jpeg")

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now_time = datetime.now()
    h, m, s = now_time.hour, now_time.minute, now_time.second
    screen.blit(clock_img, (0, 0))

    a_h = ((h % 12 + m / 60 + s / 3600) * 360 / 12)
    a_m = ((m + s / 60) * 360 / 60)   
    a_s = (s * 360 / 60)
    h_l = 180
    m_l = 240
    s_l = 320
    h_x = 424 + h_l * math.cos(math.radians(90 - a_h))
    h_y = 416 - h_l * math.sin(math.radians(90 - a_h))
    m_x = 424 + m_l * math.cos(math.radians(90 - a_m))
    m_y = 416 - m_l * math.sin(math.radians(90 - a_m))
    s_x = 424 + s_l * math.cos(math.radians(90 - a_s))
    s_y = 416 - s_l * math.sin(math.radians(90 - a_s))

    pygame.draw.line(screen, (0, 0, 0), (426, 416), (h_x, h_y), 16)
    pygame.draw.line(screen, (255, 0, 0), (426, 416), (m_x, m_y), 8)
    pygame.draw.line(screen, (0, 0, 255), (426, 416), (s_x, s_y), 4)

    pygame.display.flip()
    time.sleep(1)
