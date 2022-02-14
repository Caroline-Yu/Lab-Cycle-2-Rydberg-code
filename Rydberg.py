#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:08:07 2022

@author: carolineyu
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
#sin(theta) vs m graph for red
theta_red0=np.array([0,3.03,5.78,9.10,12.2,15.2,-3.2,-6.23,-9.23,-12.3])
theta_red=np.radians(theta_red0)
m_red=np.array([0,1,2,3,4,5,-1,-2,-3,-4])
error=np.array([1,1,1,1,1,1,1,1,1,1])
fit_red,cov_red=np.polyfit(np.sin(theta_red),m_red,1,w=1/error,cov=1)
pred=np.poly1d(fit_red)
plt.plot(np.sin(theta_red),pred(np.sin(theta_red)),'red')
plt.title('order number vs theta for red fringes')
plt.xlabel('sin(theta)')
plt.ylabel('order number')
plt.scatter(np.sin(theta_red),m_red)
plt.show()

#%%
#sin(theta) vs m graph for blue
theta_blue0=np.array([0,2.08,4.23,6.47,8.7,10.9,-2.5,-4.77,-7.03,-9.23])
theta_blue=np.radians(theta_blue0)
m_blue=np.array([0,1,2,3,4,5,-1,-2,-3,-4])
error=np.array([1,1,1,1,1,1,1,1,1,1])
fit_blue,cov_blue=np.polyfit(np.sin(
    theta_blue),m_blue,1,w=1/error,cov=1)
pblue=np.poly1d(fit_blue)
plt.title('order number vs theta for blue fringes')
plt.xlabel('sin(theta)')
plt.ylabel('order number')
plt.plot(np.sin(theta_blue),pblue(np.sin(theta_blue)))
plt.scatter(np.sin(theta_blue),m_blue)
plt.show()
#%%
#sin(theta) vs m graph for purple
theta_purple0=np.array([0,1.72,3.83,-2.28,-4.23,-8.12])
theta_purple=np.radians(theta_purple0)
m_purple=np.array([0,1,2,-1,-2,-4])
error1=np.array([1,1,1,1,1,1])
fit_purple,cov_purple=np.polyfit(np.sin(theta_purple),m_purple,1,w=1/error1,cov=1)
ppurple=np.poly1d(fit_purple)
plt.title('order number vs theta for purple fringes')
plt.xlabel('sin(theta)')
plt.ylabel('order number')
plt.plot(np.sin(theta_purple),ppurple(np.sin(theta_purple)),'purple')
plt.scatter(np.sin(theta_purple),m_purple)
plt.show()
#%%
d=1e-3/80 #because we used the 80lines/mm diffraction grating
lambda_red=d/18.88 #d/fit_red
lambda_blue=d/25.66 #d/fit_blue
lambda_purple=d/28.77 #d/fit_purple

#The n vlaue for each colour can be found by looking up the Balmer series of hydrogen
purple_n=5
blue_n=4
red_n=3

error2=np.array([0.00450681,0.01674557,0.13389705])
#error2 is made up by the 0,0 element of the covariance matrix for each colour
lambdas=np.array([lambda_red,lambda_blue,lambda_purple])
ns=np.array([3,4,5])
plt.scatter(1/(ns)**2-1/(2)**2,1/lambdas)
fit_R,cov_R=np.polyfit(1/(ns)**2-1/(2)**2,1/lambdas,1,w=1/error2,cov=True)
pr=np.poly1d(fit_R)
plt.title('1/wavelength vs 1/n^2 -1/p^2 ')
plt.xlabel('x')
plt.ylabel('1/wavelength(m^-1)')
plt.plot(1/(ns)**2-1/(2)**2,pr(1/(ns)**2-1/(2)**2))
print(fit_R)
#%%
print('the percentage error in our Rydberg constant is',((11156893.2-10973731.6)/10973731.6)*100,'%')

#using the covariance matrix
print('the uncertainty in our Rydberg constant is', np.sqrt(33776389.97979183),'m^-1')
print('the percentage uncertainty in our Rydberg constant is',((5811.745863317823/11156893.2)*100),'%')

#result
print('Our Rydberg constant is 11156893.2 +/- 5811.7 m^-1')
#%%
plt.plot(np.sin(theta_purple),ppurple(np.sin(theta_purple)),'purple')
plt.plot(np.sin(theta_blue),pblue(np.sin(theta_blue)))
plt.plot(np.sin(theta_red),pred(np.sin(theta_red)),'red')
plt.legend(['purple light','blue light','red light'])
plt.xlabel('sin(theta)')
plt.ylabel('order number')
plt.title('order number vs sin(theta)')
plt.show()