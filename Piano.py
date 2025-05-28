import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption('A Pygame Piano')
test_font = pygame.font.Font(None, 50)


title_surface = test_font.render('A Pygame Piano', False, 'White')

