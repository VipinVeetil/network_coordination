"""
	Please feel free to use the code without citing or crediting the author(s) mentioned below. Cheers to science :-)
	I'd be happy to hear from you about how to improve this code, and as to how the code may have been useful to you.
	
	Author: Vipin P. Veetil
	Contact: vipin.veetil@gmail.com
	
	Paper title: Network Origins of Coordination
	Paper URL: http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2621852
	
	Language: Python
	
	Module name: parameters
"""

time_steps = 100000

measure_system_states_time_interval = 100
""" the number of time steps that pass between two measures of the system's states """

mean_degree = 6
""" mean of the degree distribution of networks """

number_of_states = 100
""" number of states """

number_of_agents = 10000

number_of_games=1000

epsilon = 0.001
""" the proportion of agents that must have same state before the system is said to converge to equilibrium is 1 - epsilon """

proportion_agents_activated = 0.01
""" the proportion of agents activated every time step """

network_topology = "scale-free"

watts_strogatz_rewiring_probability = 0.5

