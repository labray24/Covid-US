#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:46:24 2020

@author: pi
"""
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datascrape import data
#%%
st = pd.DataFrame(data)
st.set_index(['state', 'date'])
#%%
st.sort_values(by=['positive'], ascending=False, inplace=True)
st.head(5) 