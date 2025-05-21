# Start-Codon-Position-and-Translation-Frame
The program finds the position and the translation frame of the start codon 'ATG'

I used the .find function to find the position that ATG appears on in the string.  I then used this position and divided it by 3 since a codon is made up of 3 nucleotides.  I added 1 to this because I am adding back the fact that strings start with a position of 0 and not 1 so I will get the translation frame output to read correctly with the position of the codon in the translation frame. 
