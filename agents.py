from __future__ import division
import random



class Agent(object):
	def __initi__(self):
		self.number_of_states = 0
		""" number of possible states """
		self.state = 0
		""" present state """
		self.frequency_neighbors_states = [0] * self.number_of_states
		""" the number of neighbors that have each of the possible states """

	def update_neighbors_states(self, neighbors_states):
		""" record the states of the neighbors """
		self.frequency_neighbors_states = [0] * self.number_of_states
		for state in neighbors_states:
			self.frequency_neighbors_states[state] += 1

	def update_state(self):
		""" update one's own state to the state that is most frequent among neighbors """
		m = max(self.frequency_neighbors_states)
		max_states = [state for state, x in enumerate(self.frequency_neighbors_states) if x == m]
		""" make a list of the states that have highest frequency, it is possible more than one state has highest frequency """
		self.state = random.choice(max_states)
