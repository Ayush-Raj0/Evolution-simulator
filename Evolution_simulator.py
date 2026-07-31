import random
import pygame

pygame.init()

WIDTH, HEIGHT = 900, 600
FPS = 60

ORGANISM_COUNT = 20
ORGANISM_RADIUS = 8
ORGANISM_COLOR = (0, 0, 255)

FOOD_COUNT = 50
FOOD_RADIUS = 5
FOOD_COLOR = (0, 180, 0)

BACKGROUND_COLOR = (255, 255, 255)

MIN_SPEED = 1
MAX_SPEED = 3
STARTING_ENERGY = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evolution Simulator - Version 1")

clock = pygame.time.Clock()


class Organism:
    def __init__(self):
        self.x = random.randint(
            ORGANISM_RADIUS,
            WIDTH - ORGANISM_RADIUS
        )
        self.y = random.randint(
            ORGANISM_RADIUS,
            HEIGHT - ORGANISM_RADIUS
        )
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.energy = STARTING_ENERGY

    def move(self):
        self.x += random.uniform(
            -self.speed,
            self.speed
        )
        self.y += random.uniform(
            -self.speed,
            self.speed
        )

        self.x = max(
            ORGANISM_RADIUS,
            min(WIDTH - ORGANISM_RADIUS, self.x)
        )
        self.y = max(
            ORGANISM_RADIUS,
            min(HEIGHT - ORGANISM_RADIUS, self.y)
        )

    def draw(self):
        pygame.draw.circle(
            screen,
            ORGANISM_COLOR,
            (int(self.x), int(self.y)),
            ORGANISM_RADIUS
        )


class Food:
    def __init__(self):
        self.x = random.randint(
            FOOD_RADIUS,
            WIDTH - FOOD_RADIUS
        )
        self.y = random.randint(
            FOOD_RADIUS,
            HEIGHT - FOOD_RADIUS
        )

    def draw(self):
        pygame.draw.circle(
            screen,
            FOOD_COLOR,
            (self.x, self.y),
            FOOD_RADIUS
        )


organisms = [
    Organism()
    for _ in range(ORGANISM_COUNT)
]

foods = [
    Food()
    for _ in range(FOOD_COUNT)
]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for food_item in foods:
        food_item.draw()

    for organism in organisms:
        organism.move()
        organism.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()