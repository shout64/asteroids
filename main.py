import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    pygame.init()

    #Groups
    updateable = pygame.sprite.Group()
    drawable   = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()

    Player.containers        = (updateable, drawable)
    Asteroid.containers      = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)

    dt = 0  
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Instance game objects
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS)
    asteroidspawner = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        updateable.update(dt)
        for i in asteroids:
            if player.is_colliding(i):
                print("Game over!")
                exit()

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()