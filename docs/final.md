---
layout: default
title: Final Report
---

## Video

## Summary
The focus of this project is to train an agent that can successfully complete MineRLNavigateDense-vO from the MineRL competition. In this task, the agent must navigate a forest with the goal of locating a diamond block. The block can be positioned below or above the level of the agent. The agent distinguishes the goal block based on unique visual features compared to surrounding blocks. We chose navigate dense as opposed to navigate, because the dense environment provides a positive/negative reward to the agent every tick based on it's performance, while navigate is more sparse in it's rewarding. 

In our status update, we chose to revise aspects of the GAIL baseline from MineRLLabs in order to see how these changes would improve either the final result of our agent, or the number of episodes to train an agent, or even the time it takes to complete each episode. In our final report, we have chosen to expand on this by introducing further changes to GAIL to see if these will have a substantial impact on the success of our final agent. 

## Approaches
In our previous attempt at improving GAIL we had noticed from observing our agent in early episodes that it would tend to get stuck if surrounded by blocks that resembled diamond (water and sky blocks), so we adjusted the policy update interval by cutting it in half. We inferred that reducing this interval would shorten the episodes in which the agent was stuck, thus improving training time. 

![Image](images/pui.png)

For our final report, we wanted to continue along this same approach, by adjusting various hyperparamaters to find a combination that would deliver a capable agent in the shortest amount of time. To begin with, we realized that our change to the policy update interval was a somewhat arbitrary decision. Cutting it in half showed us that it was a beneficial change, but could we do better? Our group decided to train several agents, each at a different policy update interval: 400, 600, 800, and 1000. We also ran several experiments on how changes to `--discriminator-update-interval` and `--original-reward-weight` would affect the success of our agent. The evaluation section of this report will show the results from these experiments.

Another approach we took was to use the default hyper-parameters of the GAIL agent, but initialize the policy parameters using Behavioral Cloning. This was mentioned in the GAIL paper, and the researchers were confident that doing so would dramatically improve learning speed because BC requires no environment interaction. 

![Pretrain](images/Pretrain.png)


## Evaluation

## References
