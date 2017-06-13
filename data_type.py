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
			return "Less than 100"
		if data == 100:
			return "Equal to 100"
		else:
			return "More than 100"
		



#print(data_type('andela'))
#print(data_type(None))
#print(data_type(True))
print(data_type(4034))