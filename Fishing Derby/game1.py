import pygame
import random
import math

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
time_limit = 5

class Hook:
    def __init__(self):
        
        self.anchor_x = 100     # Fixed end
        self.anchor_y = 400

        self.end_x = self.anchor_x          # Movable end
        self.end_y = self.anchor_y - 100

        self.length = 100                   #Min.length

        self.color = BLACK

    def update(self, direction):
        # Adjust the hook's length based on the direction
        if direction == "right":
            self.length += random.randint(1,150)
        elif direction == "left":
            self.length -= random.randint(1,150)
        elif direction == "up":
            self.end_y = self.anchor_y - random.randint(1,150)
        elif direction == "down":
            self.end_y = self.anchor_y + random.randint(1,150)

        # Limit the hook's length to a minimum of 10
        if self.length < 10:
            self.length = 10

        # Update the hook's end point coordinates
        self.end_x = self.anchor_x + (self.length * math.cos(math.radians(90 + direction)))
        self.end_y = self.anchor_y + (self.length * math.sin(math.radians(90 + direction)))

    def draw(self, screen):
        # Draw the hook line
        pygame.draw.line(screen, self.color, (self.anchor_x, self.anchor_y), (self.end_x, self.end_y), 3)


# Main game loop
running = True
start_time = pygame.time.get_ticks() 

while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate remaining time
    remaining_time = max(0, time_limit - (pygame.time.get_ticks() - start_time) / 1000)

    if remaining_time > 0:
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

        # Generate new fishes
        if len(fishes) < 10:
            fish_y = random.randint(400, 600)
            fish_direction = random.choice([-1, 1])
            if fish_direction == -1:
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

        if len(fishes2) < 10:
            fish2_y = random.randint(400, 600)
            fish2_direction = random.choice([-1, 1])
            if fish2_direction == -1:
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
    #screen.fill(GREEN)
    screen.blit(background_image, (0, 0))

    # Draw fishes
    for fish in fishes:
        if fish["direction"] == 1:
            screen.blit(fish_image, (fish["x"], fish["y"]))
        else:
            screen.blit(fishr_image, (fish["x"], fish["y"]))
    for fish in fishes2:
        if fish["direction"] == 1:
            screen.blit(fish2_image, (fish["x"], fish["y"]))
        else:
            screen.blit(fish2r_image, (fish["x"], fish["y"]))

    # Display score and time
    font = pygame.font.SysFont("Arial", 32)
    score_text = font.render(f"Score: {score}", True, BLACK)
    time_text = font.render(f"Time: {int(remaining_time)}", True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (370, 10))
    screen.blit(score_text, (680, 10))

    # Update the display
    pygame.display.flip()

    # Check if the game should end
    if remaining_time == 0:
        running = False

# Display final score
final_score_text = font.render(f"Final Score: {score}", True, RED)
screen.blit(final_score_text, (300, 300))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(5000)

pygame.quit()
