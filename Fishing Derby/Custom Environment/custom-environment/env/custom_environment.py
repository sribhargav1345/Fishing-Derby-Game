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

        self.possible_agents = ["fm1", "fm2"]
        #self.fishes = {1:[320,430],2:[170,380],3:[70,455],4:[520,505],5:[745,475],6:[695,530],7:[445,555],8:[145,405]}  # Fishes positions
        self.pos = {"fm1":[175,325],"fm2":[600,325]}           # Agent's positions

        self.fishes1 = {1:[320,430],2:[170,380]}    # Blue-LR
        self.fishes2 = {3:[70,455],4:[520,505]}     # Red-LR
        self.fishes3 = {5:[745,475],6:[695,530]}    # Blue-RL
        self.fishes4 = {7:[445,555],8:[145,405]}    # Red-RL

        self.observation_spaces = dict(zip(self.possible_agents,[MultiDiscrete([800]*18)]))
        self.action_spaces = dict(zip(self.possible_agents,[Discrete(4)]*2))

        

        
        pygame.init()
        pygame.display.set_caption("Fishing Derby Game")
        self.screen = pygame.display.set_mode((800,600))

        self.fish_image = pygame.image.load("bluefish.png")
        self.fishr_image = pygame.image.load("bluefish2.png")

        self.fish_image = pygame.transform.scale(self.fish_image, (25,25))
        self.fishr_image = pygame.transform.scale(self.fishr_image, (25,25))

        self.fish2_image = pygame.image.load("redfish.png")
        self.fish2r_image = pygame.image.load("redfish2.png")

        self.fish2_image = pygame.transform.scale(self.fish2_image, (25,25))
        self.fish2r_image = pygame.transform.scale(self.fish2r_image, (25,25))

        self.background_image = pygame.image.load("background-2.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (800,600))

        self.test_image = pygame.image.load("test.png")
        self.test_image = pygame.transform.scale(self.test_image, (2,2))

        

    def reset(self, seed=None, options=None):

        self.fishes1 = {1:[320,430],2:[170,380]}    # Blue-LR
        self.fishes2 = {3:[70,455],4:[520,505]}     # Red-LR
        self.fishes3 = {5:[745,475],6:[695,530]}    # Blue-RL
        self.fishes4 = {7:[445,555],8:[145,405]}    # Red-RL

        self.pos = {"fm1":[175,325],"fm2":[600,325]}           # Agent's positions
        
        self.score = 0

        self.rewards={"fm1":0,"fm2":0}
        
        self.agents = copy(self.possible_agents)

        observations = {
            a: self.get_obs(a)
            for a in self.agents
        }

        infos = {a: {} for a in self.agents}

        self.observation_spaces = observations

        return observations, infos

    def get_obs(self,agent):
        if agent == 'fm1':
            return np.array((self.pos["fm1"][0],self.pos["fm1"][1],self.fishes1[1][0],self.fishes1[1][1],self.fishes1[2][0],self.fishes1[2][1],self.fishes2[3][0],self.fishes2[3][1],self.fishes2[4][0],self.fishes2[4][1],self.fishes3[5][0],self.fishes3[5][1],self.fishes3[6][0],self.fishes3[6][1],self.fishes4[7][0],self.fishes4[7][1],self.fishes4[8][0],self.fishes4[8][1]
            ))     # Only have to give fish and agent coordinates
        else:
            return np.array((self.pos["fm2"][0],self.pos["fm2"][1],self.fishes1[1][0],self.fishes1[1][1],self.fishes1[2][0],self.fishes1[2][1],self.fishes2[3][0],self.fishes2[3][1],self.fishes2[4][0],self.fishes2[4][1],self.fishes3[5][0],self.fishes3[5][1],self.fishes3[6][0],self.fishes3[6][1],self.fishes4[7][0],self.fishes4[7][1],self.fishes4[8][0],self.fishes4[8][1]
            ))
    
    def step(self, actions):
        terminations = {a: False for a in self.agents}

        def ifIsCollide(co_fx,co_fy,co_sx,co_sy):
            if(abs(co_fx - co_sx)< 20 and abs(co_fy - co_sy) < 20):
                return True
            return False
        
        for agent in self.agents:
            agent_action = actions[agent]
            #print(self.pos[agent][0])
            for fish in self.fishes1.values():
                if ifIsCollide(self.pos[agent][0],self.pos[agent][1],fish[0],fish[1]):
                    self.rewards[agent] += 20
                    fish[0] = 0
            for fish in self.fishes2.values():
                if ifIsCollide(self.pos[agent][0],self.pos[agent][1],fish[0],fish[1]):
                    self.rewards[agent] -= 10
                    fish[0] = 0
            for fish in self.fishes3.values():
                if ifIsCollide(self.pos[agent][0],self.pos[agent][1],fish[0],fish[1]):
                    self.rewards[agent] += 20
                    fish[0] = 820
            for fish in self.fishes4.values():
                if ifIsCollide(self.pos[agent][0],self.pos[agent][1],fish[0],fish[1]):
                    self.rewards[agent] -= 10
                    fish[0] = 820
            
            if(agent=="fm1"):
                if agent_action == 0:
                    if(self.pos[agent][1] > 575):
                        self.pos[agent][1] = 550
                    self.pos[agent][1] += 25
                elif agent_action == 1:
                    if(self.pos[agent][0] > 375):
                        self.pos[agent][0] = 350
                    self.pos[agent][0] += 25 
                elif agent_action == 2:
                    if(self.pos[agent][1] < 330):
                        self.pos[agent][1] = 355
                    self.pos[agent][1] -= 25
                elif agent_action == 3:
                    if(self.pos[agent][0] < 205):
                        self.pos[agent][0] = 225
                    self.pos[agent][0] -= 25
            else:
                if agent_action == 0:
                    if(self.pos[agent][1] > 575):
                        self.pos[agent][1] = 550
                    self.pos[agent][1] += 25
                elif agent_action == 1:
                    if(self.pos[agent][0] < 425):
                        self.pos[agent][0] = 450
                    self.pos[agent][0] -= 25 
                elif agent_action == 2:
                    if(self.pos[agent][1] < 330):
                        self.pos[agent][1] = 355
                    self.pos[agent][1] -= 25
                elif agent_action == 3:
                    if(self.pos[agent][0] > 675):
                        self.pos[agent][0] = 650
                    self.pos[agent][0] += 25

        for fish in self.fishes1.values():
            fish[0] += 0.5
            if(fish[0]>800):
                fish[0] = 0
        for fish in self.fishes2.values():
            fish[0] += 0.5
            if(fish[0]>800):
                fish[0] = 0
        for fish in self.fishes3.values():
            fish[0] -= 0.5
            if(fish[0]<0):
                fish[0] = 805
        for fish in self.fishes4.values():
            fish[0] -= 0.5
            if(fish[0]<0):
                fish[0] = 805
        
        if self.rewards["fm1"]>50 or self.rewards["fm2"]>50:
            terminations= {a: True for a in self.agents}

        # Check truncation conditions (overwrites termination conditions)
        truncations = {a: False for a in self.agents}
        
        if any(terminations.values()) or all(truncations.values()):
            self.agents = []

        observations = {
            a: self.get_obs(a)
            for a in self.agents
        }

        # Get dummy infos (not used in this example)
        infos = {a: {} for a in self.agents}

        rewards=self.rewards

        self.render()

        return observations, rewards, terminations, truncations, infos

    def render(self):

        self.screen.blit(self.background_image, (0, 0))

        for i in range(0,800,25):
            for j in range(305,600,25):
                pygame.draw.line(self.screen, (0,0,0), (i, j),(800,j), 3)
                pygame.draw.line(self.screen, (0,0,0), (i, j),(i,600), 3)
            
        pygame.draw.line(self.screen, (255,0,0), (75,225), (self.pos["fm1"][0],225), 3)
        pygame.draw.line(self.screen, (255,0,0), (700,225), (self.pos["fm2"][0], 225), 3)
        pygame.draw.line(self.screen, (255,0,0), (self.pos["fm1"][0], 225), (self.pos["fm1"][0],self.pos["fm1"][1]), 3)
        pygame.draw.line(self.screen, (255,0,0), (self.pos["fm2"][0], 225), (self.pos["fm2"][0],self.pos["fm2"][1]), 3)

        for fish in self.fishes1.values():
            self.screen.blit(self.fish_image, (fish[0], fish[1]))
        for fish in self.fishes2.values():
            self.screen.blit(self.fish2_image, (fish[0], fish[1]))
        for fish in self.fishes3.values():
            self.screen.blit(self.fishr_image, (fish[0], fish[1]))
        for fish in self.fishes4.values():
            self.screen.blit(self.fish2r_image, (fish[0], fish[1]))

        # Display score and time
        font = pygame.font.SysFont("Arial", 32)
        score1_text = font.render(f"Score: {self.rewards['fm1']}", True, (0,0,0))
        score2_text = font.render(f"Score: {self.rewards['fm1']}", True, (0,0,0))

        self.screen.blit(score1_text, (10, 10))
        self.screen.blit(score2_text, (680, 10))
        self.screen.blit(self.test_image, (75,240))       # Remember, (75,240) are the coordinates of the agent1's hand
        self.screen.blit(self.test_image, (300,350))        

        if(self.rewards['fm1'] > self.rewards['fm2']):
            final_score_text = font.render(f"Winner: Player-1", True, (255,0,0))
        elif(self.rewards['fm1'] == self.rewards['fm2']):
            final_score_text = font.render(f"Match Drawn", True, (255,0,0))
        else:
            final_score_text = font.render(f"Winner: Player-2", True, (255,0,0))

        self.screen.blit(final_score_text, (300, 300))
        pygame.display.flip()

        pass