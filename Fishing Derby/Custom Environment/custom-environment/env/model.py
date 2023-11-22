"""Uses Ray's RLlib to train agents to play Pistonball.

Author: Rohan (https://github.com/Rohan138)
"""

import os

import ray
import supersuit as ss
from ray import tune
from ray.rllib.algorithms.ppo import PPOConfig
from ray.rllib.env.wrappers.pettingzoo_env import ParallelPettingZooEnv
from ray.rllib.models import ModelCatalog
from ray.rllib.models.torch.torch_modelv2 import TorchModelV2
from ray.tune.registry import register_env
from torch import nn

from custom_environment import CustomEnvironment

    
def env_creator(args):
    env = CustomEnvironment()
    
    # env = ss.dtype_v0(env, "float64")
    # env = ss.normalize_obs_v0(env, env_min=0, env_max=1)
    
    return env

if __name__ == "__main__":
    ray.init(num_gpus=0)

    env_name = "fish"
    register_env(env_name, lambda config: ParallelPettingZooEnv(env_creator(config)))

config = (
        PPOConfig()
        .environment(env="fish", clip_actions=True)
        .rollouts(num_rollout_workers=3)
        .training(
            train_batch_size=512,
            lr=2e-5,
            gamma=0.99,
            lambda_=0.9,
            use_gae=True,
            clip_param=0.4,
            grad_clip=None,
            entropy_coeff=0.1,
            vf_loss_coeff=0.25,
            sgd_minibatch_size=64,
            num_sgd_iter=10,
        )
        .debugging(log_level="ERROR")
        .framework(framework="tf")
        .resources(num_gpus=int(os.environ.get("RLLIB_NUM_GPUS", "0")))
    )


# Get the user's home directory
user_home = os.path.expanduser("~")


downloads_dir = os.path.join(user_home, "1")
local_dir = downloads_dir

print(local_dir)

tune.run(
        "PPO",
        name="PPO",
        stop={"timesteps_total": 5000000},
        checkpoint_freq=10,
        local_dir=downloads_dir,
        config=config.to_dict(),
    )