"""
	Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
	I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Paper title: Network Origins of Coordination
	Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2621852
	
	Language: Python
	
	Module name: analysis
"""


from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

scale_free_degree = pd.read_csv('scale_free_deg.csv')
scale_free_degree = pd.DataFrame(scale_free_degree)



scale_free_degree_4 = scale_free_degree.loc[scale_free_degree.degree == 4].loc[:, ['time']]
scale_free_degree_4 = scale_free_degree_4['time'].tolist()
scale_free_degree_6 = scale_free_degree.loc[scale_free_degree.degree == 6].loc[:, ['time']]
scale_free_degree_6 = scale_free_degree_6['time'].tolist()
scale_free_degree_8 = scale_free_degree.loc[scale_free_degree.degree == 8].loc[:, ['time']]
scale_free_degree_8 = scale_free_degree_8['time'].tolist()
scale_free_degree_10 = scale_free_degree.loc[scale_free_degree.degree == 10].loc[:, ['time']]
scale_free_degree_10 = scale_free_degree_10['time'].tolist()
scale_free_degree_12 = scale_free_degree.loc[scale_free_degree.degree == 12].loc[:, ['time']]
scale_free_degree_12 = scale_free_degree_12['time'].tolist()


data_scale_free = [scale_free_degree_4, scale_free_degree_6,scale_free_degree_8,scale_free_degree_10,scale_free_degree_12]



a = np.count_nonzero(np.isnan(scale_free_degree_4))
print a
a = np.count_nonzero(np.isnan(scale_free_degree_6))
print a
a = np.count_nonzero(np.isnan(scale_free_degree_8))
print a
a = np.count_nonzero(np.isnan(scale_free_degree_10))
print a
a = np.count_nonzero(np.isnan(scale_free_degree_12))
print a


scale_free_degree_4 = np.array(scale_free_degree_4)
b = scale_free_degree_4[np.logical_not(np.isnan(scale_free_degree_4))]
mean_b = np.mean(b)
cv_b  = np.var(b)
print int(mean_b)
print int(cv_b)

scale_free_degree_6 = np.array(scale_free_degree_6)
b = scale_free_degree_6[np.logical_not(np.isnan(scale_free_degree_6))]
mean_b = np.mean(b)
cv_b  = np.var(b)
print int(mean_b)
print int(cv_b)

scale_free_degree_8 = np.array(scale_free_degree_8)
b = scale_free_degree_8[np.logical_not(np.isnan(scale_free_degree_8))]
mean_b = np.mean(b)
cv_b  = np.var(b)
print int(mean_b)
print int(cv_b)

scale_free_degree_10 = np.array(scale_free_degree_10)
b = scale_free_degree_10[np.logical_not(np.isnan(scale_free_degree_10))]
mean_b = np.mean(b)
cv_b  = np.var(b)
print int(mean_b)
print int(cv_b)

scale_free_degree_12 = np.array(scale_free_degree_12)
b = scale_free_degree_12[np.logical_not(np.isnan(scale_free_degree_12))]
mean_b = np.mean(b)
cv_b  = np.var(b)
print int(mean_b)
print int(cv_b)


plt.boxplot(data_scale_free)
plt.title('Scale-free network convergence - mean degree ',fontsize = 17)
plt.xlabel('Degree',fontsize = 16)
plt.ylabel('Time Steps',fontsize = 16)
plt.xticks([1,2,3,4,5],[4,6,8,10,12])
plt.text(2.75,33000,'Degree')
plt.text(3,31000,'4')
plt.text(3,29000,'6')
plt.text(3,27000,'8')
plt.text(3,25000,'10')
plt.text(3,23000,'12')
plt.text(3.65,35000,'Time to convergence')
plt.text(3.5,33000,'Mean')
plt.text(3.5,31000,'12,439')
plt.text(3.5,29000,'2,888')
plt.text(3.5,27000,'1,712')
plt.text(3.5,25000,'1,311')
plt.text(3.5,23000,'1,118')
plt.text(4.5,33000,'Variance')
plt.text(4.5,31000,'22,029,641')
plt.text(4.5,29000,'488,531')
plt.text(4.5,27000,'139,123')
plt.text(4.5,25000,'129,088')
plt.text(4.5,23000,'17,386')
plt.text(3.8,37000,'10,000 agents')
plt.tick_params(axis='both',labelsize=14)
plt.grid()
plt.show()




scale_free = pd.read_csv('scale_free.csv')
scale_free = scale_free['time']
scale_free = scale_free[np.logical_not(np.isnan(scale_free))]


scale_free_mean = np.mean(scale_free)
scale_free_cv = np.var(scale_free)


print int(scale_free_mean), "scale_free_mean"
print scale_free_cv, "scale_free_cv"


plt.hist(scale_free, 50, facecolor='grey', alpha=0.75)
plt.title('Scale-free network distribution of time to convergence to equilibrium',fontsize = 17)
plt.text(20000,80,'mean = 11,759',fontsize = 14)
plt.text(20000,75, 'coefficient of variation = 0.40',fontsize = 14)
plt.text(20000,70,'non-convergence = 0.2 percent',fontsize = 14)
plt.xlabel('Time steps',fontsize = 16)
plt.ylabel('Frequency',fontsize = 16)
plt.tick_params(axis='both',labelsize=12)
plt.grid()
plt.show()
