"""
Simple script to generate .fasta files with random gene sequences
of 20-100 codons in length.
Gianluca Truda
"""

# Importing useful modules
import random 	# Allows us to generate random numbers.
import hashlib 	# Allows us to 'hash' (so we can create random names for our files).
from datetime import datetime as dt # Allows us to get the current date and time.

nucleotides = ['A','T','C','G'] # Adenosine, Thymine, Cytosine, Guanine nucleotides
rand_num = random.randint(1,99)**random.randint(1,99) # A random number between 1 and 99^99 is generated.
this_name = hashlib.md5(str(rand_num).encode()).hexdigest() # The random number is hashed to create a hexademal string.
# The sequence length must be a multiple of 3 (3 nucleotides to a codon).
seq_length = 3*random.randint(20, 100)	# A sequence of 60 - 600 bases.

# We create a string for the output and give it the FASTA description line.
out_text = "> Random Sequence of length "+str(seq_length)+" | "+str(dt.now())+"\n"

# This loops for each base in our sequence
for i in range(seq_length):
	out_text += nucleotides[random.randint(0, 3)] # Appends a random item from nucleotides array to output string.

with open("fasta/"+this_name+".fasta", 'w') as f: # Opens up a new file named after the hash in write mode.
	f.write(out_text)	# Writes the output string to the file
	# The file is automatically closed ... I think.

# Console message about the file being created, its name, its size.
print("Created "+this_name+".fasta\t"+str(seq_length)+" bp")
