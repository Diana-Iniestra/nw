DNA = 'GATTACA'

def complement(chain):
	changed = ""
	for i in chain:
		if i == 'A':
			changed += 'T'
		elif i == 'T':
			changed += 'A'
		elif i == 'G':
			changed += 'C'
		elif i == 'C':
			changed += 'G'
	print ('The complementary chain for ' + chain + ' is ' + changed + '.')
	
complement(DNA)