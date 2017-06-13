class Car():
	def __init__(self,name = 'General',model= 'GM',car_type= 'honda',speed = 0):
		self.name = name
		self.model = model
		self.car_type = car_type
		self.speed = speed
		
		if name== 'Porshe' or name== 'Koenigsegg':
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

		if car_type == 'trailer':
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4

	def is_saloon(self):
		if self.type !=  'trailer':
			self.car_type == 'saloon'
			return True
		else:
			return False

	def drive(self,moving_speed):
		if moving_speed == 3:
			self.speed = 1000
		elif moving_speed == 7:
			self.speed = 77

		
 return self
 

	
	
	
		
	
 

#gm = Car()
#gm.default_car_name