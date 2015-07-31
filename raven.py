'https://raw.githubusercontent.com/nvictus/python101/master/raven.txt'


fh = open('raven.txt', 'r') 

for line in fh:
	print (line)



"""raven_text = open('raven.txt') 

def word_count(file_name):
	#raven_dict = {}
	
	n = file_name.split()
	print (n)

word_count(raven_text)
	
raven_text.close()"""



	#raven_text.strip()
	#raven_text.rstrip(',')
	#raven_text.rstrip('"')
	#raven_text.lstrip('"')






	#for line in raven_text:
		#print (line)
	#lst = raven_text.split()

	#new_list = []
	#l = len





	#for word in raven_text:
	#	number = raven_text.count(word)



#def count(sequence,item):
#	lst = []
#	for x in sequence: 
#		if item == x:
#			lst.append(1)
#		else:
#			lst.append(0)
#	t = sum(lst)
#	return t

#def remove_duplicates(list_elements):
#	new_list = []
#	l = len(list_elements)
#	for item in list_elements:
#		if item not in new_list:
#			new_list.append(item)
#	return new_list"""