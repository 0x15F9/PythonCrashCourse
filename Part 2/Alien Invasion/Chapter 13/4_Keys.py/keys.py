import sys, pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((240, 120))
    pygame.display.set_caption("Keys")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print('Key pressed: '+pygame.key.name(event.key))

main()