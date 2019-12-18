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

For our final report, we wanted to continue along this same approach, by adjusting various hyperparamaters to find a combination that would deliver a capable agent in the shortest amount of time. To begin with, we realized that our change to the policy update interval was a somewhat arbitrary decision. Cutting it in half showed us that it was a beneficial change, but could we do better? Our group decided to train several agents, each at a different policy update interval: 400, 600, 800, and 1000. We also ran several experiments on how changes to `--discriminator-update-interval` and `--original-reward-weight` would affect the success of our agent. More specifically, for discriminator update interval, we tried 2000, 3000, 4000 and 5000; for original reward weight, we tried 6 and 8. Note that we also trained a baseline model with `--discriminator-update-interval=6000, --policy-update-interval=2000 and, --original-reward-weight=10`, which are the suggested default value from the [basline library][1]. We theorized that the  discriminator update interval functions similarly to the policy update interval in that it will shorten the duration of each episode, potentially decreasing training time. However, we also believed that decreasing this value too much would make it difficult for the agent to learn from each episode with the shortened amount of time. The evaluation section of this report will show the results from these experiments.

Another approach we took was to use the default hyper-parameters of the GAIL agent, but initialize the policy parameters using Behavioral Cloning. This was mentioned in the GAIL paper, and the researchers were confident that doing so would dramatically improve learning speed because BC requires no environment interaction. 

![Pretrain](images/Pretrain.png)

It should also be mentioned that there were two versions of policy optimization that we could use for GAIL: one with Proximal Policy Optimization (PPO) and another with Trust Region Policy Optimization (TRPO). TRPO performs consistenly well, but is too computationally complex to be used in the time we had for this project. Furthermore, PPO offers nearly as good performance at far less a cost, so it was the method we opted for. 

## Evaluation

Amongst other MineRL environments like “MineRLNavigate-vO” and “MineRLNavigateExtreme-vO”, MineRLNavigateDense-vO differs in that it delivers a reward towards the agent for every tick that passes within the current active episode. Based on the current location of the agent, the reward it receives varies in value depending on how far away the agent’s location is relative to the diamond block, the target goal within this environment. Upon reaching the diamond block, the agent is rewarded +100 for completing the task.
As previously mentioned in our approach, we’ve made several different changes to the foundation of the baseline GAIL provided, affecting three hyperparameters; --policy-update-interval, --discriminator-update-interval, and --original-reward-weight with additonal pretraining with behavior cloning. However, how these results compare to the performance of the original baseline itself is what we wish to prioritize and improve upon, with an emphasis towards achieving both higher reward and average policy outputs, all the while attempting for shorter runtimes between each episode the agent is currently attempting to solve. The reasoning behind our focus on the manipulation of these hyperparameters is that we believe they in turn will have a profound effect on not solely the rewards obtained by the agent but how quickly it can respond to the environment it’s placed in. Also, we want to have a robust agent which is less prone to overfitting the expert trajectory. The details regarding each hyperparameter change including explanations for them can be found in their respective section below. We evaluated the performance of our models based on the following 7 metrics: Rewards, Average Policy Value, Runtime, Policy Average Value Loss, Discriminator Average Loss, Policy Average Entropy and Discriminator Average Entropy. 

(BASELINE ANALYSIS TO BE INCLUDED)

One method our group went with towards improving the baseline GAIL was to first change the --policy-update-interval value (PUI for brevity sake) to differ from the default provided. What the PUI does regarding the agent’s performance is based around the expert dataset used within the GAIL algorithm that our agent trains upon. Using Inverse Reinforcement Learning (IRL), our agent’s performance is analyzed using a cost function. This result is compared against various instances of the expert data set that are also analyzed with the IRL cost function, subsequently setting the maximal value obtained to be the new policy that our agent follows. This overall explains how our agent is training/learning within its respective environment. We decided to change these values from the default PUI to 400, 600, 800, and 1000, observing the results of these changes shown in the graphs above. As seen in the “Episodic Reward” graph each change more or less appears to be performing to the same standard as before, however by taking a closer look at the values its shown that PUI-600 delivers the highest average over all rewards collected throughout all episodes with an average of 47.61 (standard deviation not calculated) compared to the rest; PUI-400: 47.03, PUI-800: 47.18, and PUI-1000: 44.84. While interesting, this unfortunately does not compare to the baselines’ best average result of 59.32 +- 30.6. This result in accordance follows that PUI-600 delivers the best policy average value as well visualized within the “Episodic Reward Average” graph, with 17.20 average in comparison to the rest; PUI-400: 15.77, PUI-800: 14.97, and PUI-1000: 14.50. These policy average values show the uptake/rate an agent is improving upon within each episode and the rewards it gathers. Strangely enough, all these results seem to perform under-par with our original change made in the status report when we halved the PUI value, as that change not only gave us higher rewards, but also policy average values that showed the agent was learning at a faster rate than the baseline, something these PUI’s shown here are failing to achieve.

Moving on to our second method towards improving the baseline GAIL, 

### Policy Average Value Loss

### Discriminator Average Loss
<center>![dal](images/all-discriminator_average_loss.png)</center>

<center>Fig.X Discriminator Average Loss</center>

The general trend for all the agents we have tested are the same upward trend, which is not something we want in the ideal case. Ideally, the loss should decrease with more training and finally converge to a stable value. Although it is hard to figure out the reason for such unfavorable behavior, from the metrics of agents with different hyperparameters, we could gain some insights. Firstly, note that with smaller policy update interval, the discriminator tends to have lower loss and thus perform better. On the other hand, with smaller discriminator update interval, the discriminator tends to have higher loss. We think the smaller policy update interval makes the discriminator easier to overfit and have lower loss.

### Policy Average Entropy

### Discriminator Average Entropy

## References

[GAIL Algorithm][1]

[Baselines][2]

[PPO vs TRPO][3]

[1]: https://arxiv.org/pdf/1606.03476.pdf)

[2]: https://github.com/minerllabs/baselines/tree/master/general/chainerrl#getting-started

[3]: https://towardsdatascience.com/introduction-to-various-reinforcement-learning-algorithms-part-ii-trpo-ppo-87f2c5919bb9
