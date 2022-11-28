#!/usr/bin/env python
# coding: utf-8

# #Functions
# 
# This file can be used to write functions that simplify the code

# In[ ]:





# plot function to show a bar chart

# In[9]:


import matplotlib.pyplot as plt
def plot_bar_average(data, savefigure_name, xlabel, ylabel, print_xaxis = True):
    """
    This function created shows a bar plot with the corresponding data
    
    INPUT:
    data (dataframe) - data to be displayed
    savefigure_name (str) - needs a format (.png, .jpg)
    xlabel (str)
    ylabel (str)
    print_xaxis (bool) - if the origin of the x axis is displayed or not
    
    OUTPUT:
    -
    """
    
    data.plot(kind='bar', legend=None);
    if print_xaxis:
        plt.axhline(0, color = "k", linewidth = 0.8)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(savefigure_name)
    plt.show()


# In[10]:


get_ipython().system('jupyter nbconvert --to script functions.ipynb')


# In[ ]:




