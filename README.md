# Proposal                                                                                                            
                                                                                                                      
## Summary of the Project
The project is based on [MineRL competition][1]. The goal is to use no more than 8,000,000 samples and less than 4 days to train a RL agent to obtain a diamond, which consists of four separate tasks: navigation, treechop, obtain item and survival. Not only does the competition highlight some of the existing challenge in RL such as:
> sparse rewards, long reward horizons and efficient hierarchical planning
>
> -- <cite>MineRL Competition Proposal</cite>

it also challenges competitors to do efficient imitation learning with a tight time and resource budget. Given the scope and difficulty of this project, we may not be able to reach the end goal. So our plan is to tackle the subtasks from the order of difficulty:
+ Navigation
+ Treechop
+ Obtain Item
+ Survival
                                                                                         
                                                                                                                      
## Algorithms
The algorithms to be used are primarily RL with a focus on imitation learning. Since [MineRL competition][1] prohibits any model heavily relying on human domain knowledge, it is important for us to keep it in mind when designing the reward. It might also be possible to use other ML algorithms to facilitate the task, for example behavior cloning might be helpful as the success of [end to end learning of self-driving cars][3] suggests.                                                                                                   
                                                                                                                      
## Evaluation Plan                                                                                                    
The [MineRL competition][1] provides a metric for evaluation:

![metric][2]

Since we might not be able to reach the final task or even many subtasks, we could also use the time it takes for us to reach a certain goal as a metric. 

                                                                                                                      
## Appointment   


[1]: http://minerl.io/competition/
[2]: https://www.ics.uci.edu/~daohangt/metric.png
[3]: https://arxiv.org/pdf/1604.07316.pdf


