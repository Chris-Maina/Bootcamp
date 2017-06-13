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



#print(data_type('andela'))
#print(data_type(None))
print(data_type(True))