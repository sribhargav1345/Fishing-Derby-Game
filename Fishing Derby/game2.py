import pygame
import random
import time
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 180)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fishing Derby Game")


""" <-------- Image loadings  ---------> """

fish_image = pygame.image.load("bluefish.png")
fishr_image = pygame.image.load("bluefish2.png")

fish_image = pygame.transform.scale(fish_image, (25,25))
fishr_image = pygame.transform.scale(fishr_image, (25,25))

fish2_image = pygame.image.load("redfish.png")
fish2r_image = pygame.image.load("redfish2.png")

fish2_image = pygame.transform.scale(fish2_image, (25,25))
fish2r_image = pygame.transform.scale(fish2r_image, (25,25))

background_image = pygame.image.load("background-2.jpg")
background_image = pygame.transform.scale(background_image, (800,600))

test_image = pygame.image.load("test.png")
test_image = pygame.transform.scale(test_image, (2,2))

""" <-------- Image loadings  ---------> """


""" <---------  List of fishes and speeds ----------->  """

fishes = []
fishes2 = []

fish_speed = 0.5           # Blue fish speed
fish2_speed = 0.5         # Red fish speed

""" <---------  List of fishes and speeds ----------->  """


""" <-------- Giving exact coordinates for fishes ----------> """

def fish_movements():
    f1 = [320,430]
    f2 = [170,380]
    f3 = [70,455]
    f4 = [520,505]
    f5 = [745,475]
    f6 = [695,530]
    f7 = [445,555]
    f8 = [145,405]
    fs1 = [f1,f2,f3,f4]
    fs2 = [f5,f6,f7,f8]

    for i in range(4):
        if(i<2):            # Blue wala     
            fishes.append({
                "x": fs1[i][0],
                "y": fs1[i][1],
                "speed": fish_speed,
                "image": fish_image,
                "color": BLUE
            })
        else:               # Red wala
            fishes.append({
                "x": fs1[i][0],
                "y": fs1[i][1],
                "speed": fish2_speed,
                "image": fish2_image,
                "color": RED
            })

    for i in range(4):
        if(i<2):            # Blue wala reverse
            fishes2.append({
                "x": fs2[i][0],
                "y": fs2[i][1],
                "speed": fish_speed,
                "image": fishr_image,
                "color": BLUE
            })
        else:               # Red wala reverse
            fishes2.append({
                "x": fs2[i][0],
                "y": fs2[i][1],
                "speed": fish2_speed,
                "image": fish2r_image,
                "color": RED
            })


# Initialize multiple fish objects
fish_movements()

""" <-------- Giving exact coordinates for fishes ----------> """


score1 = 0
score2 = 0

time_limit = 10

""" <------- Lines defining ---------> """
line_color = RED

# Line 1
start1_x = 75
start1_y = 225

end1_x = 175
end1_y = start1_y

start2_x = 700
start2_y = 225

end2_x = 600
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



""" <------------ Game Loop ---------->"""

running = True
# start_time = pygame.time.get_ticks() 

while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # remaining_time = max(0, time_limit - (pygame.time.get_ticks() - start_time) / 1000)

    """ Only belongs to the line which is hook """

    """
    0 -> move down
    1 -> move right
    2 -> move up
    3 -> move left
    """

    """ <------- 1st agent's hook -------> """

    k = random.choice([0,1,2,3]) 

    if(k==0):
        if(end3_y > 600):
            end3_y = 575
        end3_y += 25
    elif(k==1):
        if(end1_x > 400):
            end1_x = 350
        end1_x += 25
    elif(k==2):
        if(end3_y < 305):
            end3_y = 355
        end3_y -= 25
    elif(k==3):
        if(end1_x < start1_x + 30):
            end1_x = start1_x + 50
        end1_x -= 25
    
    """ <--------- 2nd agent's hook ---------> """

    r = random.choice([0,1,2,3])

    if(k==0):
        if(end4_y > 600):
            end4_y = 575
        end4_y += 25
    if(k==1):
        if(end2_x < 400):
            end2_x = 450
        end2_x -= 25
    elif(k==2):
        if(end4_y < 305):
            end4_y = 355
        end4_y -= 25
    elif(k==3):
        if(end2_x > start2_x - 25):
            end2_x = start2_x - 50
        end2_x += 25

    """ <--------- 2nd agent's hook completed -----------> """
        
    start3_x = end1_x
    start3_y = end1_y
    end3_x = start3_x
 
    start4_x = end2_x
    start4_y = end2_y
    end4_x = start4_x


    """ Only belongs to the line, which is hook"""

    """ <--------- Definition of Collision ----------> """

    def ifIsCollide(co_fx,co_fy,co_sx,co_sy):
        if(abs(co_fx - co_sx)< 20 and abs(co_fy - co_sy) < 20):
            return True
        return False
            
    """ <--------- Definition of Collision ----------> """


    if (score1<50 and score2<50):
        for fish in fishes:
            fish["x"] += fish["speed"] 
            if(fish["x"]>800):
                fish["x"] = 0 
            elif(ifIsCollide(fish["x"],fish["y"],end3_x,end3_y)):
                if(fish["color"]==BLUE):
                    score1 += 20
                else:
                    score1 -= 10
                fish["x"] = 0
            elif(ifIsCollide(fish["x"],fish["y"],end4_x,end4_y)):
                if(fish["color"]==BLUE):
                    score2 += 20
                else:
                    score2 -= 10
                fish["x"] = 0
            if(score1>=50 or score2>=50):
                break

        for fish in fishes2:
            fish["x"] -= fish["speed"] 
            if(fish["x"]<0):
                fish["x"] = 820 
            elif(ifIsCollide(fish["x"],fish["y"],end3_x,end3_y)):
                if(fish["color"]==BLUE):
                    score1 += 20
                else:
                    score1 -= 10
                fish["x"] = 820
            elif(ifIsCollide(fish["x"],fish["y"],end4_x,end4_y)):
                if(fish["color"]==BLUE):
                    score2 += 20
                else:
                    score2 -= 10
                fish["x"] = 820
            if(score1>=50 or score2>=50):
                break

    screen.blit(background_image, (0, 0))
    
    #Draw Grid    
    for i in range(0,800,25):
        for j in range(305,600,25):
            pygame.draw.line(screen, BLACK, (i, j),(800,j), 3)
            pygame.draw.line(screen, BLACK, (i, j),(i,600), 3)
            
    pygame.draw.line(screen, line_color, (start1_x, start1_y), (end1_x, end1_y), 3)
    pygame.draw.line(screen, line_color, (start2_x, start2_y), (end2_x, end2_y), 3)
    pygame.draw.line(screen, line_color, (start3_x, start3_y), (end3_x, end3_y), 3)
    pygame.draw.line(screen, line_color, (start4_x, start4_y), (end4_x, end4_y), 3)

    # Draw fishes
    for fish in fishes:
        screen.blit(fish["image"], (fish["x"], fish["y"]))
    for fish in fishes2:
        screen.blit(fish["image"], (fish["x"], fish["y"]))

    # Display score and time
    font = pygame.font.SysFont("Arial", 32)
    score1_text = font.render(f"Score: {score1}", True, BLACK)
    score2_text = font.render(f"Score: {score2}", True, BLACK)

    # time_text = font.render(f"Time: {int(remaining_time)}", True, BLACK)

    screen.blit(score1_text, (10, 10))
    # screen.blit(time_text, (370, 10))
    screen.blit(score2_text, (680, 10))
    screen.blit(test_image, (75,240))       # Remember, (75,240) are the coordinates of the agent1's hand
    screen.blit(test_image, (300,350))      # (725,250) are the coordinates of agent2's hand
    #screen.blit(test_image, (185,325))


    time.sleep(0.1)
    # Update the display
    pygame.display.flip()

    # Check if the game should end
    # if remaining_time == 0:
    #     running = False

# Display final score
if(score1 >= 50):
    final_score_text = font.render(f"Winner: Player-1", True, RED)
elif(score1 == score2):
    final_score_text = font.render(f"Match Drawn", True, RED)
else:
    final_score_text = font.render(f"Winner: Player-2", True, RED)

screen.blit(final_score_text, (300, 300))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(5000)

pygame.quit()