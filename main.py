import pygame
from constants import * 
from player import Player

def main():
    print("Starting asteroids!")
    pygame.init()

    dt = 0  
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000
        # dt = x / 1000




if __name__ == "__main__":
    main()