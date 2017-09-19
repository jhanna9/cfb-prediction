from data_pull import stat_num_reader

# class Stats:
# 	def __init__(self, stat_name_list):
# 		self.stat_name_list = stat_name_list

# 	# def print_names(self):
# 	# 	for name in self.stat_name_list:
# 	# 		print(name[0])

names = list(stat_num_reader('stat_num.txt'))

print(names)

# all_names = Stats(names)

# print(all_names)