arr_list=[]
i=1
for i in range(1,1000001):
	arr_list.extend([(i-1),i])

min_number=min(arr_list)
max_number=max(arr_list)

sum_number=sum(list(arr_list))
print "Smallest number is at index:"+str(min_number)
print "Largest number is at index:"+str(max_number)
print "Sum number = "+str(sum_number)
print "All Array Item are : \n"
print str(arr_list)