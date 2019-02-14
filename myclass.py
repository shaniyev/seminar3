class my_point:
	def __init__(self, a = 0, b = 0):
		self.a = a
		self.b = b

	def get_value(self):
		return str(self.a) + ', ' + str(self.b)

	def change_att(self):
		self.a = 10
		self.b = 15
		print('a = ', self.a)
		print('b = ', self.b)

	def sum_ab(self):
		return self.a + self.b

	def mult_ab(self):
		return self.a * self.b

class my_point_child(my_point):
	def __init__(self, a = 0, b = 0, n = 0):
		self.a = a
		self.b = b
		self.n = n

	def n_square(self):
		return self.n ** 2

	def print_msg(self):
		print("This is child class method!!!")
