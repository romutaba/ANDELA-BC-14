def find_max_min(num):
	#create an empty list
	min_max_list = []
	#assign input to a list
	num_list = num
	#sort the list
	num_list.sort()
	#assign smallest number in list to variable min_num 
	min_num = num_list[0]
	#assign largest number in list to variable max_num 
	max_num = num_list[-1]
	#checks if smallest and largest number are equal and appends to new list
	if (min_num == max_num):
		min_max_list.append(min_num)
	#if the numbers arent equal append to min_max_list and sort list
	else:		
		min_max_list.append(min_num)
		min_max_list.append(max_num)
		min_max_list.sort()
	return (min_max_list)
#print (find_max_min([8,9,908, 8,4]))	
