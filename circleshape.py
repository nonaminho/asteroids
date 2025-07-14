import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def colision(self, other):
        r1 = self.radius
        r2 = other.radius
        colision_dist = r1 + r2

        if self.position.distance_to(other.position) > colision_dist:
            return False
        else:
            return True
