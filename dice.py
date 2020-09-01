#!/usr/bin/env python

# 1. Central limit theorem (with dice)
# 2. from unfair dice to time distribution
#
#The family of normal distributions is closed under linear transformations: if X {\displaystyle X} X is normally distributed with mean μ {\displaystyle \mu } \mu and standard deviation σ {\displaystyle \sigma } \sigma , then the variable Y = a X + b {\displaystyle Y=aX+b} Y=aX+b, for any real numbers a {\displaystyle a} a and b {\displaystyle b} b, is also normally distributed, with mean a μ + b {\displaystyle a\mu +b} {\displaystyle a\mu +b} and standard deviation | a | σ {\displaystyle |a|\sigma } {\displaystyle |a|\sigma }.

import random
from scipy.stats import skewnorm, norm

FACES = [1, 2, 3, 4, 5, 6]
FAIR_DICE_DIST = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
UNFAIR_DICE_DIST = (0.2, 0.1, 0.1, 0.1, 0.35, 0.15)

# Modified from https://stackoverflow.com/a/479299/200945
#  def roll(dist):
    #  randRoll = random.random()
    #  total = 0
    #  result = 1
    #  for mass in dist:
        #  total += mass
        #  if randRoll < total:
            #  return result
        #  result += 1


def roll(dist, size=None):
    '''this function rolls N dimensional die with biasing provided'''
    return np.random.choice(FACES, size, p=dist)


def roll_n(dist, num_rolls, num_experiments):
    rolls = roll(dist, size=(num_rolls, num_experiments))
    result = np.zeros(len(dist) * num_rolls)
    for cnt in rolls.sum(axis=0):
        result[cnt-1] += 1
    result /= num_experiments
    return result


def durations_pdf():
    x = np.linspace(0, 10, 1000)
    y = skewnorm.pdf(x, 4., -0.25, scale=4)
    return x, y

def sample_durations(count):
    x = skewnorm.rvs(4., -0.25, scale=4, size=count*2)
    return x[x >= 0][:count]


def sample_n(num_issues, story_range = (5, 25)):
    durations = list(sample_durations(num_issues))
    stories = []
    while durations:
        cnt = random.randint(story_range[0], story_range[1])
        s, durations = durations[:cnt], durations[cnt:]
        stories.append(s)

    # In [536]: norm.fit([sum(x)/len(x) for x in stories])
    return stories
