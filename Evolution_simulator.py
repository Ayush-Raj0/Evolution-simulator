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


def create_organism():
    return {
        "x": random.randint(
            ORGANISM_RADIUS,
            WIDTH - ORGANISM_RADIUS
        ),
        "y": random.randint(
            ORGANISM_RADIUS,
            HEIGHT - ORGANISM_RADIUS
        ),
        "speed": random.uniform(MIN_SPEED, MAX_SPEED),
        "energy": STARTING_ENERGY
    }


def move_organism(organism):
    organism["x"] += random.uniform(
        -organism["speed"],
        organism["speed"]
    )
    organism["y"] += random.uniform(
        -organism["speed"],
        organism["speed"]
    )

    organism["x"] = max(
        ORGANISM_RADIUS,
        min(WIDTH - ORGANISM_RADIUS, organism["x"])
    )

    organism["y"] = max(
        ORGANISM_RADIUS,
        min(HEIGHT - ORGANISM_RADIUS, organism["y"])
    )


def draw_organism(organism):
    pygame.draw.circle(
        screen,
        ORGANISM_COLOR,
        (int(organism["x"]), int(organism["y"])),
        ORGANISM_RADIUS
    )


def create_food():
    return {
        "x": random.randint(
            FOOD_RADIUS,
            WIDTH - FOOD_RADIUS
        ),
        "y": random.randint(
            FOOD_RADIUS,
            HEIGHT - FOOD_RADIUS
        )
    }


def draw_food(food_item):
    pygame.draw.circle(
        screen,
        FOOD_COLOR,
        (int(food_item["x"]), int(food_item["y"])),
        FOOD_RADIUS
    )


organisms = [
    create_organism()
    for _ in range(ORGANISM_COUNT)
]

foods = [
    create_food()
    for _ in range(FOOD_COUNT)
]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for food_item in foods:
        draw_food(food_item)

    for organism in organisms:
        move_organism(organism)
        draw_organism(organism)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()