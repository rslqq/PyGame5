import pygame
import os


def load(name):
    fullname = os.path.join('data', name)
    pic = pygame.image.load(fullname)
    pic = pic.convert_alpha()
    return pic

running = True

size = width, height = 640, 640

pygame.init()

screen = pygame.display.set_mode(size)

image = load("arrow.png")

while running:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_focused():
            screen.blit(image, event.pos)
            pygame.mouse.set_visible(False)
            pygame.display.flip()

pygame.quit()