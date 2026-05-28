import pygame
import sys
from game import Game

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("XZ - Subway Surfers")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

def main():
    """Main game loop"""
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    running = True
    
    while running:
        clock.tick(FPS)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game.handle_input(event.key)
        
        # Update game state
        game.update()
        
        # Draw everything
        screen.fill((135, 206, 235))  # Sky blue background
        game.draw(screen)
        
        # Update display
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
