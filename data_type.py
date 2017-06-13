"""
function data_type that compares and 
returns results based on argument supllied
"""
def data_type(data):
	if isinstance(data,basestring):
		return len(data)
	