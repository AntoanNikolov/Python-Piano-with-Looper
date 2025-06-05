import pygame
import pygame.midi
pygame.midi.init()
#Make it track the time each key is being held for, and the time for each key between key release and key activation


player = pygame.midi.Output(1) #0 for Windows
player.set_instrument(0)  #id for piano


octave_shift = 0  #octaves shift by 12 midi notes, our default octave is the fourth, so a shift of 0 will leave us there
key_to_note = {
    pygame.K_a: 60, #C
    pygame.K_w: 61, #C#
    pygame.K_s: 62, #D
    pygame.K_e: 63, #D#
    pygame.K_d: 64, #E
    pygame.K_f: 65, #F
    pygame.K_t: 66, #F#
    pygame.K_g: 67, #G
    pygame.K_y: 68, #G#
    pygame.K_h: 69, #A
    pygame.K_u: 70, #A#
    pygame.K_j: 71, #B
    pygame.K_k: 72, #C (next octave)
    pygame.K_o: 73, #C#
    pygame.K_l: 74, #D
    pygame.K_p: 75, #D#
    pygame.K_SEMICOLON: 76, #E
    pygame.K_QUOTE: 77 #F
}

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1117, 450))
pygame.display.set_caption('A Pygame Piano')
test_font = pygame.font.Font(None, 50)


title_surface = test_font.render('A Pygame Piano', False, 'White')


piano_surface = pygame.image.load('graphics/Piano.png')

#default/inital values/blits
octave = 4 
octave_text = f"{octave}"
octave_surface = test_font.render(octave_text, False, 'White')

marker_image_raw = pygame.image.load('graphics/Green-Circle.png')
marker_image = pygame.transform.scale(marker_image_raw, (35, 35))



hold_counter = 0
release_counter = 0
played_keys = [] #note: this is different from pygame.key.get_pressed()
while True:  
    screen.blit(piano_surface, (0, 0))
    screen.blit(title_surface, (430, 50))
    screen.blit(octave_surface, (110,305)) #initally blit it

    #stores whatever keys are pressed
    keys = pygame.key.get_pressed()
    release_counter+=1
    print(release_counter)
    
    for key, note in key_to_note.items(): #go through each key-note relationship

        if keys[key]: #if the key IS being pressed
            
            if key not in played_keys: #and we do not have a record of that key already having started being held. In other words, if this key is being held and we have just now started to hold it
                player.note_on(note + octave_shift, 127) # play note
                played_keys.append(key) #save the fact that we have not let go of this key yet
                release_counter = 0
                print(key)


        else: #if the key is not being pressed
            if key in played_keys: #AND we have a record of that key not being let go of
                player.note_off(note + octave_shift, 127) #tell pygame to stop playing that note
                played_keys.remove(key) #remove it to acknowledge that key has been let go of
                print(f"released {key}")
                hold_counter = 0
    #in other words, checking for pygame.key.get_pressed() will check if the key is being pressed which will result in it being spammed since it is pressed 60 frames per 
    #however, with our list, we instead check if it is STILL being HELD rather than PRESSED
        
    
    
    #uhhhhhh it works, will prolly tidy it up later lol
    if keys[pygame.K_a]:
        screen.blit(marker_image, (147, 215))
        
        hold_counter +=1
        print(hold_counter)
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                octave_shift +=12
                octave+=1

                octave_text = f"{octave}"
                octave_surface = test_font.render(octave_text, False, 'White') #blit it again in here for updated value
            elif event.key == pygame.K_z:
                octave_shift -=12
                octave-=1

                octave_text = f"{octave}"
                octave_surface = test_font.render(octave_text, False, 'White') #blit it again in here for updated value
            #elif event.key == pygame.K_z:



            


    pygame.display.flip()
    clock.tick(60)