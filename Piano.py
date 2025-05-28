import pygame

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1117, 450))
pygame.display.set_caption('A Pygame Piano')
test_font = pygame.font.Font(None, 50)


title_surface = test_font.render('A Pygame Piano', False, 'White')


piano_surface = pygame.image.load('graphics/Piano.png')
marker_image_raw = pygame.image.load('graphics/Green-Circle.png')
marker_image = pygame.transform.scale(marker_image_raw, (35, 35))




while True:  
    screen.blit(piano_surface, (0, 0))
    screen.blit(title_surface, (430, 50))

    #uhhhhhh it works, will prolly tidy it up later lol
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        screen.blit(marker_image, (147, 215))
    if keys[pygame.K_w]:
        screen.blit(marker_image, (210, 140))
    if keys[pygame.K_e]:
        screen.blit(marker_image, (299, 140))
    if keys[pygame.K_s]:
        screen.blit(marker_image, (235, 215))
    if keys[pygame.K_d]:
        screen.blit(marker_image, (322, 215))
    if keys[pygame.K_f]:
        screen.blit(marker_image, (413, 215))
    if keys[pygame.K_t]:
        screen.blit(marker_image, (473, 140))
    if keys[pygame.K_g]:
        screen.blit(marker_image, (502, 215))
    if keys[pygame.K_y]:
        screen.blit(marker_image, (562, 140))
    if keys[pygame.K_h]:
        screen.blit(marker_image, (587, 215))
    if keys[pygame.K_u]:
        screen.blit(marker_image, (650, 140))
    if keys[pygame.K_j]:
        screen.blit(marker_image, (675, 215))
    if keys[pygame.K_k]:
        screen.blit(marker_image, (764, 215))
    if keys[pygame.K_o]:
        screen.blit(marker_image, (827, 140))
    if keys[pygame.K_l]:
        screen.blit(marker_image, (854, 215))
    if keys[pygame.K_p]:
        screen.blit(marker_image, (916, 140))
    if keys[pygame.K_SEMICOLON]:
        screen.blit(marker_image, (941, 215))
    if keys[pygame.K_QUOTE]:
        screen.blit(marker_image, (1030, 215))

    #dont crash on quit pls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

            


    pygame.display.flip()
    clock.tick(60)