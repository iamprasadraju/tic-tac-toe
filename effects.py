import random

import pygame


class ConfettiEffect:
    def __init__(self, screen, count=200):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.count = count
        self.particles = [self._create_particle() for _ in range(count)]

    def _create_particle(self):
        return {
            "x": random.randint(0, self.width),
            "y": random.randint(-self.height, 0),
            "size": random.randint(6, 15),
            "color": [random.randint(50, 255) for _ in range(3)],
            "speed_y": random.uniform(2, 6),
            "speed_x": random.uniform(-1, 1),
        }

    def update(self):
        for p in self.particles:
            p["x"] += p["speed_x"]
            p["y"] += p["speed_y"]
            if p["y"] > self.height:
                # Reset to top
                p["y"] = random.randint(-50, -10)
                p["x"] = random.randint(0, self.width)

    def draw(self):
        for p in self.particles:
            pygame.draw.rect(
                self.screen,
                p["color"],
                (int(p["x"]), int(p["y"]), p["size"], p["size"]),
            )
