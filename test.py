### check output with 
# python ~/script/python/21w1_format_fasta.py -i Ljr_cdna.chr0-6.fa.refined -g 

import os,sys,getopt, re
from C_loadFasta import *

### main argument to 
b=5

def options(argv):
	inputfile = ''
	gff3 = ''
	try:
		opts, args = getopt.getopt(argv,"hi:",["ifile="])
	except getopt.GetoptError:
		print 'python 21w1_format_fasta.py -i <inputfile>'
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print 'python 21w1_format_fasta.py -i <inputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
			
	return inputfile, gff3
    
def add(a):
	print a = a+b 							
		

if __name__ == "__main__":
	gff3 = options(sys.argv[1:])
	a=10
	add(a)
