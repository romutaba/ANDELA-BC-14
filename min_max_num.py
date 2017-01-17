def find_max_min(num):

	min_max_list = []
	num_list = num
	num_list.sort()
	min_num = num_list[0]
	max_num = num_list[-1]
	
	if (min_num == max_num):
		min_max_list.append(min_num)

	else:		
		min_max_list.append(min_num)
		min_max_list.append(max_num)
		min_max_list.sort()
	return (min_max_list)
#print (find_max_min([8,9,908, 8,4]))	
