
def dna (c):
	if c == "C": 
		return 1
	if c == 'T': 
		return 0
	if c == 'A': 
		return 2
	if c == 'G': 
		return 3
	else:
		return 99999

def convDNA( str ):
	return dna(str[2])+4*dna(str[1])+16*dna(str[0])

dividedDNA=[]

_64bitRefKey = "-=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+{}\/<>,.?:;' "

def divideDNA (str):
	s = ""
	j=k=0
	print len(str)
	for i in str:
		s=s+i
		if j%3 == 2:
			dividedDNA.append(s)
			s=""
		if j == len(str):
			dividedDNA.append(s)
		j=j+1


_64bitcode = []

def _64bitdna(str):
	divideDNA(str)
	for i in dividedDNA:
		_64bitcode.append(convDNA(i))

def uncrypt(str):
	return _64bitRefKey[int(str)]

def main():
	answer = ''.join(uncrypt(x) for x in _64bitcode)
	print "ans= "+answer

_64bitdna("GGCTACTAACATGCCTTTCAACTTCCAGGGTTACTGTCAGGGTACTTATGCTCGCATTTACAAGGGCCCTACTCACTGTCAGAAGGGCTTTGGTCTTCAGGGCAATTCAAAAGAGAACCTACCGATCAATCCATCAGAGAACGAGCTTGGATGTGATACCCCTCACGCAGAAACGGCAGTTTGCATGTGGCGCGACAAAGCACCGCTTACGGAATGGATGTCGGGTGTCCGGGATACACTACTGGCTATAACATTCTGTATCAAGGCTCGGGTCGTATGGGTTAGGATGAGGTAGATCTAGAAGCTTTTCTTCCAGGGCCTCTTTTCTACGAGCGAGCCGCGATACACTCAGAATTGCAGCGTACCCTTTCTTGGATTTAACCAAATAAGCATTACCATCTAAACCATAGATATCAATAAACTGAAATGACACCTGCCGTCGGTTCTACCCGATGCGAATGGTTGAATCCGACGCAATTGACGATTCCAGGCCGGGGCACTATGCAGACGCAAAACCAAAATTTGTAATACATGCGCGGGATGCGGTGTAGAGATCTTTAGACGCTAGCCGCTCGGAAAATGTGTTGGTTTTGCCCGTCAGGGCCCTACTCAGGGTCATGGTAATATTGATTAGACGGGTCCCTGCTTCTCGGGCCACCTGGGTTAGGGTTCCAGCCCGTCCAATAGCTAGGTTTTTGATTATAATGCGGGTTACCCGGGTTATACTGACACTGCCCGCTACTATAAAATTCTCCACTGTCATCGTAACCCGAATCTCTTTGATTCTCACTTACTGTCGACGGCTCGGTTCTTCCAAGCACTGCA")
print dividedDNA
print _64bitcode
main()


