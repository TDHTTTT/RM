#!/bin/env python3

import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import ast
import seaborn as sns

def get_reward(l,xs,ys):
    xs.append(int(l.split()[-2].split(":")[-1]))
    ys.append(float(l.split()[-1].split(":")[-1]))

def get_stats(l,yss):
    l = l[l.find("statistics")+11:]
    l = l.replace("nan","0")
    l = ast.literal_eval(l)
    d = {}
    for lx in l:
        d[lx[0]] = lx[1]
    yss.append(d)
    

def get_statn(stats,n,ys,lkup):
    for l in stats:
        ys.append(l[lkup[n]])


def plot1(X,Y,n):
    fig, ax = plt.subplots()
    ax.plot(X,Y,alpha=0.5)
    ax.set_title(n)
    ax.set_xlabel("Episodes")
    ax.set_ylabel(n)
    plt.show()

def plotN(Xs,Yss,lkup,labels):
    lkup["R"] = "Rewards"
    LINE_STYLES = ['solid', 'dashed', 'dashdot', 'dotted']
    sns.reset_orig()  # get default matplotlib styles back
    clrs = sns.color_palette('husl', n_colors=len(labels))  # a list of RGB tuples
    for k,v in lkup.items():
        if len(labels) < 5:
            fig, ax = plt.subplots()
        else:
            fig, ax = plt.subplots(figsize=(16,6))
        ax.set_title(v)
        ax.set_xlabel("Episodes")
        ax.set_ylabel(v)
        for i in range(len(Xs)):
            ax.plot(Xs[i],Yss[i][k],alpha=0.5,label=labels[i],ls=LINE_STYLES[i%len(LINE_STYLES)],color=clrs[i])
        if len(labels) < 5:
            ax.legend()
        else:
            ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)
           
        if len(labels) < 5:
            plt.savefig(labels[0].split('-')[0]+"-"+v+".png")
        else:
            plt.savefig("all"+"-"+v+".png")
        plt.show()

def main(ns):
    Xs, Yss = [], []
    for n in ns:
        o = open(n,"r")
        X, Ys, Ysst = [], {"R":[],"pav":[],"pae":[],"pavl":[],"papl":[],"pnu":[],
                    "pev":[],"dag":[],"dae":[],"dal":[],"daen":[]}, []
        lkup = {"pav":"policy_average_value","pae":"policy_average_entropy",
                "pavl":"policy_average_value_loss","papl":"policy_average_policy_loss",
                "pnu":"policy_n_updates","pev":"policy_explained_variance",
                "dag":"discriminator_accuracy_gen","dae":"discriminator_accuracy_exp",
                "dal":"discriminator_average_loss","daen":"discriminator_average_entropy"}
        for l in o:
            if "run_evaluation_episodes" in l:
                pass

            else:
                if "R:" in l:
                    get_reward(l, X, Ys["R"])
                elif "statistics:" in l:
                    get_stats(l, Ysst)
            

        for k,v in lkup.items():
            get_statn(Ysst,k,Ys[k],lkup)

        X = np.array(X)
        for k in lkup:
            if 'nan' in Ys[k]:
                print(k,Ys[k].count("nan"))
            Ys[k] = np.array(Ys[k])

        #plot1(X,Ys["R"],"Reward")
        #for k in lkup:
        #    plot1(X,Ys[k],lkup[k])
        Xs.append(X)
        Yss.append(Ys)

    labels = [x.replace(".txt","").replace("log_","") for x in ns]
    print(labels)
    plotN(Xs,Yss,lkup,labels)


if __name__ == "__main__":
    main(sys.argv[1:])


