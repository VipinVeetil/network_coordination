"""
	Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
	I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Paper title: Network Origins of Coordination
	Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2621852
	
	Language: Python
	
	Module name: main
"""


from __future__ import division
import parameters
import agents
import random
import networkx as nx
import sys
import numpy as np
import scipy.stats
import csv
import matplotlib.pyplot as plt

class Model(object):
	def __init__(self):
		self.agents_list = []
		self.number_of_states = parameters.number_of_states
		self.states_list = range(self.number_of_states)
		self.number_of_agents = parameters.number_of_agents
		self.time_steps = parameters.time_steps
		self.measure_system_states_time_interval = parameters.measure_system_states_time_interval
		self.mean_degree = parameters.mean_degree
		self.number_of_games = parameters.number_of_games
		self.epsilon_convergence = 1 - parameters.epsilon
		self.proportion_agents_activated = parameters.proportion_agents_activated
		self.number_of_agents_activated = int(self.proportion_agents_activated * self.number_of_agents)
		self.activated_agents = []
		self.states_dynamics = dict((state, []) for state in range(self.number_of_states))
		self.converged = False
		self.convergence_sequence = []
		self.time_steps_to_convergence = None
		self.number_of_non_convergences = 0
		self.agents_network = []
		self.network_topology = parameters.network_topology
		self.watts_strogatz_rewiring_probability = parameters.watts_strogatz_rewiring_probability


	def create_agents_list(self):
		""" create a list of agents """
		self.agents_list = [agents.Agent() for count in xrange(self.number_of_agents)]

	def assign_attributes(self):
		""" each agent is initialized with a random state """
		for agent in self.agents_list:
			agent.number_of_states = self.number_of_states
			agent.state = random.choice(self.states_list)

	def create_network(self):
		if self.network_topology == "small-world":
			G = nx.watts_strogatz_graph(self.number_of_agents, self.mean_degree, self.watts_strogatz_rewiring_probability)
		elif self.network_topology == "scale-free":
			G = nx.barabasi_albert_graph(self.number_of_agents, int(self.mean_degree/2))
		elif self.network_topology == "ring":
			G = nx.watts_strogatz_graph(self.number_of_agents, self.mean_degree, 0)
		elif self.network_topology == "random":
			G = nx.watts_strogatz_graph(self.number_of_agents, self.mean_degree, 1)

		mapping = dict(enumerate(self.agents_list))
		self.agents_network = nx.relabel_nodes(G, mapping)


	def sample_agents(self):
		self.activated_agents = random.sample(self.agents_list, self.number_of_agents_activated)

	def collect_neighbor_states(self):
		""" each activated agent collected information about the states of its neighbors """
		for agent in self.activated_agents:
			neighbors_states = [neighbor.state for neighbor in self.agents_network.neighbors(agent)]
			agent.update_neighbors_states(neighbors_states)

	def agents_update_state(self):
		""" each agent updates its state """
		for agent in self.activated_agents:
			agent.update_state()

	def return_system_convergence(self):
		states = np.zeros(self.number_of_states, dtype = int)
		for agent in self.agents_list:
			states[agent.state] += 1
		states = states / self.number_of_agents
		return states.max()

	def update_convergence_sequence(self):
		a = self.return_system_convergence()
		self.convergence_sequence.append(a)

	def is_converged(self):
		return self.return_system_convergence() > self.epsilon_convergence

	def update_states_dynamics(self):
		states = np.zeros(self.number_of_states, dtype = int)
		for agent in self.agents_list:
			states[agent.state] += 1
		states = states / self.number_of_agents

		for state in range(self.number_of_states):
			self.states_dynamics[state].append(states[state])

	def one_time_step(self):
		self.sample_agents()
		self.collect_neighbor_states()
		self.agents_update_state()

	def game(self):
		self.create_agents_list()
		self.assign_attributes()
		self.create_network()
		for time in range(self.time_steps):
			self.one_time_step()
			if time % self.measure_system_states_time_interval == 0:
				#self.update_convergence_sequence()
				#self.update_states_dynamics()
				if self.is_converged():
					self.time_steps_to_convergence = time
					return
					""" once the system has converged exit the game """
		self.number_of_non_convergences += 1



"""
plt.plot(model_instance.states_dynamics[0])
plt.plot(model_instance.states_dynamics[1])
plt.plot(model_instance.states_dynamics[2])
plt.xlabel("Time steps", fontsize = 18)
plt.ylabel("Proportion of agents in each state", fontsize = 18)
plt.title("Scale-free network transient dynamics: 10,000 agents, 3 states",fontsize = 20)
plt.grid()
plt.show()
"""



































