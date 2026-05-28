import pygame

class Player(pygame.sprite.Sprite):
    """Player character class"""
    
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.velocity_y = 0
        self.is_jumping = False
        self.gravity = 0.6
        self.jump_power = 15
        
        # Create simple rectangle as player sprite
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))  # Red player
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def move_left(self):
        """Move player left"""
        if self.x > 0:
            self.x -= 40
    
    def move_right(self):
        """Move player right"""
        if self.x < 370:  # Assuming 400px width
            self.x += 40
    
    def jump(self):
        """Make player jump"""
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_power
    
    def update(self, screen_width):
        """Update player physics"""
        # Apply gravity
        self.velocity_y += self.gravity
        self.y += self.velocity_y
        
        # Check ground collision
        if self.y >= 560:  # Ground level
            self.y = 560
            self.velocity_y = 0
            self.is_jumping = False
        
        # Update rect position
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self, surface):
        """Draw player on surface"""
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))
    
    def get_rect(self):
        """Get player collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
