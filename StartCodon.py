# Write a python program to find the position and the translation frame
# (1, 2, or 3) of the first start-codon in the DNA sequence:
	     #gcatcacgttatgtcgactctgtgtggcgtctgctggg

dna_seq = 'gcatcacgttatgtcgactctgtgtggcgtctgctggg'
StartCodon = 'atg'
PositionOfATG = dna_seq.find('atg')
print('Position of Start Codon:', PositionOfATG)

# Which Translation Frame has position 10
# Take position divide it by the number of codons
TranslationFrame = (PositionOfATG) % 3 + 1
print('DNA Sequence:', dna_seq)
print('Position of ATG:', PositionOfATG)
print('Translation Frame:', TranslationFrame) 


