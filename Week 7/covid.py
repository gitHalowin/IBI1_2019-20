#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:15:39 2020

@author: halowin
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


os.chdir("/Users/halowin/Desktop/py file")

covid_data = pd.read_csv("full_data.csv")
#print(covid_data.iloc[0:18:3,:])

a = covid_data.loc[:,"location"]
row = []
for i in range(7995):
    if a.loc[i] == 'Afghanistan':
        print ('True')
        row.append(i)
    else:
        print ('False')
A_total_cases = covid_data.loc[row,"total_cases"]
print (A_total_cases)

row1 = []
for i in range(7995):
    if a.loc[i] == 'World':
        row1.append(i)
    else:
        row1 = row1
        
world_dates = covid_data.iloc[row1,0]
world_new_cases = covid_data.iloc[row1,2]
world_new_deaths = covid_data.iloc[row1,3]
mean = np.mean(world_new_cases)
median = np.median(world_new_cases)
print(mean)
print(median)
plt.title("new cases worldwide")
plt.xlabel("date")
plt.boxplot(world_new_cases,meanline = True)
plt.show()
plt.close()


#plt.plot(world_dates,world_new_cases,'b+')
#plt.show()

plt.title('New cases and deaths worldwide')
plt.xlabel('date')
plt.ylabel('number')
plt.plot(world_dates, world_new_cases, color = 'green', label = 'New cases')
plt.plot(world_dates, world_new_deaths, color = 'red', label = 'New deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
legend = plt.legend(loc='upper right', shadow=True)
plt.show()
plt.close()

date = covid_data.loc[:,'date']
row2 = []
for i in range(7995):
    if date.iloc[i] == '2020-03-31':
        row2.append(i)
    else:
        row2 = row2

end_total_cases = covid_data.loc[row2,'total_cases']
row3 = []
for i in row2:
    if end_total_cases.iloc[i] <= 10:
        print(i)
    else:
        print ('False')
low_total_cases = covid_data.loc[row3,'location']
print (low_total_cases)









      
    
      