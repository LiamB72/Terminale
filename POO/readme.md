if you want to secure a variable, you may do:

class Point:

	def __init__(self, abscisse, ordonnee):
		"""
		This secure the variable, meaning you can't access\n
		those variable outside of the class.
		"""
		self.__x, self.__y  = abscisse, ordonnee
		
	def get_value(self,value):
		return self.__value
		
	def set_x(self, a0):
		"""
		This help setting the x variable\n
		to the a0.
		"
		self.__x = x
		
	def set_y(self, a0):
		self.__y = y


Now to decorator:

