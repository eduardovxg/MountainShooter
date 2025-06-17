import pygame

print('Bem vindo ao meu jogo')

pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Bem vindo ao meu jogo fim')

while True:
    # check for all events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
