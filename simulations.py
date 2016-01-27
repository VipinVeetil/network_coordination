"""
	Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
	I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Paper title: Network Origins of Coordination
	Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2621852
	
	Language: Python
	
	Module name: simulations
"""


from __future__ import division
import main
import parameters
import csv
import numpy as np


with open('scale_free.csv', 'wb') as scale_free:
	for game in xrange(10000):
		print "game", game
		model_instance = main.Model()
		model_instance.network_topology = "scale-free"
		model_instance.game()
		writer = csv.writer(scale_free, delimiter= ',')
		writer.writerow([game] + [model_instance.time_steps_to_convergence])


with open('scale_free_deg.csv', 'wb') as scale_free:
	for degree in np.arange(4, 14, 2):
		print "scale-free", degree, "degree"
		for count in xrange(1000):
			model_instance = main.Model()
			model_instance.network_topology = "scale-free"
			model_instance.mean_degree = degree
			model_instance.game()
			writer = csv.writer(scale_free, delimiter= ',')
			writer.writerow([degree] + [model_instance.time_steps_to_convergence])




