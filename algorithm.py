def search(array,elementFirst,elementSecond):
    for e in array:
	if e == elementFirst + elementSecond:
		return True
    return False
