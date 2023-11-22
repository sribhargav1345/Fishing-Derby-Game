import os

#import torch
import ray
import supersuit as ss
from ray import tune
from ray.rllib.algorithms.ppo import PPOConfig
from ray.rllib.algorithms.ppo import PPO
from ray.rllib.env.wrappers.pettingzoo_env import ParallelPettingZooEnv
from ray.rllib.models import ModelCatalog
from ray.rllib.models.torch.torch_modelv2 import TorchModelV2
from ray.tune.registry import register_env

from custom_environment import CustomEnvironment
   
def env_creator():
    env = CustomEnvironment()    
    return env


ray.init(ignore_reinit_error=True, num_gpus=1)

env_name = "fish"

register_env(env_name, lambda config: ParallelPettingZooEnv(env_creator()))

env=env_creator()

config = (
        PPOConfig()
        .environment(env="fish", clip_actions=True)
        .rollouts(num_rollout_workers=1)
        .debugging(log_level="ERROR")
        .framework(framework="tf")
        .resources(num_gpus=1)
    )

from ray.rllib.algorithms.algorithm import Algorithm

def new_policy_mapping_fn(agent_id, episode, worker, **kwargs):
    print(agent_id)
    return agent_id


algo_w_2_policies = Algorithm.from_checkpoint(              # Loads checkpoint weights to PPO algorithm
    checkpoint=r"C:\Users\Bhargav\1\PPO\PPO_fish_69eca_00000_0_2023-11-21_11-52-58\checkpoint_000341",
    policy_ids=['default_policy']
)

obs=env.reset()

import time
env.reset()
while True:
    if(type(obs) == type(())):
        fm1 = algo_w_2_policies.compute_single_action(obs[0]['fm1'], policy_id="default_policy")
        fm2 = algo_w_2_policies.compute_single_action(obs[0]['fm2'], policy_id="default_policy")
    else:
        fm1 = algo_w_2_policies.compute_single_action(obs['fm1'], policy_id="default_policy")
        fm2 = algo_w_2_policies.compute_single_action(obs['fm2'], policy_id="default_policy")
    obs, rewards, terminations, truncations, infos = env.step({"fm1": fm1, "fm2": fm2})
    
    env.render()
    print(obs)
    print(terminations, truncations)
    if any(terminations.values()) or all(truncations.values()):
        break
ray.shutdown()
exit()