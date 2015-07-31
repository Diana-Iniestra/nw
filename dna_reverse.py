DNA = 'GATTACA'

def complement(chain):
	changed = ""
	for i in chain:
		if i == 'A':
			changed = 'T' + changed
		elif i == 'T':
			changed = 'A' + changed
		elif i == 'G':
			changed = 'C' + changed
		elif i == 'C':
			changed = 'G' + changed
	print ('The complementary chain for ' + chain + ' is ' + changed + '.')
	
complement(DNA)