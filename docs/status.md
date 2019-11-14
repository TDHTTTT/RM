---
layout: default
title:  Status
---

# Project Summary:
The focus of this project is to train an agent that can successfully complete MineRLNavigateDense-vO from the MineRL competition. In this task, the agent must navigate a forest with the goal of locating a diamond block. The block can be positioned below or above the level of the agent. The agent distinguishes the goal block based on unique visual features compared to surrounding blocks. There are readily available implementations that we can use as a resource in solving this problem, and our goal for this task is to improve upon these implementations to create a superior agent either by increasing it's ability to reach the goal, or reducing the number of episodes necessary to converge. 

# Approach:
For our approach we began with an implementation of the GAIL(Generative Adversarial Imitation Learning) algorithm from a set of baseline functions. The GAIL algorithm is an application of an imitation learning approach called IRL (Inverse Reinforcement Learning), a method used in training an agent to perform a task from the demonstrations of an expert without receiving any reinforcement signal. This is done through finding "a cost function under which the expert is uniquely optimal" on a trajectory dataset, but not telling the learner how to respond to that cost function. GAIL employs both an IRL and RL in it's solution. The optimal solution of the RL in the GAIL algorithm is equivalent to the solution from the IRL cost function. 

![Image](images/IRL.PNG)

The IRL essentially uses a RL to find the lowest cost function out of a set of costs, assigns that cost to the expert policy, and assigns high costs to the rest.  

# Evaluation

# Remaining Goals and Challenges
A huge limitation of the GAIL algorithm is that it is not model based, and thus requires far more interactions to achieve an effective agent. It is also quite computationally complex because it uses an RL in an inner loop, further increasing the time for the algorithm to run its course. Fortunately, there are many other baselines that we can examine. 

Our goal moving foward is to analyze and attempt to improve the Rainbow and PPO algorithms in the context of MineRLNavigateDense-vO, similarly to how we did so for GAIL. The main challenge of these algorithms is their lack of a trajectory data set to help with training the model. 

# Resources Used

[GAIL Algorithm](https://arxiv.org/pdf/1606.03476.pdf)

[Baselines](https://github.com/minerllabs/baselines/tree/master/general/chainerrl#getting-started).
