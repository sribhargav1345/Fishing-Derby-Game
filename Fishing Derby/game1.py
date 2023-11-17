import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fishing Derby Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 180)

# Load images
fish_image = pygame.image.load("bluefish.png")
fishr_image = pygame.image.load("bluefish2.png")

fish_image = pygame.transform.scale(fish_image, (25,25))
fishr_image = pygame.transform.scale(fishr_image, (25,25))

fish2_image = pygame.image.load("redfish.png")
fish2r_image = pygame.image.load("redfish2.png")

fish2_image = pygame.transform.scale(fish2_image, (25,25))
fish2r_image = pygame.transform.scale(fish2r_image, (25,25))


fish_speed = 0.15
fish2_speed = 0.20

# Define variables
fishes = []
fishes2 = []

# Initialize multiple fish objects
for i in range(8):
    fish_x = random.randint(0, 800)
    fish_y = random.randint(320, 580)
    fish_direction = random.choice([-1, 1])
    if(fish_direction==-1):
        fishes.append({
            "x": fish_x,
            "y": fish_y,
            "speed": fish_speed,
            "direction": fish_direction,
            "image": fishr_image
        })
    else:
        fishes.append({
            "x": fish_x,
            "y": fish_y,
            "speed": fish_speed,
            "direction": fish_direction,
            "image": fish_image
        })

for i in range(4):
    fish2_x = random.randint(0, 800)
    fish2_y = random.randint(320, 580)
    fish2_direction = random.choice([-1, 1])
    if(fish2_direction==-1):
        fishes2.append({
            "x": fish2_x,
            "y": fish2_y,
            "speed": fish2_speed,
            "direction": fish2_direction,
            "image": fish2r_image
        })
    else:
        fishes2.append({
            "x": fish2_x,
            "y": fish2_y,
            "speed": fish2_speed,
            "direction": fish2_direction,
            "image": fish2_image
        })

background_image = pygame.image.load("background-2.jpg")
background_image = pygame.transform.scale(background_image, (800,600))

score = 0
time_limit = 30

# Main game loop
running = True
start_time = pygame.time.get_ticks() 

while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fish2_x -= fish2_speed
            if event.key == pygame.K_RIGHT:
                fish2_x += fish2_speed
            if event.key == pygame.K_UP:
                fish2_y -= fish2_speed
            if event.key == pygame.K_DOWN:
                fish2_y += fish2_speed

    #screen.blit(background_image, (0, 200))
    remaining_time = time_limit - (pygame.time.get_ticks() - start_time) / 1000

    # Update the fish position
    for fish in fishes:
        fish["x"] += fish["speed"] * fish["direction"]
        if fish["x"] > 800:
            fishes.remove(fish)  
        elif fish["x"] < -15:
            fishes.remove(fish)

    for fish in fishes2:
        fish["x"] += fish["speed"] * fish["direction"]
        if fish["x"] > 800:
            fishes2.remove(fish) 
        elif fish["x"] < -15:
            fishes2.remove(fish)

    if remaining_time > 0 and len(fishes) < 10:
        fish_y = random.randint(400, 600)
        fish_direction = random.choice([-1, 1])
        if(fish_direction == -1):
            fish_x = 800
            fishes.append({
            "x": fish_x,
            "y": fish_y,
            "speed": fish_speed,
            "direction": fish_direction,
            "image": fishr_image
        })
        else:
            fish_x = 0
            fishes.append({
            "x": fish_x,
            "y": fish_y,
            "speed": fish_speed,
            "direction": fish_direction,
            "image": fish_image
        })
    
    if remaining_time > 0 and len(fishes2) < 10:
        fish2_y = random.randint(400, 600)
        fish2_direction = random.choice([-1, 1])
        if(fish2_direction == -1):
            fish2_x = 800
            fishes2.append({
            "x": fish2_x,
            "y": fish2_y,
            "speed": fish2_speed,
            "direction": fish2_direction,
            "image": fish2r_image
        })
        else:
            fish2_x = 0
            fishes2.append({
            "x": fish2_x,
            "y": fish2_y,
            "speed": fish2_speed,
            "direction": fish2_direction,
            "image": fish2_image
        })

    # Check for a collision
    if abs(fish_x - fish2_x) < 50 and abs(fish_y - fish2_y) < 50:
        score += 1
        fish_x = random.randint(0, 800)
        fish_y = random.randint(400, 600)

    # Fill the screen
    screen.fill(GREEN)
    screen.blit(background_image, (0, 0))

    for fish in fishes:
        if(fish["direction"]==1):
            screen.blit(fish_image, (fish["x"], fish["y"]))
        else:
            screen.blit(fishr_image, (fish["x"], fish["y"]))
    for fish in fishes2:
        if(fish["direction"]==1):
            screen.blit(fish2_image, (fish["x"], fish["y"]))
        else:
            screen.blit(fish2r_image, (fish["x"], fish["y"]))

    font = pygame.font.SysFont("Arial", 32)
    score_text = font.render(f"Score: {score}", True, WHITE)
    time_text = font.render(f"Time Remaining: {int(remaining_time)}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

pygame.quit()