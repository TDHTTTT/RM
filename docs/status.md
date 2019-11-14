---
layout: default
title:  Status
---

# Project Summary:
The focus of this project is to train an agent that can successfully complete MineRLNavigateDense-vO from the MineRL competition. In this task, the agent must navigate a forest with the goal of locating a diamond block. The block can be positioned below or above the level of the agent. The agent distinguishes the goal block based on unique visual features compared to surrounding blocks. There are readily available implementations that we can use as a resource in solving this problem, and our goal for this task is to improve upon these implementations to create a superior agent either by increasing it's ability to reach the goal, or reducing the number of episodes necessary to converge. 

# Approach:
For our approach we began with an implementation of the [GAIL](https://arxiv.org/pdf/1606.03476.pdf) (Generative Adversarial Imitation Learning) algorithm from the set of [baselines](https://github.com/minerllabs/baselines/tree/master/general/chainerrl#getting-started). The GAIL algorithm is an application of an imitation learning approach called IRL (Inverse Reinforcement Learning), a method used in training an agent to perform a task from the demonstrations of an expert without receiving any reinforcement signal. This is done through finding "a cost function under which the expert is uniquely optimal", but not telling the learner how to respond to that cost function. GAIL employs both an IRL and RL in it's solution. The optimal solution of the RL in the GAIL algorithm is equivalent to the solution from the IRL cost function. 

![Image](images/IRL.PNG)

Using the GAIL implementation we ran the agent 

# Evaluation

# Remaining Goals and Challenges

# Resources Used
