import pygame
import random
import math

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 180)

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fishing Derby Game")

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
for i in range(4):
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

for i in range(2):
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

test_image = pygame.image.load("test.png")
test_image = pygame.transform.scale(test_image, (2,2))

score = 0
time_limit = 5

""" <------- Lines defining ---------> """
line_color = BLACK

# Line 1
start1_x = 75
start1_y = 230

end1_x = 175
end1_y = start1_y

start2_x = 695
start2_y = 235

end2_x = 595
end2_y = start2_y

# Line 2
start3_x = end1_x
start3_y = end1_y

end3_x = end1_x
end3_y = end1_y + 100

start4_x = end2_x
start4_y = end2_y

end4_x = end2_x
end4_y = end2_y + 100

""" Expanding of lines"""
isExpanding = True
isExpanding2 = True
isExpanding3 = True
isExpanding4 = True

""" <------ Lines defining -------> """

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

    """ Only belongs to the line which is hook """

    k = random.choice([-1, 1])

    if(k==1):
        isExpanding = True
    else:
        isExpanding = False

    if isExpanding:
        if(end1_x>400):
            end1_x = 350
        end1_x += 1
    else:
        if(end1_x<start1_x):
            end1_x = start1_x + 20
        end1_x -= 1

    r = random.choice([-1, 1])

    if(r==1):
        isExpanding2 = True
    else:
        isExpanding2 = False

    if isExpanding2:
        if(end2_x<400):
            end2_x = 450
        end2_x -= 4
    else:
        if(end2_x>start2_x):
            end2_x = start2_x - 20
        end2_x += 4
        
    start3_x = end1_x
    start3_y = end1_y
    end3_x = start3_x
 
    start4_x = end2_x
    start4_y = end2_y
    end4_x = start4_x

    z = random.choice([-1, 1])

    if(z==1):
        isExpanding3 = True
    else:
        isExpanding3 = False

    if isExpanding3:
        if(end3_y>600):
            end3_y = 575
        end3_y += 4
    else:
        if(end3_y<start3_y):
            end3_y = start3_y + 20
        end3_y -= 4

    p = random.choice([-1, 1])

    if(p==1):
        isExpanding4 = True
    else:
        isExpanding4 = False

    if isExpanding4:
        if(end4_y>600):
            end4_y = 575
        end4_y += 4
    else:
        if(end4_y<start4_y):
            end4_y = start4_y + 20
        end4_y -= 4

    """ Only belongs to the line, which is hook"""

    if remaining_time > 0:
        # Update the fish position
        for fish in fishes:
            fish["x"] += fish["speed"] * fish["direction"]
            if fish["x"] > 800:
                fishes.remove(fish)  
            elif fish["x"] < -15:
                fishes.remove(fish)
            
            if(abs(fish["x"] - end3_x) < 30 and abs(fish["y"] - end3_y) < 30):
                score += 2
            # fish_x = random.randint(0, 800)
            # fish_y = random.randint(400, 600)
            if(abs(fish["x"] - end4_x) < 30 and abs(fish["y"] - end4_y) < 30):
                score += 2
            # fish_x = random.randint(0, 800)
            # fish_y = random.randint(400, 600)

        for fish in fishes2:
            fish["x"] += fish["speed"] * fish["direction"]
            if fish["x"] > 800:
                fishes2.remove(fish) 
            elif fish["x"] < -15:
                fishes2.remove(fish)

        # Generate new fishes
        if len(fishes) < 6:
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

        if len(fishes2) < 6:
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
    # if abs(fish_x - fish2_x) < 50 and abs(fish_y - fish2_y) < 50:
    #     score += 1
    #     fish_x = random.randint(0, 800)
    #     fish_y = random.randint(400, 600)
    
    if(abs(fish_x - end3_x) < 30 and abs(fish_y - end3_y) < 30):
        score += 2
        fish_x = random.randint(0, 800)
        fish_y = random.randint(400, 600)
    if(abs(fish2_x - end3_x) < 30 and abs(fish2_y - end3_y) < 30):
        score -= 1
        fish2_x = random.randint(0, 800)
        fish2_y = random.randint(400, 600)
    
    if(abs(fish_x - end4_x) < 30 and abs(fish_y - end4_y) < 30):
        score += 2
        fish_x = random.randint(0, 800)
        fish_y = random.randint(400, 600)
    if(abs(fish2_x - end4_x) < 30 and abs(fish2_y - end4_y) < 30):
        score -= 1
        fish2_x = random.randint(0, 800)
        fish2_y = random.randint(400, 600)

    # Fill the screen
    #screen.fill(GREEN)
    screen.blit(background_image, (0, 0))

    pygame.draw.line(screen, line_color, (start1_x, start1_y), (end1_x, end1_y), 3)
    pygame.draw.line(screen, line_color, (start2_x, start2_y), (end2_x, end2_y), 3)
    pygame.draw.line(screen, line_color, (start3_x, start3_y), (end3_x, end3_y), 3)
    pygame.draw.line(screen, line_color, (start4_x, start4_y), (end4_x, end4_y), 3)

    # left vertical
    #right vertical

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
    screen.blit(test_image, (75,240))       # Remember, (75,240) are the coordinates of the agent1's hand
    screen.blit(test_image, (725,250))      # (725,250) are the coordinates of agent2's hand

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







# class Hook:
#     def __init__(self):
        
#         self.anchor_x = 100     # Fixed end
#         self.anchor_y = 400

#         self.end_x = self.anchor_x          # Movable end
#         self.end_y = self.anchor_y - 100

#         self.length = 100                   #Min.length

#         self.color = BLACK

#     def update(self, direction):
#         # Adjust the hook's length based on the direction
#         if direction == "right":
#             self.length += random.randint(1,150)
#         elif direction == "left":
#             self.length -= random.randint(1,150)
#         elif direction == "up":
#             self.end_y = self.anchor_y - random.randint(1,150)
#         elif direction == "down":
#             self.end_y = self.anchor_y + random.randint(1,150)

#         # Limit the hook's length to a minimum of 10
#         if self.length < 10:
#             self.length = 10

#         # Update the hook's end point coordinates
#         self.end_x = self.anchor_x + (self.length * math.cos(math.radians(90 + direction)))
#         self.end_y = self.anchor_y + (self.length * math.sin(math.radians(90 + direction)))

#     def draw(self, screen):
#         # Draw the hook line
#         pygame.draw.line(screen, self.color, (self.anchor_x, self.anchor_y), (self.end_x, self.end_y), 3)