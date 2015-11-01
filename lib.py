def indicators(dic):
	if dic['indicators'] is None:
		return input("All lit indicators, seperated by spaces: ").lower().split(" ")
	return value



def batteries(dic):
	if dic['batteries'] is None:
		dic['batteries'] = int(input("Number of batteries: "))
