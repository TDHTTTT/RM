---
layout: default
title:  Status
---

# Project Summary:
The focus of this project is to train an agent that can successfully complete MineRLNavigateDense-vO from the MineRL competition. There are readily available implementations that we can use as a resource in solving this problem, and our goal for this task is to improve upon these implementations to create a superior agent. 

# Approach:
For our approach we began with an implementation of the [GAIL](https://arxiv.org/pdf/1606.03476.pdf) (Generative Adversarial Imitation Learning) algorithm from the set of [baselines](https://github.com/minerllabs/baselines/tree/master/general/chainerrl#getting-started). The GAIL algorithm is an application of a concept called IRL (Inverse Reinforcement Learning), a method used in training an agent to perform a task from the demonstrations of an expert without receiving any reinforcement signal. This is done through finding "a cost function under which the expert is uniquely optimal".
