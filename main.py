import pygame
import Scratch_Cat
import Timer
pygame.init()
screen_size = (480, 360)
colors = [(255, 0, 0), (255, 102, 0), (255, 255, 0), (0, 255, 0), (77, 151, 255), (102, 0, 255)]
color = 0
scratch_cat = Scratch_Cat.ScratchCat(screen_size)
meow = pygame.mixer.Sound("Sounds\\Meow.wav")
gameRun = True
pygame.display.set_caption("Pacing Cat")
screen = pygame.display.set_mode(screen_size)
cat1 = pygame.image.load("Images/cat1.png").convert_alpha()
cat2 = pygame.image.load("Images/cat2.png").convert_alpha()
timer1 = Timer.Timer()
timer2 = Timer.Timer()
timer1.reset()
timer2.reset()
clock = pygame.time.Clock()
while gameRun:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
    if scratch_cat.on_edge():
        meow.play()
    if timer1.get_time() > 0.2:
        timer1.reset()
        scratch_cat.switch_costume()
    if timer2.get_time() > 0.3:
        timer2.reset()
        if color < len(colors) - 1:
            color += 1
        else:
            color = 0
    scratch_cat.move(5)
    screen.fill(colors[color])
    if scratch_cat.direction() == "right":
        if scratch_cat.costume() == "cat1":
            screen.blit(cat1, scratch_cat.pos())
        else:
            screen.blit(cat2, scratch_cat.pos())
    else:
        if scratch_cat.costume() == "cat1":
            screen.blit(pygame.transform.flip(cat1, True, False), scratch_cat.pos())
        else:
            screen.blit(pygame.transform.flip(cat2, True, False), scratch_cat.pos())
    pygame.display.update()
pygame.quit()
