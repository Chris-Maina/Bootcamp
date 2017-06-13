"""
function data_type that compares and 
returns results based on argument supllied
"""
def data_type(data):
	#check for string argument
	if isinstance(data,basestring):
		return len(data)
	#check for None argument
	if data is None:
		return "no value"
	#check for boolean argument
	if isinstance(data,bool):
		return data
	#check for integer argument
	if isinstance(data,int):
		if data < 100 :
			return "less than 100"
		if data == 100:
			return "equal to 100"
		else:
			return "more than 100"
	if isinstance(data,list):
		if len(data)<3:
			return None
		else:
			#return data[2]
			return data.pop(2)
		



#print(data_type('andela'))
#print(data_type(None))
#print(data_type(True))
#print(data_type(4034))
<<<<<<< HEAD
#print(data_type([1,2]))
=======
#print(data_type([1,2]))
>>>>>>> eb181b31329814b227b7d0d3789484fdbbf2ab40
