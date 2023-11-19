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

        self.score1 = None
        self.score2 = None

        self.l1 = 100
        self.l2 = 100
        self.l3 = 100
        self.l4 = 100

        self.fishes = {1:[320,430],2:[170,380],3:[70,455],4:[520,505],5:[745,475],6:[695,530],7:[445,555],8:[145,405]}

        self.observation_spaces = dict(zip(self.possible_agents,[MultiDiscrete([]*4)*2]))
        self.action_spaces = dict(zip(self.possible_agents,[Discrete(4)]*2))

        self.timestep = 30
        self.possible_agents = ["fm1", "fm2"]

        pass

    def reset(self, seed=None, options=None):

        self.score1 = 0
        self.score2 = 0

        self.l1 = 100
        self.l2 = 100
        self.l3 = 100
        self.l4 = 100

        self.timestep = 30

        observations = {
            a: self.get_obs(a)
            for a in self.possible_agents
        }

        infos = {a: {} for a in self.agents}

        self.observation_spaces = observations

        return observations, infos

    def get_obs(self,agent):
        if agent == 'fm1':
            return tuple(self.score1,self.l1,self.l3,self.timestep)
        else:
            return tuple(self.score2,self.l2,self.l4,self.timestep)

    def step(self, actions):
        pass

    def render(self):
        pass