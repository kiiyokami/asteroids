import pygame
from constants import *


def main():
    print ("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw asteroids

        # Update the screen
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
  


if __name__ == '__main__':
    main() # main