import functools
import random
from copy import copy

import pygame
import math

import numpy as np
from gymnasium.spaces import  *

from pettingzoo import ParallelEnv


class CustomEnvironment(ParallelEnv):

    metadata = {
        "name": "custom_environment_v0",
    }

    def __init__(self):

        self.fm1_y = None
        self.fm1_x = None

        self.fm2_y = None
        self.fm2_x = None   

        self.fishes = {1:[320,430],2:[170,380],3:[70,455],4:[520,505],5:[745,475],6:[695,530],7:[445,555],8:[145,405]}  # Fishes positions
        self.pos = {1:[175,325],2:[600,325]}           # Agent's positions

        self.observation_spaces = dict(zip(self.possible_agents,[MultiDiscrete([]*4)*2]))
        self.action_spaces = dict(zip(self.possible_agents,[Discrete(4)]*2))

        
        self.possible_agents = ["fm1", "fm2"]

        

    def reset(self, seed=None, options=None):

        self.fishes = {1:[320,430],2:[170,380],3:[70,455],4:[520,505],5:[745,475],6:[695,530],7:[445,555],8:[145,405]}  # Fishes positions
        self.pos = {"fm1":[175,325],"fm2":[600,325]}           # Agent's positions

        
        self.score = 0

        self.rewards={"fm1":0,"fm2":0}
        
        self.agents = copy(self.possible_agents)

        observations = {
            a: self.get_obs(a)
            for a in self.agents
        }

        infos = {a: {} for a in self.agents}

        pygame.init()
        pygame.display.set_caption("Fishing Derby Game")
        self.screen = pygame.display.set_mode((800,600))

        self.observation_spaces = observations

        return observations, infos

    def get_obs(self,agent):
        if agent == 'fm1':
            return np.array((self.pos["fm1"][0],self.pos["fm1"][1],self.fishes[1][0],self.fishes[1][1],self.fishes[2][0],self.fishes[2][1],self.fishes[3][0],self.fishes[3][1],self.fishes[4][0],self.fishes[4][1],self.fishes[5][0],self.fishes[5][1],self.fishes[6][0],self.fishes[6][1],self.fishes[7][0],self.fishes[7][1],self.fishes[8][0],self.fishes[8][1]
            ))     # Only have to give fish and agent coordinates
        else:
            return np.array((self.pos["fm2"][0],self.pos["fm2"][1],self.fishes[1][0],self.fishes[1][1],self.fishes[2][0],self.fishes[2][1],self.fishes[3][0],self.fishes[3][1],self.fishes[4][0],self.fishes[4][1],self.fishes[5][0],self.fishes[5][1],self.fishes[6][0],self.fishes[6][1],self.fishes[7][0],self.fishes[7][1],self.fishes[8][0],self.fishes[8][1]
            ))
    
    def step(self, actions):
        terminations = {a: False for a in self.agents}

        def ifIsCollide(co_fx,co_fy,co_sx,co_sy):
            if(abs(co_fx - co_sx)< 20 and abs(co_fy - co_sy) < 20):
                return True
            return False
        
        for agent in self.agents:
            agent_action = actions[agent]
            for fish in self.fishes:
                if ifIsCollide(self.pos[agent][0],self.pos[agent][1],fish[0],fish[1]):
                    self.rewards[agent] += 20
                    fish[1] = fish[1] + 30

            if agent_action == 0 and self.pos[agent][0] > 0:
                self.pos[agent][0] -= 25
            elif agent_action == 1 and self.pos[agent][0] < 499:
                self.pos[agent][0] += 25
            elif agent_action == 2 and self.pos[agent][1] > 0:
                self.pos[agent][1] -= 25
            elif agent_action == 3 and self.pos[agent][1] < 499:
                self.pos[agent][1] += 25
        
            x=self.pos[agent][0]
            y=self.pos[agent][1]

        
        for fish in self.fishes:
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

        for fish in self.fishes:
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

    def render(self):
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

        self.screen.blit(background_image, (0, 0))

        for i in range(0,800,25):
            for j in range(305,600,25):
            pygame.draw.line(self.screen, BLACK, (i, j),(800,j), 3)
            pygame.draw.line(self.screen, BLACK, (i, j),(i,600), 3)
            
        pygame.draw.line(self.screen, line_color, (start1_x, start1_y), (end1_x, end1_y), 3)
        pygame.draw.line(self.screen, line_color, (start2_x, start2_y), (end2_x, end2_y), 3)
        pygame.draw.line(self.screen, line_color, (start3_x, start3_y), (end3_x, end3_y), 3)
        pygame.draw.line(self.screen, line_color, (start4_x, start4_y), (end4_x, end4_y), 3)

        for fish in fishes:
            self.screen.blit(fish["image"], (fish["x"], fish["y"]))
        for fish in fishes2:
            self.screen.blit(fish["image"], (fish["x"], fish["y"]))

        # Display score and time
        font = pygame.font.SysFont("Arial", 32)
        score1_text = font.render(f"Score: {score1}", True, BLACK)
        score2_text = font.render(f"Score: {score2}", True, BLACK)

        time_text = font.render(f"Time: {int(remaining_time)}", True, BLACK)

        self.screen.blit(score1_text, (10, 10))
        self.screen.blit(time_text, (370, 10))
        self.screen.blit(score2_text, (680, 10))
        self.screen.blit(test_image, (75,240))       # Remember, (75,240) are the coordinates of the agent1's hand
        self.screen.blit(test_image, (300,350)) 

        if(score1 > score2):
        final_score_text = font.render(f"Winner: Player-1", True, RED)
        elif(score1 == score2):
            final_score_text = font.render(f"Match Drawn", True, RED)
        else:
            final_score_text = font.render(f"Winner: Player-2", True, RED)

        screen.blit(final_score_text, (300, 300))
        pygame.display.flip()

        pass