#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 10:18:40 2020

@author: pi
"""
#%%
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json


#%%
stjson = pd.read_json("https://covidtracking.com/api/states", orient= 'records')
numcol = 'positive', 'negative', 'pending', 'hospitalized', 'death', 'totalTestResults', 'lastUpdateEt'
us = stjson.set_index('state')
us.sort_values("death", axis = 0, ascending = False, inplace = True, na_position ='last')
states = stjson['state']
#%%
numus = us.loc[:, numcol]
numst = us.loc['AK':'WY', numcol]
numter= us.loc['PR':'VI', numcol]
numus.sort_values("death", axis = 0, ascending = False, inplace = False, na_position ='last')
dex = numus.index
#%%
plt.figure(figsize=(30,10))
# linear
plt.subplot(221)
plt.bar(dex, numus['death'])
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# log
plt.subplot(223)
plt.bar(dex, numus['death'])
plt.yscale('log')
plt.title('log')
plt.grid(True)
