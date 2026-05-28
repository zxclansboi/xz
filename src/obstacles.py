import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    """Obstacle class"""
    
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))  # Black obstacles
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def update(self):
        """Move obstacle down"""
        self.y += self.velocity
        self.rect.y = self.y
    
    def draw(self, surface):
        """Draw obstacle on surface"""
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.width, self.height))
    
    def is_off_screen(self, screen_height):
        """Check if obstacle is off screen"""
        return self.y > screen_height

class ObstacleManager:
    """Manage obstacle generation and updates"""
    
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.obstacles = []
        self.spawn_timer = 0
        self.spawn_rate = 60  # Spawn every 60 frames
    
    def update(self):
        """Update all obstacles"""
        # Spawn new obstacles
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_rate:
            self.spawn_obstacle()
            self.spawn_timer = 0
        
        # Update existing obstacles
        for obstacle in self.obstacles:
            obstacle.update()
        
        # Remove off-screen obstacles
        self.obstacles = [obs for obs in self.obstacles if not obs.is_off_screen(self.screen_height)]
    
    def spawn_obstacle(self):
        """Spawn a new obstacle"""
        x = random.randint(0, self.screen_width - 60)
        obstacle = Obstacle(x, -40, 60, 40)
        self.obstacles.append(obstacle)
    
    def check_collision(self, player):
        """Check collision between player and obstacles"""
        player_rect = player.get_rect()
        for obstacle in self.obstacles:
            if player_rect.colliderect(pygame.Rect(obstacle.x, obstacle.y, obstacle.width, obstacle.height)):
                return True
        return False
    
    def draw(self, surface):
        """Draw all obstacles"""
        for obstacle in self.obstacles:
            obstacle.draw(surface)
