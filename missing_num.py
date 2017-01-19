def find_missing (a,b):
	#initial list assignment
	list_a = a
	list_b = b
	return 0 if list_a and list_b == 0 or list_a == list_b else (set(list_b)-set(list_a)).pop()
print (find_missing ([5,4,7,6,11,66],[5,4,1,7,6,11,66]))
print (find_missing([0,8],[0,8,9]))