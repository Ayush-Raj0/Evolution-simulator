import random
import pygame
import csv
from datetime import datetime


pygame.init()

WIDTH, HEIGHT = 900, 600
FPS = 60

ORGANISM_COUNT = 5
ORGANISM_RADIUS = 8
ORGANISM_COLOR = (0, 0, 255)
MIN_SPEED = 1
MAX_SPEED = 3
SENSING_RANGE = 85

STARTING_ENERGY = 100
ENERGY_LOSS_RATE = 10
SPEED_ENERGY_COST = 1
REPRODUCTION_THRESHOLD = 150
REPRODUCTION_ENERGY_COST = STARTING_ENERGY


FOOD_COUNT = 150
FOOD_RADIUS = 5
FOOD_COLOR = (0, 180, 0)
FOOD_ENERGY_VALUE = 40

BACKGROUND_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Evolution Simulator - Version 4")

clock = pygame.time.Clock()
stats_font = pygame.font.Font(None, 28)


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
        self.generation = 0

    def move(self, target_food):
        if target_food is not None:
            dx = target_food.x - self.x
            dy = target_food.y - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance > 0:
                step = min(self.speed, distance)
                self.x += (dx / distance) * step
                self.y += (dy / distance) * step

        else:
            self.x += random.uniform(-self.speed, self.speed)
            self.y += random.uniform(-self.speed, self.speed)

        self.x = max(
            ORGANISM_RADIUS,
            min(WIDTH - ORGANISM_RADIUS, self.x)
        )
        self.y = max(
            ORGANISM_RADIUS,
            min(HEIGHT - ORGANISM_RADIUS, self.y)
        )
        
    def lose_energy(self, dt):
        energy_loss_rate = ENERGY_LOSS_RATE + self.speed * SPEED_ENERGY_COST
        self.energy -= energy_loss_rate * dt

    def collides_with(self, food_item):
        dx = self.x - food_item.x
        dy = self.y - food_item.y
        distance_squared = dx ** 2 + dy ** 2

        return distance_squared <= (
            ORGANISM_RADIUS + FOOD_RADIUS
        ) ** 2
    
    def eat(self, food_item):
        self.energy += food_item.energy_value

    def sense_food(self, foods):
        nearest_food = None
        nearest_distance_sq = SENSING_RANGE**2
        for food_item in foods:
            dx = food_item.x - self.x
            dy = food_item.y - self.y
            distance_sq = dx**2 + dy**2

            if distance_sq <= nearest_distance_sq:
                nearest_food = food_item
                nearest_distance_sq = distance_sq
        return nearest_food

    def reproduce(self):
        if self.energy >= REPRODUCTION_THRESHOLD:
            child = Organism()
            child.generation = self.generation + 1
            
            child.x=self.x + random.uniform(-20,20)
            child.y=(self.y + random.uniform(-20,20))

            child.x=max(ORGANISM_RADIUS, min(WIDTH - ORGANISM_RADIUS, child.x))
            child.y=max(ORGANISM_RADIUS, min(HEIGHT - ORGANISM_RADIUS, child.y))

            speed_change = random.uniform(-0.2, 0.2)
            child.speed = self.speed + speed_change
            child.speed = max(MIN_SPEED, min(MAX_SPEED, child.speed))

            self.energy -= REPRODUCTION_ENERGY_COST
            return child

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
        self.energy_value = FOOD_ENERGY_VALUE

    def draw(self):
        pygame.draw.circle(
            screen,
            FOOD_COLOR,
            (self.x, self.y),
            FOOD_RADIUS
        )

organisms = [Organism() for _ in range(ORGANISM_COUNT)]
foods = [Food() for _ in range(FOOD_COUNT)]

running = True
elapsed_time = 0
recording_timer = 0
stats_history = []

while running:
    dt = clock.tick(FPS)/1000
    elapsed_time += dt
    recording_timer += dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for food_item in foods:
        food_item.draw()

    for organism in organisms[:]:
        target_food = organism.sense_food(foods)
        organism.move(target_food)
        organism.lose_energy(dt)


        if organism.energy <= 0:
            organisms.remove(organism)
            continue

        for food_item in foods[:]:
            if organism.collides_with(food_item):
                organism.eat(food_item)
                foods.remove(food_item)

        child=organism.reproduce()
        if child is not None:
            organisms.append(child)
       
        organism.draw()
    population_count = len(organisms)
    total_speed = 0
    highest_generation = 0
    for organism in organisms:
        total_speed += organism.speed
        if organism.generation>highest_generation:
            highest_generation = organism.generation
    if population_count>0:
        avg_speed = total_speed/population_count
    else:
        avg_speed = 0

    if recording_timer>=1:
        stats_history.append([
            elapsed_time, 
            population_count, 
            avg_speed
        ])
        recording_timer %= 1


    population_text = stats_font.render(
        "Population: " + str(population_count),
        True, (0,0,0)
    )
    speed_text = stats_font.render(
        "Average Speed: " + str(round(avg_speed, 2)),
        True, (0,0,0)
    )

    if population_count > 0:
        generation_label = str(highest_generation)
    else:
        generation_label = "None"

    generation_text = stats_font.render(
        "Highest gen alive: " + generation_label,
        True, (0,0,0)
    )
    screen.blit(population_text, (10,10))
    screen.blit(speed_text, (10,40))
    screen.blit(generation_text, (10,70))
    
    pygame.display.flip()
pygame.quit()

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
stats_filename = "Simulation_stats_" + timestamp + ".csv"

with open(stats_filename, "w", newline="") as stats_file:
    writer = csv.writer(stats_file)

    writer.writerow([
        "Elapsed_time", 
        "population_count",
        "avg_speed"
    ])

    writer.writerows(stats_history)

settings_filename = "Simulation_settings_" + timestamp + ".csv"

with open(settings_filename, "w", newline="") as settings_file:
    writer = csv.writer(settings_file)
    writer.writerow(["settings", "value"])

    writer.writerows([
        ["ORGANISM_COUNT", ORGANISM_COUNT],
        ["MIN_SPEED", MIN_SPEED],
        ["MAX_SPEED", MAX_SPEED],
        ["SENSING_RANGE", SENSING_RANGE],
        ["STARTING_ENERGY", STARTING_ENERGY],
        ["ENERGY_LOSS_RATE", ENERGY_LOSS_RATE],
        ["SPEED_ENERGY_COST", SPEED_ENERGY_COST],
        ["REPRODUCTION_THRESHOLD", REPRODUCTION_THRESHOLD],
        ["REPRODUCTION_ENERGY_COST", REPRODUCTION_ENERGY_COST],
        ["FOOD_COUNT", FOOD_COUNT],
        ["FOOD_ENERGY_VALUE", FOOD_ENERGY_VALUE]
    ]),