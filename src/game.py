import pygame
from player import Player
from obstacles import ObstacleManager

class Game:
    """Main game class"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0
        self.game_over = False
        
        # Initialize game objects
        self.player = Player(width // 2, height - 100)
        self.obstacle_manager = ObstacleManager(width, height)
        
    def handle_input(self, key):
        """Handle keyboard input"""
        if key == pygame.K_LEFT:
            self.player.move_left()
        elif key == pygame.K_RIGHT:
            self.player.move_right()
        elif key == pygame.K_UP or key == pygame.K_SPACE:
            self.player.jump()
    
    def update(self):
        """Update game state"""
        if not self.game_over:
            # Update player
            self.player.update(self.width)
            
            # Update obstacles
            self.obstacle_manager.update()
            
            # Check collisions
            if self.obstacle_manager.check_collision(self.player):
                self.game_over = True
            
            # Increase score
            self.score += 1
    
    def draw(self, surface):
        """Draw all game objects"""
        # Draw player
        self.player.draw(surface)
        
        # Draw obstacles
        self.obstacle_manager.draw(surface)
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score // 10}", True, (0, 0, 0))
        surface.blit(score_text, (10, 10))
        
        # Draw game over message
        if self.game_over:
            font = pygame.font.Font(None, 72)
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
            surface.blit(game_over_text, text_rect)
