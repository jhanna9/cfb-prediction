from data_pull import csv_stat_calc

class Stats:
	def __init__(self, stat_name, stat_mean, stat_stdev):
		self.name = stat_name
		self.mean = stat_mean
		self.stdev = stat_stdev

stat_calc = list(csv_stat_calc())

for s in stat_calc:
	name = str(s[0])
	name = Stats(s[0], s[1], s[2])
	print('Stat: {} \nMean: {} \nStandard Deviation: {} \n'.format(name.name, name.mean, name.stdev))
