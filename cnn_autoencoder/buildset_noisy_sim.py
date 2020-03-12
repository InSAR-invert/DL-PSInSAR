#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 12:30:04 2019

@author: subhayanmukherjee
"""

import numpy as np
import matplotlib.pyplot as plt
from simulator import generate_sim
from simulator import coherence
from os import path


sim_cnt = 80*3
ifgsize = [1000,1000]

for loop_idx in range(0, sim_cnt):
    noisy_fname = 'simtdset/noisy_' + str(loop_idx) + '.npy'
    if not path.exists(noisy_fname):
        sim = generate_sim(width=ifgsize[1],height=ifgsize[0])
        sim_cohs = coherence(sim)
        np.save(noisy_fname,sim.ifg_noisy)
    
    print('Finished saving simulated interferogram #' + str(loop_idx+1))
