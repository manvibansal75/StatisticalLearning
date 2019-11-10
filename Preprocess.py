#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:52:35 2019

@author: manvibansal
"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import random
import glob


path = './StatsData/Kickstarter_2019'# use your path
all_files = glob.glob(path + "/*.csv")

dataset = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    dataset.append(df)

frame = pd.concat(dataset, axis=0, ignore_index=True)

