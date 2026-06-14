import pygame
import random

pygame.init()

# ---------------- SETTINGS ----------------
WIDTH, HEIGHT = 900, 600
FPS = 60

ORGANISM_COUNT = 20
ORGANISM_RADIUS = 8
ORGANISM_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (255, 255, 255)

FOOD_COUNT = 50
FOOD_RADIUS = 5
FOOD_COLOUR = (0, 180, 0)

MIN_SPEED = 1
MAX_SPEED = 3
STARTING_ENERGY = 100

# ---------------- SCREEN SETUP ----------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evolution Simulator- 1st version")

clock = pygame.time.Clock()


# ---------------- ORGANISM FUNCTIONS ----------------
def create_organism():
    organism = {
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "speed": random.uniform(MIN_SPEED, MAX_SPEED),
        "energy": STARTING_ENERGY
    }
    return organism


def move_organism(org):
    org["x"] += random.uniform(-org["speed"], org["speed"])
    org["y"] += random.uniform(-org["speed"], org["speed"])

    org["x"] = max(0, min(WIDTH, org["x"]))
    org["y"] = max(0, min(HEIGHT, org["y"]))


def draw_organism(org):
    pygame.draw.circle(
        screen,
        ORGANISM_COLOR,
        (int(org["x"]), int(org["y"])),
        ORGANISM_RADIUS
    )

# ---------------- CREATE ORGANISMS ----------------
organisms = []

for i in range(ORGANISM_COUNT):
    organisms.append(create_organism())

#----------------- CREATE FOOD FUNCTION-------------
def create_food():
    food_item = {
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT)
    }
    return food_item

def draw_food(food_item):
    pygame.draw.circle(
        screen, 
        FOOD_COLOUR,
        (int(food_item["x"]), int(food_item["y"])),
        FOOD_RADIUS
    )

#----------------- CREATE FOOD----------------------
food = []

for i in range(FOOD_COUNT):
    food.append(create_food())


# ---------------- MAIN SIMULATION LOOP ----------------
running = True

while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for org in organisms:
        move_organism(org)
        draw_organism(org)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()